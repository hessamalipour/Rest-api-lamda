# Rest API Lambda

![alt text](https://raw.githubusercontent.com/hessamalipour/Rest-api-lamda/master/Img/Rest-AWS.jpg)

An example of deploying AWS Lambda functions with Ansible “Deploying Amazon Lambda Functions with Ansible.”
``
## Requirements 
To run this, you will need:

- Python and a recent pip 
- Ansible 2.5+ (`pip install ansible`) 
- Boto, configured to work on your target AWS account (pip install boto) 
- The AWS CLI (`pip install awscli`)

## Usage

Make a new S3 bucket in your default boto region with versioning on, and update playbook.yml so the s3_bucket var has the correct bucket name, and aws_region with the region it is in, which is where the Lambda etc. will be created too.

Run `ansible-playbook playbook.yml`. It will create a Cloudformation stack in your AWS account called my-lambda-function.

There is two codes `put.py` and `get.py` to test **Lambda**. First need to add the **API Gateway** address to the codes.

1. collect the API Gateway address in outputs of CloudFormation "**apiGatewayInvokeURL**"
2. Edit `put.py` and `get.py` and replace your address in line '5': 
"`url = '{API Gateway address}/hello/hessam'`". In addition in line '6' you can change date of birth "`data = {"dateOfBirth": "2000-08-25"}`"
3. First run `python put.py` first will check if existed table's **hessam** in DynamoDB, if not exited, will create table and show this message:
"`{
    "error": "DynamoDB is creating. please try again one minute later."
}`" 
after two mins again run `python put.py` will show "{}"
4. Second run `python get.py` that will show this message for example 
"`{
    "message": "Hello, hessam! your birthday is in 361 days"
}`"
