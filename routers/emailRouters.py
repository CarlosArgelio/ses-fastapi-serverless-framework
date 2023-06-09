# python
import json

# fastApi
from fastapi import APIRouter
from fastapi.responses import JSONResponse

# services
from services.emailsServices import Inbox, inbox_schema

emailRouter = APIRouter()

emails = []

@emailRouter.post(
    path='/api/v1/send-email-for-user',
    tags=['Emails']
)
def post_send_email_for_user(inbox: Inbox) -> dict:

    item = json.loads(inbox.json())
    emails.append(item)

    print(inbox_schema)
    return JSONResponse(status_code=200, content={"message": "success", "data": item})