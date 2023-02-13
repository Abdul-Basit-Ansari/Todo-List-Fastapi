from fastapi import FastAPI
from api import api_router
from starlette.templating import Jinja2Templates

from sqlalchemy.orm import Session
from database import engine
import models

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.include_router(api_router)
