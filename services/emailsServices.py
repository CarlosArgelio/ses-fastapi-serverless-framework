# python
import os
import json

# boto3
import boto3
from botocore.exceptions import ClientError

# DotEnv
from dotenv import load_dotenv

load_dotenv()

SOURCE = os.getenv('SOURCE')
TEMPLATE_NAME = os.getenv('TEMPLATE_NAME')

ses = boto3.client('ses')

class ApiSES:
    def __init__(self, body):
        self.client = ses
        self.body = body

    def send_email(self):

        try:
            data = json.dumps(self.body.json())

            send_email_template = self.client.send_templated_email(
                Source='palaciosrcarlosa2@gmail.com',
                Destination={'ToAddresses': ['palaciosrcarlosa2@gmail.com']},
                Template=TEMPLATE_NAME,
                TemplateData=data
            )
            print(send_email_template)
            response = {'status': True, 'response': send_email_template}
        except ClientError as err:
            message = err.response['Error']['Message']
            response = {'status': False, 'response': message}
        
        return response