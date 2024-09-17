from langchain_openai import OpenAIEmbeddings, OpenAI, ChatOpenAI
from langchain_qdrant import QdrantVectorStore
from models import QueryRequest
from fastapi import HTTPException
import os
from dotenv import load_dotenv

load_dotenv()
openai_key = os.getenv('openai_key')
data_url = os.getenv('data_url')
qdrant_key = os.getenv('qdrant_key')

# Initialize embeddings and vector store
embeddings = OpenAIEmbeddings(model="text-embedding-3-large", api_key = openai_key)
vector_store = QdrantVectorStore.from_existing_collection(
    embedding = embeddings,
    collection_name="ContractorsData",
    url= data_url, 
    api_key = qdrant_key
)

async def search_vectorstore(query_request: QueryRequest):
    try:
        # Perform similarity search
        results = vector_store.similarity_search(query_request.query, k = 20)
        llm = ChatOpenAI(api_key=openai_key, model="gpt-4o")

        # Format results to return as JSON
        formatted_results = [
            {"content": res.page_content, "metadata": res.metadata}
            for res in results
        ]

        context_string = ""
        for res in results:
            context_string += 'contractor: ' + res.page_content + '\n' + 'metadata: ' + str(res.metadata) + '\n\n'

        ai_response = llm.invoke(f"Given the following contractors data: \n{context_string} \n\nAnswer the following user query: \n{query_request.query}\nIf the user query is related to contractors tell the user that you can only answer contractor related questions\nanswer: ")

        return {"results": ai_response.content}
    
    except Exception as e:
        # In case of any errors, return an HTTP exception with a 500 status code
        raise HTTPException(status_code=500, detail=str(e))
