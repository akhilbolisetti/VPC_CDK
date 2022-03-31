from compileall import compile_dir
from email.utils import encode_rfc2231
from hashlib import new
import string
import this
import aws_cdk as cdk
import aws_cdk.aws_ec2 as ec2
from aws_cdk import  (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)

from constructs import Construct

class FirstVpcStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        my_vpc = ec2.Vpc(
        self, "Myvpc",
        subnet_configuration=[
            cidr="10.13.0.0/21"
            ec2.SubnetConfiguration_public=(name="PUBLIC", cidr_mask=24,subnet_type=ec2.SubnetType.PUBLIC),
            ec2.SubnetConfiguration_private=(name="PRIVATE", cidr_mask=24,subnet_type=ec2.SubnetType.PRIVATE)
        ]
        )

        instance =  ec2.Instance(self, 'ec2-instance',instance_type=ec2.InstanceType('t2.micro'),machine_image=ec2.machine_image('ami-0c02fb55956c7d316')
        vpc=my_vpc,subnet_configuration=ec2.SubnetConfiguration_public=(name="PUBLIC", cidr_mask=24,subnet_type=ec2.SubnetType.PUBLIC) )

        instance =  ec2.Instance(self, 'ec2-instance',instance_type=ec2.InstanceType('t2.micro'),machine_image=ec2.machine_image('ami-0c02fb55956c7d317')
        vpc=my_vpc,subnet_configuration=ec2.SubnetConfiguration_private=(name="PRIVATE", cidr_mask=24,subnet_type=ec2.SubnetType.PRIVATE) )

        


      #  cidr="10.13.0.0/21",
     #   max_azs=2,
    #    nat_gateways=0,
   #     subnet_configuration=[
  #          ec2.SubnetConfiguration=(name="PUBLIC", cidr_mask=24,subnet_type=ec2.SubnetType.PUBLIC),
 #           ec2.SubnetConfiguration=(name="PRIVATE", cidr_mask=24,subnet_type=ec2.SubnetType.PRIVATE)
#
        #]    
       # )

        # example resource
        # queue = sqs.Queue(
        #     self, "FirstVpcQueue",
        #     visibility_timeout=Duration.seconds(300),
         )
