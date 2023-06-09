# python
import json

# fastApi
from fastapi import APIRouter
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi import HTTPException

# services
from services.emailsServices import ApiSES

# models
from models.emailModels import Inbox

emailRouter = APIRouter()

@emailRouter.post(
    path='/api/v1/send-email-for-user',
    tags=['Emails']
)
def post_send_email_for_user(inbox: Inbox) -> dict:
    """
    # Params:

    id:uuid
    name:str
    email:str[email]
    number_phone:str[validate numbers]
        Example: 4120000000
    
    Example request Success:
    
    ```
    {
    "id": "6312cfbd-dc47-46ed-84d9-20c03aba7402",
    "name": "string",
    "email": "user@example.com",
    "number_phone": "4120000000"
    }
    ```

    Example request err:

    ```
    {
    "id": "6312cfbd-dc47-46ed-84d9-20c03aba7402",
    "name": "string",
    "email": "user@example.com",
    "number_phone": "+58-4120000000"
    }
    ```
    """

    item = json.loads(inbox.json())
    ses = ApiSES(body=inbox).send_email()

    if ses['status'] == False:
        response = {'message': f'{ses["response"]}' ,'HttpResponse': f'{status.HTTP_404_NOT_FOUND}'}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=response
        )
    else:
        resp_ses = ses['response']
    
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "success", "data": item, "response": resp_ses})