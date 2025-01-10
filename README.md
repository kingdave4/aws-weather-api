# Weather Dashboard

### Welcome to my first devops challenge of the 30 Days Challenge!. 
I am excited to start this journey of learning cloud technologies and tackling  all the hands-on projects together.


### Weather Dashboard : 
Uses a Python script to fetch weather data from the OpenWeatherMap API for specific cities mentioned in the list and saves the data in an AWS S3 bucket. Let's dive in!


### Prerequisites for the project

AWS Account: ensure you have an aws account with permissions to create and use S3 buckets.
Go to IAM service, and then go to users to generate an access key adn then download it. 

Used the downloaded access key and use the "aws configure" to login aws locally using cli. 

If you don't have AWS CLI installed thne please do that first.

    AWS_ACCESS_KEY_ID=<your_aws_access_key_id>

    AWS_SECRET_ACCESS_KEY=<your_aws_secret_access_key>

    AWS_DEFAULT_REGION=<aws_region


Environment Variables: create a .env file in the project directory and include the following:

WEATHER_API_KEY=<your_openweathermap_api_key>

      Sign up for an API key at https://openweathermap.org
      Copy your API key and store it in a .env file.

AWS_BUCKET_NAME=<base_name_for_your_bucket>


### Installation
Clone this repository:

    git clone https://github.com/kingdave4/aws-weather-api.git
    cd aws-weather-api

### Dependencies

boto3: For interacting with AWS S3.

requests: For making HTTP requests to the OpenWeatherMap API.

python-dotenv: For managing environment variables.


### Install the required Python packages version:
    pip install -r requirements.txt



#### Install them using:
    pip install boto3 requests python-dotenv


### Run the program:
    python weather_dashboard.py


### Example Output
![image](https://github.com/user-attachments/assets/71a42957-0a0d-4577-a072-7a9c9042fc56)



