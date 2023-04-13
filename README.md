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

## Usage Steps

1. Install AWS CLI on your local system if you haven't already done so. You can download and install AWS CLI from the AWS official documentation based on your operating system.

2. Create an IAM user with appropriate roles and policies for S3, Glue, and CodeCommit in the AWS Management Console. Use the ARN of the AWS Glue service role that you have defined for your AWS platform.

3. Copy the relevant data files from your local system to an S3 bucket using the AWS CLI. For example: `aws s3 cp <local_path> s3://<bucket_name>/<s3_path>`.

4. Create a CodeCommit repository in the AWS Management Console to store your code. Note down the repository URL for later use.

5. Generate Git credentials for the CodeCommit repository. In the AWS Management Console, go to the CodeCommit repository settings and generate Git credentials (username and password) that will be used for authentication when pushing your code to the repository.

6. Set up the AWS profile and Git credentials in your local IDE for code development. Configure your local IDE (Integrated Development Environment) to use the AWS profile and Git credentials that you created earlier.

7. Update the parameters in the 'final_data.json' script to match your AWS platform and data locations. Modify the following parameters in the JSON object:
   - `roles`: Update with the ARN of the AWS Glue service role that you have defined for your AWS platform.
   - `scriptLocation`: Update with the S3 path where you have stored the Glue job script file.
   - `--spark-event-logs-path`: Update with the S3 path where you want to store the Spark event logs.
   - `--filepath`: Update with the S3 path of your input data file.
   - `--outputpath`: Update with the S3 path where you want to store the output data.
   - `--TempDir`: Update with the S3 path where you want to store temporary files.
   - `repository`: Update with the name of your CodeCommit repository.

8. Save the 'final_data.json' script with the updated parameters.

9. Push the code to the CodeCommit repository using Git commands. Use Git commands from your local IDE or terminal to push the updated Glue job script to the CodeCommit repository.

10. Test the AWS Glue job in the AWS Management Console to ensure it's working correctly. Go to the AWS Management Console, navigate to the Glue service, and run the Glue job that you updated earlier to analyze revenue data per keyword. Monitor the job's status and check the output to ensure it's producing the expected results.

Make sure to replace the placeholder values with the actual values specific to your AWS platform, data locations, and CodeCommit repository. This will ensure that the Glue job runs successfully with the correct configurations for your environment.



 
