from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os
import csv

load_dotenv()
embeddings = OpenAIEmbeddings(model="text-embedding-3-large", api_key = os.getenv('openai_key'))
data_url = os.getenv('data_url')
qdrant_key = os.getenv('qdrant_key')

docs = []
with open('contractors.csv', 'r',encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if row[0] == 'Company_name':
            continue
        doc = Document(
            page_content=row[0],
            metadata={"Membership_number": row[2], "City": row[3],"Email": row[4],"Activities": row[5]}
        )
        docs.append(doc)

qdrant = QdrantVectorStore.from_documents(
    docs,
    embeddings,
    url = data_url,
    prefer_grpc = True,
    api_key = qdrant_key,
    collection_name="ContractorsData",
)
