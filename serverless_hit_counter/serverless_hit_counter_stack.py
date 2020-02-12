import os

from aws_cdk import aws_apigateway as _apigw
from aws_cdk import aws_dynamodb as _ddb
from aws_cdk import aws_lambda as _lambda
from aws_cdk import core

from constructs.counter import HitCounter


class ServerlessHitCounterStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        with open("lambda_src/hello.py", encoding="utf-8") as fp:
            my_lambda_handler_code = fp.read()

        # Define the lambda web page
        welcomeLambda = _lambda.Function(
            self,
            'welcomeLambdaId',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.inline(my_lambda_handler_code),
            handler='index.handler'
        )

        # Call the hitcounter lambda
        hit_counter = HitCounter(
            self,
            'hitCounter',
            downstream=welcomeLambda
        )

        # Define the API Gateway
        _apigw.LambdaRestApi(
            self,
            'Endpoint',
            handler=hit_counter.handler
        )
