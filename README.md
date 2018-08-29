Rest--api-lambda

An example of deploying AWS Lambda functions with Ansible
“Deploying Amazon Lambda Functions with Ansible.”

Requirements
To run this, you will need:

Python and a recent pip
Ansible 2.5+ (pip install ansible)
Boto, configured to work on your target AWS account (pip install boto)
The AWS CLI (pip install awscli)
Usage
Make a new S3 bucket in your default boto region with versioning on, and update playbook.yml so the s3_bucket var has the correct bucket name, and aws_region with the region it is in, which is where the Lambda etc. will be created too.

Run ansible-playbook playbook.yml. It will create a Cloudformation stack in your AWS account called my-lambda-function.
