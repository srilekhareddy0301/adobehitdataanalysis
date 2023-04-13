# Adobe Hit Data Analysis

This project involves analyzing revenue data per keyword from a third-party search engine using AWS Glue.

## Prerequisites
Before getting started with this project, make sure you have completed the following pre-requisites:

- Install AWS CLI on your local system.
- Create an IAM user with appropriate roles and policies for S3, Glue, and CodeCommit.
- Create an AWS profile with the Access Key ID and Secret Access Key of the IAM user.
- Copy the relevant data files from your local system to an S3 bucket.
- Create a CodeCommit repository to store your code.
- Generate Git credentials for the CodeCommit repository.
- Set up the AWS profile and Git credentials in your local IDE for code development.
- Develop the code for revenue data analysis per keyword and push it to the CodeCommit repository.
- Test the AWS Glue job to ensure it's working correctly.

## Usage
To use this project, follow these steps:

-	Install AWS CLI on your local system if you haven't already done so: You can download and install AWS CLI from the AWS official documentation based on your operating system.
-	Create an IAM user with appropriate roles and policies for S3, Glue, and CodeCommit in the AWS Management Console: Go to the AWS Management Console, navigate to the IAM service, and create a new IAM user with the necessary permissions for accessing S3, Glue, and CodeCommit services. Make sure to note down the Access Key ID and Secret Access Key for later use.
-	Create an AWS profile using the Access Key ID and Secret Access Key of the IAM user in your local system: Open a terminal or command prompt on your local system and run the aws configure command. Enter the Access Key ID, Secret Access Key, and other required information when prompted to create a new AWS profile. This profile will be used for authentication when interacting with AWS services from your local system.
-	Copy the relevant data files from your local system to an S3 bucket using the AWS CLI: Use the aws s3 command-line interface to upload the relevant data files from your local system to an S3 bucket. For example: aws s3 cp <local_path> s3://<bucket_name>/<s3_path>.
-	Create a CodeCommit repository in the AWS Management Console to store your code: Go to the AWS Management Console, navigate to the CodeCommit service, and create a new CodeCommit repository to store your code. Note down the repository URL for later use.
-	Generate Git credentials for the CodeCommit repository: In the AWS Management Console, go to the CodeCommit repository settings and generate Git credentials (username and password) that will be used for authentication when pushing your code to the repository.
-	Set up the AWS profile and Git credentials in your local IDE for code development: Configure your local IDE (Integrated Development Environment) to use the AWS profile and Git credentials that you created earlier. This will allow you to interact with AWS services and push code to the CodeCommit repository directly from your IDE.
-	Develop the code for revenue data analysis per keyword using AWS Glue: Use AWS Glue, a managed extract, transform, and load (ETL) service provided by AWS, to develop the code for revenue data analysis per keyword. This may involve creating Glue jobs, writing Glue scripts in Python or Scala, and configuring Glue data sources and data targets.
-	Push the code to the CodeCommit repository using Git commands: Use Git commands from your local IDE or terminal to push the developed code to the CodeCommit repository. This may involve creating a local Git repository, adding files to the repository, committing changes, and pushing changes to the remote repository using the Git credentials generated earlier.
-	Test the AWS Glue job in the AWS Management Console to ensure it's working correctly: Go to the AWS Management Console, navigate to the Glue service, and run the Glue job that you developed earlier to analyze revenue data per keyword. Monitor the job's status and check the output to ensure it's producing the expected results.



 
