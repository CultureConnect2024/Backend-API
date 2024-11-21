from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from fastapi import Request
from app.handlers.userHandlers import get_users as fetch_user, add_user_to_db


from app.models.user import User


router = APIRouter()

@router.get("/",response_class=JSONResponse)
async def get_users():
    user = await fetch_user()
    return {"message": user}


@router.post("/")
async def create_user(request: Request ,user: User):
    result = await add_user_to_db(email=user.email, name=user.name)
    
    if result["status"] == "success":
        return JSONResponse(content={"message": "User created successfully"})
    else:
        raise HTTPException(status_code=400, detail="Failed to create user")