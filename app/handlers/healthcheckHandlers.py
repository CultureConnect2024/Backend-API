from app.database import test_db_connection

async def healthcheck():
    db_version = await test_db_connection()
    if "Error" in db_version:
        return {"status": "fail", "message": db_version}
    else :
        return {"status": "success", "db_version": db_version}


