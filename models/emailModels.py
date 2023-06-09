# python
import os
import json

# boto3
import boto3
from botocore.exceptions import ClientError

# DotEnv
from dotenv import load_dotenv

load_dotenv()

SOURCE = os.environ['SOURCE']
TEMPLATE_NAME = os.environ['TEMPLATE_NAME']

ses = boto3.client('ses')

class ApiSES:
    def __init__(self, body):
        self.client = ses
        self.body = body

    def send_email(self):

        try:
            data = json.dumps(self.body.json())

            send_email_template = ses.send_templated_email(
                Source      =   SOURCE,
                Destination =   {'ToAddresses': [SOURCE]},
                Template    =   TEMPLATE_NAME,
                TemplateData=   data
            )

            response = {'status': True, 'response': json.dumps(send_email_template, indent=4, sort_keys=True, default=str)}
        except ClientError as err:
            message = err.response['Error']['Message']
            response = {'status': False, 'response': message}
        
        return response