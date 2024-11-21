import asyncpg
from app.config import config  # import config class from config file 

# test connection to postgre
async def test_db_connection():
    try:
        conn = await asyncpg.connect(
            user=config.DB_USER,
            password=config.DB_PASS,
            database=config.DB_NAME,
            host=config.DB_HOST,
            port=config.DB_PORT
        )
        # take version of db
        version = await conn.fetchval('SELECT version()')
        await conn.close()
        return version
    except Exception as e:
        return f"Error connecting to the database: {e}"


# create connection to postgre
async def get_db_connection():
    try:
        conn = await asyncpg.connect(
            user=config.DB_USER,
            password=config.DB_PASS,
            database=config.DB_NAME,
            host=config.DB_HOST
        )
        return conn
    except Exception as e:
        raise Exception(f"Error connecting to database: {str(e)}")
        
    
