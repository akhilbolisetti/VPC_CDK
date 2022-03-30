import aws_cdk as core
import aws_cdk.assertions as assertions

from first_vpc.first_vpc_stack import FirstVpcStack

# example tests. To run these tests, uncomment this file along with the example
# resource in first_vpc/first_vpc_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = FirstVpcStack(app, "first-vpc")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
