# #!/usr/bin/env python3

# import aws_cdk as cdk

# from cdk_workshop.cdk_workshop_stack import CdkWorkshopStack


# app = cdk.App()
# CdkWorkshopStack(app, "cdk-workshop")

# app.synth()

#!/usr/bin/env python3

# import aws_cdk as cdk
# from cdk_workshop.pipeline_stack import WorkshopPipelineStack

# app = cdk.App()
# WorkshopPipelineStack(app, "WorkshopPipelineStack")

# app.synth()

import os
import aws_cdk as cdk
from cdk_workshop.pipeline_stack import MyPipelineStack

app = cdk.App()
MyPipelineStack(app, "MyPipelineStack", 
    env=cdk.Environment(account="246213974221", region="us-west-2")
)

app.synth()
