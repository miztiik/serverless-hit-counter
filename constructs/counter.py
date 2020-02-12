from aws_cdk import aws_dynamodb as ddb
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_iam as _iam
from aws_cdk import core


class HitCounter(core.Construct):

    @property
    def handler(self):
        return self._handler

    def __init__(self, scope: core.Construct, id: str, downstream: _lambda.IFunction, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Define the DynamoDB table to store hit counts
        table = ddb.Table(
            self, 'Hits',
            partition_key={'name': 'path', 'type': ddb.AttributeType.STRING}
        )

        with open("lambda_src/request_processor.py", encoding="utf-8") as fp:
            request_processor_handler_code = fp.read()

        # Define the lambda funtion for counting hits
        self._handler = _lambda.Function(
            self, 'requestProcessorId',
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler='index.handler',
            code=_lambda.Code.inline(request_processor_handler_code),
            environment={
                'DOWNSTREAM_FUNCTION_NAME': downstream.function_name,
                'HITS_TABLE_NAME': table.table_name,
            }
        )

        # Add permission for lambda to write to table
        table.grant_read_write_data(self._handler)

        # All this Lambda to Invoke downstream Lambda
        downstream.grant_invoke(self._handler)
