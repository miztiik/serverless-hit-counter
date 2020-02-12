
# Serverless Hit Counter

Count the incoming hits to the website and update dynamob.

![Serverless Hit Counter](images/hitcounter.png)

  Follow this article in **[Youtube](https://www.youtube.com/c/ValaxyTechnologies)**

1. ## Prerequisites

    This demo, instructions, scripts and cloudformation template is designed to be run in `us-east-1`. With few modifications you can try it out in other regions as well(_Not covered here_).

    - AWS CLI pre-configured - [Get help here](https://youtu.be/TPyyfmQte0U)

1. ## Environment Setup

    In this repo, I have included a cloudformation template that provisions the resources to setup a fully automatic policy remedation engine.

    - **S3 Bucket**: We will use this bucket to modify its policy
    - **Cloudtrail(regional)**: Monitor all S3 Put API Events
    - **StepFunction**:
        - Evaluate new bucket policy compliance
        - If `NON COMPLIANT` retrieve previous bucket policy from AWS Config
        - Restore previous bucket policy
    - **EventBridge Rule**: Receives `PutBucketPolicy` events & triggers stepfuction
    - **IAM Roles**: For lambda and step functions with restrictive permissions

    _**Note**: Sample bucket policies to test the solution can be found in the output section of the cloudformation template_

1. ## Deployment

    You have couple of options to set this up in your account, You can use [AWS CDK](https://www.youtube.com/watch?v=MKwxpszw0Rc) or use the cloudformation template generated by CDK. All the necessary steps are baked into the templates, you can launch it and try it out.

1. ### Environment Setup

      If you have AWS CDK installed you can close this repository and deploy the stack with,

        ```sh
        # If you DONT have cdk installed
        npm install -g aws-cdk

        git clone https://github.com/miztiik
        cd serverless-hit-counter
        source .env/bin/activate
        pip install -r requirements.txt
        ```

      The very first time you deploy an AWS CDK app into an environment _(account/region)_, you’ll need to install a `bootstrap stack`, Otherwise just go aheadand   deploy using `cdk deploy`

        ```sh
        cdk bootstrap
        cdk deploy
        ```

1. ## Testing the Solution

    Access the API Gateway URL in your browser.

    - Check DynamoDB for the hit Count

1. ## CleanUp

    If you want to destroy all the resources created by the stack, Execute the below command to delete the stack, or _you can delete the stack from console as well_

    1. Delete CloudWatch Lambda LogGroups

    1. Delete the stack[s],

    ```bash
    # Delete the CF Stack
    aws cloudformation delete-stack \
        --stack-name "MiztiikStack" \
        --region "${AWS_REGION}"
    ```

    or

    ```bash
    cdk destroy
    ```

    This is not an exhaustive list, please carry out other necessary steps as maybe applicable to your needs.

## Buy me a coffee

Buy me a coffee ☕ through [Paypal](https://paypal.me/valaxy), _or_ You can reach out to get more details through [here](https://youtube.com/c/valaxytechnologies/about).

### References

1. [Open CDK](https://github.com/kevinslin/open-cdk)

1. [For Digramming/Images](https://yuml.me/diagram/scruffy/class/draw)

### Metadata

**Level**: 200
