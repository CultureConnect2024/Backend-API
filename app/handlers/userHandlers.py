# handlers/users.py
from fastapi import HTTPException
from app.database import get_db_connection

async def get_users():
    conn = await get_db_connection() 
    try:
        query = "SELECT id, name, email FROM users"
        
        result = await conn.fetch(query)
        
        users = [{"id": row["id"], "name": row["name"], "email": row["email"]} for row in result]
            
        return users
    except Exception as e:
        return {"status": "fail", "message": str(e)}
    finally:
        await conn.close() 


async def add_user_to_db(email: str, name: str):
    conn = await get_db_connection() 
    try:
        query = "INSERT INTO users (email, name) VALUES ($1, $2)"
        await conn.execute(query, email, name)
        return {"status": "success", "message": "User added successfully"}
    except Exception as e:
        return {"status": "fail", "message": str(e)}
    finally:
        await conn.close()  

