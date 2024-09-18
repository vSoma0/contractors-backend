from fastapi import FastAPI, Depends
from security import get_api_key
from models import QueryRequest
from vector import search_vectorstore 
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/query")
async def search_query(query_request: QueryRequest, api_key: str = Depends(get_api_key)):
    return await search_vectorstore(query_request)
