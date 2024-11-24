from fastapi import FastAPI

import firebase_admin
from fastapi.responses import HTMLResponse

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
def root():
    return "<h1>API connection sucessfully</h2>"

app.include_router(
    __import__("app.routes.userRoutes", fromlist=["router"]).router, 
    prefix="/users", 
    tags=["Users"]
)

app.include_router(
    __import__("app.routes.healthchekRoutes", fromlist=["router"]).router, 
    prefix="/healthcheck", 
    tags=["Healthcheck"]
)

app.include_router(
    __import__("app.auth.auth", fromlist=["router"]).router, 
    prefix="/auth", 
    tags=["Auth"]
)
