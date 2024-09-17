import os
from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN
from dotenv import load_dotenv

load_dotenv()

api_key_header = APIKeyHeader(name='Authorization', auto_error = True)
TOKEN = os.getenv('TOKEN')

def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key == TOKEN:
        return api_key
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate API key"
        )
        