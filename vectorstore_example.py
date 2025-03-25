from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

# Load PDF
pdf_loader = PyPDFLoader("data/masterplan.pdf")
pdf_documents = pdf_loader.load()

# Load TXT using TextLoader
text_loader = TextLoader("data/prices.txt")
prices_documents = text_loader.load()

documents = pdf_documents + prices_documents

text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
vectorstore = InMemoryVectorStore.from_documents(texts, embeddings)


def get_context(query):
    docs = vectorstore.similarity_search(query, k=5)
    return "\n".join([doc.page_content for doc in docs])