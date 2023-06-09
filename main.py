# fastApi
from fastapi import FastAPI

# mangum
from mangum import Mangum

# myRouters
from routers.emailRouters import emailRouter

# middlewares
from fastapi.middleware.cors import CORSMiddleware
from middlewares.errorHandler import ErrorHandler

app = FastAPI(
    # root_path="/api/v1"
)
app.title = "Woaka"
app.version = "0.0.1"

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    ErrorHandler,
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(emailRouter)

handler = Mangum(app)