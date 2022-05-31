# from constructs import Construct
# from aws_cdk import (
#     Duration,
#     Stack,
#     aws_iam as iam,
#     aws_sqs as sqs,
#     aws_sns as sns,
#     aws_sns_subscriptions as subs,
# )


# class CdkWorkshopStack(Stack):

#     def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
#         super().__init__(scope, construct_id, **kwargs)

#         queue = sqs.Queue(
#             self, "CdkWorkshopQueue",
#             visibility_timeout=Duration.seconds(300),
#         )

#         topic = sns.Topic(
#             self, "CdkWorkshopTopic"
#         )

#         topic.add_subscription(subs.SqsSubscription(queue))


import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (aws_apigateway as apigateway,
                     aws_s3 as s3,
                     Stack,
                     aws_lambda as awslambda
                     )

import aws_cdk.aws_lambda_python_alpha as lambda_

class AwsCdkPythonDevcontainerMainStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # bucket = s3.Bucket(self, "TestNikhita667")

        handler = lambda_.PythonFunction(self, "TestLambda",
                    entry="cdk_workshop/lambda",
                    index="main.py",
                    handler="lambda_handler",
                    function_name="TestLambda",
                    runtime=awslambda.Runtime.PYTHON_3_7,
                    timeout=cdk.Duration.seconds(300),
                    environment={"ENV": "dev"}
                    )

        # bucket.grant_read_write(handler)

        # api = apigateway.RestApi(self, "test-api",
        #           rest_api_name="Test Service",

        #           description="This is a Test.")

        # get_widgets_integration = apigateway.LambdaIntegration(handler,
        #         request_templates={"application/json": '{ "statusCode": "200" }'})

        # api.root.add_method("GET", get_widgets_integration) 

