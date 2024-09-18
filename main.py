from fastapi import FastAPI, Depends
from security import get_api_key
from models import QueryRequest
from vector import search_vectorstore 
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

@app.post("/query")
async def search_query(query_request: QueryRequest, api_key: str = Depends(get_api_key)):
    return await search_vectorstore(query_request)
