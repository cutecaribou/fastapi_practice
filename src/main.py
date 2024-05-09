from fastapi import FastAPI
from .routers import nyan_router


app = FastAPI()

app.include_router(nyan_router)
