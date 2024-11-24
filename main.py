from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Mendapatkan port dari variabel lingkungan PORT
port = int(os.getenv("PORT", 8080))

# Jalankan aplikasi dengan Uvicorn dan pastikan mendengarkan pada port yang benar
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)

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
