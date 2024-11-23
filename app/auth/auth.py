import firebase_admin
from firebase_admin import credentials, auth
from fastapi import HTTPException, APIRouter, Header
import os
from fastapi import HTTPException, APIRouter, Body


# find service_account.json
base_dir = os.path.dirname(os.path.abspath(__file__))  
cred_path = os.path.join(base_dir, '..', '..', 'service_account.json')

# Initial firebase admin
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

def verify_firebase_token(id_token: str):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token["uid"]
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")


router = APIRouter()



@router.post("/")
async def login(request: dict = Body(...)):
    try:
        id_token = request.get('id-token')  
        decoded_token = auth.verify_id_token(id_token)
        user_id = decoded_token["uid"]
        return {"user_id": user_id}  
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

