# Amazon EBS Migration Script - gp2 to gp3

This repository contains code samples that makes it easy for AWS customers to migrate their existing Amazon EBS gp2 volumes to the latest generation gp3 volumes at scale. By migrating to gp3, customers can save up to 20% lower price-point per GB than existing gp2 volumes.

## Key Details (Do not skip this section)

> IMPORTANT: To kick off the upgrade from gp2 to gp3, you will need to create a Lambda function in your AWS account using the supported migration scripts, and invoke it manually to trigger the EBS migration process. 

Please note that upon execution, the Lambda function by default will upgrade **ALL** gp2 EBS volumes in your account to gp3. If you need to back out, there is no easy button in this version of the application. If you need to revert back from gp3 to gp2 this will have to be done manually. You can [modify](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/requesting-ebs-volume-modifications.html) your volume(s) using the Console/CLI/SDK. In some cases, the modify volume operation may fail and you may need to wait for 6 hours before you can modify your volume(s) back to gp2. For more details please see the limitations [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-volume-requirements.html#elastic-volumes-limitations).

 Depending on how many gp2 volumes are present in your AWS account and target region, the Lambda may take anywhere from a few seconds to a couple of minutes to complete. Please note that even though the Lambda function may complete in a couple of minutes, depending on how large your gp2 volumes are, the upgrade will be running in the background and may take a couple of hours to complete. There is no limit to the number of times you can invoke your Lambda function.

## Getting Started

Below is a high level set of steps you will need to follow to deploy the solution:

1. Create a Lambda function with a runtime of Python 3.7 and above.

1. Copy and paste the migration script from the ```migrate-gp2-to-gp3.py``` file in this repository. 

1. Execute the migration process by invoking the Lambda function. 

## Security

If you discover a potential security issue in this project we ask that you notify AWS/Amazon Security via our [vulnerability reporting page](https://aws.amazon.com/security/vulnerability-reporting/). Please do not create a public github issue.

## Next Steps

We are actively iterating on this project to add more features and functionality.  We'd love to get your input and hear from you. See [CONTRIBUTING](CONTRIBUTING.md) for details on how you could help.

## License

This library is licensed under the MIT-0 License. See the [LICENSE](LICENSE) file.