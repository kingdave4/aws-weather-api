# Weather Dashboard

### Hello everyone Weclome to my first project of the 30 Days-of DEvops Challenge. 
I am really excited to embark on this journey of learnning cloud and working on all these hands on projects together. 
If you are still fresh on learning cloud then get ready to learn along with me and get ready because it's going hot, tough and hard but we got this and we are going to work on it together and learn together.


**Weather Dashboard** : Our first project uses to use a python script to fetch weather information data from the OpenWeather API for specific cities and then saves it to a s3 bucket.

## Key feactues of the project

- Fetches weather data for multiple cities using the OpenWeatherMap API.
- Displays weather information such as temperature, "feels like" temperature, humidity, and weather description.
- Automatically creates an S3 bucket (with a randomized suffix) if it doesn't exist (which means you never have to worry about running into a bucket name already exists error message)
- Saves weather data as JSON files to the S3 bucket.

## Prerequisites for the project

1. **AWS Account**: Make sure you have an AWS account with appropriate permissions to create and use S3 buckets.
2. **OpenWeatherMap API Key**: Sign up for an API key from [OpenWeatherMap](https://openweathermap.org/api) and get copy the API key and put it in the .env folder.
3. **Visual Studio Code**: I recommand using Visual Studio Code because its easier to follow and understand but you can use your favorite IDE. 
4. **Environment File**: Create a `.env` file in the project directory with the following variables:


WEATHER_API_KEY=<your_openweathermap_api_key>

AWS_BUCKET_NAME=<base_name_for_your_bucket>


### AWS Setup on account the local computer

Security credential : Login to your AWS account and go to IAM > Users > Security Credentials and then generte your CLI access key. 
Account setup locally : Open powershell or Git bash and then configure account locally with the following steps

Step 1: Install the AWS CLI
Check if AWS CLI is installed:

aws --version
If not installed, download and install it from the AWS CLI Installation Guide.


Step 2: Configure AWS CLI Locally
Run the following command to set up AWS CLI with your credentials:

aws configure

AWS_ACCESS_KEY_ID=<your_aws_access_key_id>
AWS_SECRET_ACCESS_KEY=<your_aws_secret_access_key>
AWS_DEFAULT_REGION=<aws_region>


### Installation
Clone this repository:

git clone https://github.com/kingdave4/aws-weather-api.git

cd aws-weather-api


### Install the required Python packages:

pip install -r requirements.txt


### Run the program:

python weather_dashboard.py


### Example Output

![image](https://github.com/user-attachments/assets/71a42957-0a0d-4577-a072-7a9c9042fc56)


### Dependencies
boto3: For interacting with AWS S3.

requests: For making HTTP requests to the OpenWeatherMap API.

python-dotenv: For managing environment variables.


#### Install them using:

pip install boto3 requests python-dotenv

