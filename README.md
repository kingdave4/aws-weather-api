# Weather Dashboard

The **Weather Dashboard** is a Python-based tool for fetching, displaying, and storing weather data in AWS S3. It uses the OpenWeatherMap API to gather weather information for specified cities and saves the results as JSON files in an S3 bucket.

## Features

- Fetches weather data for multiple cities using the OpenWeatherMap API.
- Displays weather information such as temperature, "feels like" temperature, humidity, and weather description.
- Automatically creates an S3 bucket (with a randomized suffix) if it doesn't exist.
- Saves weather data as JSON files to the S3 bucket.

## Prerequisites

1. **AWS Account**: Ensure you have an AWS account with appropriate permissions to create and use S3 buckets.
2. **OpenWeatherMap API Key**: Sign up for an API key from [OpenWeatherMap](https://openweathermap.org/api).
3. **Environment File**: Create a `.env` file in the project directory with the following variables:
   ```plaintext
   WEATHER_API_KEY=<your_openweathermap_api_key>
   AWS_BUCKET_NAME=<base_name_for_your_bucket>
   AWS_ACCESS_KEY_ID=<your_aws_access_key_id>
   AWS_SECRET_ACCESS_KEY=<your_aws_secret_access_key>
   AWS_DEFAULT_REGION=<aws_region>


Installation
Clone this repository:
bash

git https://github.com/kingdave4/aws-weather-api.git
cd aws-weather-api.git


Install the required Python packages:
bash

pip install -r requirements.txt


bash
python weather_dashboard.py



The program will:

Attempt to create an S3 bucket if it doesn't already exist.
Fetch weather data for predefined cities (Toronto, Calgary, Ottawa, Vancouver, Montreal).
Display the weather information in the terminal.
Save the fetched data as JSON files in the S3 bucket.


Example Output

![image](https://github.com/user-attachments/assets/2b7ab102-190d-4506-af49-1b735cecf920)



Project Structure

├── weather_dashboard.py      # Main script
├── requirements.txt          # Python dependencies
├── .env 


Dependencies
boto3: For interacting with AWS S3.
requests: For making HTTP requests to the OpenWeatherMap API.
python-dotenv: For managing environment variables.


Install them using:
bash

pip install boto3 requests python-dotenv

