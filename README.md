# Weather Dashboard

### Welcome to my first devops challenge of the 30 Days Challenge!. 
I am excited to start this journey of learning cloud technologies and tackling  all the hands-on projects together.


#### Weather Dashboard : uses a Python script to fetch weather data from the OpenWeatherMap API for specific cities mentioned in the list and saves the data in an AWS S3 bucket. Let's dive in!


### Prerequisites for the project

AWS Account: Ensure you have an AWS account with permissions to create and use S3 buckets.

OpenWeatherMap API Key:
   
    Sign up for an API key at https://openweathermap.org
    Copy your API key and store it in a .env file.


For the environment Variables: Create a .env file in the project directory and include the following:

WEATHER_API_KEY=<your_openweathermap_api_key>

AWS_BUCKET_NAME=<base_name_for_your_bucket>


![image](https://github.com/user-attachments/assets/078a4087-fd47-43cd-93b9-f3ef1d2bb0ce)


### AWS Setup on account the local computer

Security credential : Login to your AWS account and go to IAM > Users > Security Credentials and then generate your CLI access key. 
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

Hint: Use the information from the access key you generated to find your access key and secret key.


### Installation
Clone this repository:

git clone https://github.com/kingdave4/aws-weather-api.git

cd aws-weather-api


### Install the required Python packages version:

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

