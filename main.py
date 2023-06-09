# fastApi
from fastapi import FastAPI

# mangum
from mangum import Mangum

# myRouters
from routers.emailRouters import emailRouter


app = FastAPI(
    # root_path="/api/v1"
)
app.title = "Woaka"
app.version = "0.0.1"
app.include_router(emailRouter)

handler = Mangum(app)