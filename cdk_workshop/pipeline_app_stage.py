import aws_cdk as cdk
from constructs import Construct
from cdk_workshop.cdk_workshop_stack import AwsCdkPythonDevcontainerMainStack

class MyPipelineAppStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambdaStack = AwsCdkPythonDevcontainerMainStack(self, "LambdaStack")
