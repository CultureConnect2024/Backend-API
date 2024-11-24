import firebase_admin
from firebase_admin import credentials, auth
from fastapi import HTTPException, APIRouter, Body
import os

router = APIRouter()

# Mendapatkan path dari environment variable
cred_path = os.getenv("FIREBASE_SERVICE_ACCOUNT_PATH", "/firebase-account/service_account.json")

# Memastikan file ada di path yang telah ditentukan
if not os.path.exists(cred_path):
    raise HTTPException(status_code=500, detail="Firebase service account file not found at the specified path")

# Menginisialisasi Firebase Admin SDK dengan file service_account.json
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

# Fungsi untuk memverifikasi ID token
def verify_firebase_token(id_token: str):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token["uid"]
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

# Endpoint untuk login
@router.post("/login")
async def login(request: dict = Body(...)):
    try:
        id_token = request.get('id-token')
        decoded_token = auth.verify_id_token(id_token)
        user_id = decoded_token["uid"]
        return {"user_id": user_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Root endpoint
@router.get("/")
def root():
    return "<h1>Auth Routes</h1>"
