import os
import json
import boto3
import random
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class WeatherDashboard:
    def __init__(self):
        self.api_key = os.getenv('WEATHER_API_KEY')   # initializing OpenWeatherMap API key
        # Generate a randomized bucket name
        base_bucket_name = os.getenv('AWS_BUCKET_NAME') # Get the base bucket name from the environment
        random_suffix = random.randint(0, 32767)  # Generate a random number like ${RANDOM} in Bash
        self.bucket = f"{base_bucket_name}-{random_suffix}"  # Append the random number to the bucket name
        self.s3_client  = boto3.client('s3')       # initializing  S3 client

    def create_s3_bucket_if_does_not_exist(self):
        """Create S3 bucket if it does not exist"""

        try:
            self.s3_client.head_bucket(Bucket=self.bucket)
            print(f"Bucket {self.bucket} already exists")
        except:
            print(f"Bucket is being Created...")

        try:
            self.s3_client.create_bucket(Bucket=self.bucket, CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
            print(f"Bucket {self.bucket} has been created successfully") 
        except Exception as e:
            print(f"Error creating bucket: {e}")

    
    def fetch_weather_data(self, city):
        """Fetch weather data from OpenWeatherMap API"""
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None

    

    def save_to_s3(self, weather_data, city):
        """Save weather data to S3 bucket"""
        if not weather_data:
            print("No data to save")
            return False
        timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        file_name = f"weather_data_/{city}_{timestamp}.json"
     
        try:
            self.s3_client.put_object(Bucket=self.bucket, 
                Key=file_name, 
                Body=json.dumps(weather_data),
                ContentType='application/json')
            print(f"Data saved to S3 bucket {self.bucket} with key {file_name}")
            return True
        except Exception as e:
            print(f"Error saving data to S3: {e}")
            return False
        
def main():
    dashboard = WeatherDashboard()
    
    # Create bucket if needed
    dashboard.create_s3_bucket_if_does_not_exist()
    
    cities = ["Toronto", "Calgary", "Ottawa", "Vancouver", "Montreal"]

    for city in cities:
        print(f"Fetching weather data for {city}...")
        weather_data = dashboard.fetch_weather_data(city)
        if weather_data:
            temp = weather_data['main']['temp']
            feels_like = weather_data['main']['feels_like']
            humidity = weather_data['main']['humidity']
            description = weather_data['weather'][0]['description']

            print(f"Temperature: {temp}°C")
            print(f"Feels like: {feels_like}°C")
            print(f"Humidity: {humidity}%")
            print(f"Description: {description}")

            # Save data to S3
            success = dashboard.save_to_s3(weather_data, city)
            if success:
                print(f"weather data for {city} saved successfully")
                print("\n---------------------------------------------------")
        else:
            print(f"failed to save weather data for {city}")
if __name__ == "__main__":
    main() 




      


        