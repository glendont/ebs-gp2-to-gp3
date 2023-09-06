# Amazon EBS Migration Script - gp2 to gp3

This repository contains code samples that makes it easy for AWS customers to migrate their existing Amazon EBS gp2 volumes to the latest generation gp3 volumes at scale. By migrating to gp3, customers can save up to 20% lower price-point per GB than existing gp2 volumes.

## Key Details (Do not skip this section)

> IMPORTANT: To kick off the upgrade from gp2 to gp3, you will need to invoke the Lambda function that the SAM Template/CloudFormation creates in your AWS account. Please note that upon execution, the Lambda function by default will upgrade **ALL** gp2 EBS volumes in your account to gp3. If you need to back out, there is no easy button in this version of the application. If you need to revert back from gp3 to gp2 this will have to be done manually. You can [modify](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/requesting-ebs-volume-modifications.html) your volume(s) using the Console/CLI/SDK. In some cases, the modify volume operation may fail and you may need to wait for 6 hours before you can modify your volume(s) back to gp2. For more details please see the limitations [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-volume-requirements.html#elastic-volumes-limitations).

There will be no changes made to any of your other EBS volume types like io1, io2, sc1, st1, etc. If you have any gp2 EBS volumes that you don't want upgraded, you will need to tag each EBS volume with the key **upgrade_to_gp3** and set the value to ***no*** or ***false***. This will make the Lambda code skip those volumes and they will be untouched.

 Depending on how many gp2 volumes are present in your AWS account and target region, the Lambda may take anywhere from a few seconds to a couple of minutes to complete. Please note that even though the Lambda function may complete in a couple of minutes, depending on how large your gp2 volumes are, the upgrade will be running in the background and may take a couple of hours to complete. There is no limit to the number of times you can invoke your Lambda function.

## Getting Started

The easiest way to deploy this stack is from the [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:065399810791:applications~amazon-ebs-migration-utility).

Alternatively, you can also use the SAM CLI along with the provided ```template.yaml``` file to [deploy](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-deploy.html) at scale across multiple AWS accounts and in different AWS regions. You can use the below example syntax to integrate your deployment into your CI/CD process and deploy this utility at scale in your enterprise environment.

```bash
sam deploy --region <AWS region name> --template-file </path/to/template.yaml> --stack-name <your stack name> --capabilities CAPABILITY_IAM --s3-bucket <your S3 bucket name> --parameter-overrides "TargetEmail=name@example.com"
```

Below is a high level set of steps you will need to follow to deploy at scale:

1. Create or identify an existing S3 bucket in each AWS region you will be deploying to. The S3 bucket is required to hold the Lambda code and the CloudFormation template.
1. Clone this repository to your local development environment
1. Make necessary updates to the ```template.yaml``` file.  In the *AWS::Lambda::Function* section, put in the appropriate values for S3Bucket and S3Key. The S3Key will be the name of the zip file you will be creating in the next step
1. Create a zip file with the contents of this repository which will become your Lambda deployment package.
1. Upload the zip file to your S3 bucket
1. Execute the sam deploy command with the appropriate parameters.

## Security

If you discover a potential security issue in this project we ask that you notify AWS/Amazon Security via our [vulnerability reporting page](https://aws.amazon.com/security/vulnerability-reporting/). Please do not create a public github issue.

## Next Steps

We are actively iterating on this project to add more features and functionality.  We'd love to get your input and hear from you. See [CONTRIBUTING](CONTRIBUTING.md) for details on how you could help.

## License

This library is licensed under the MIT-0 License. See the [LICENSE](LICENSE) file.