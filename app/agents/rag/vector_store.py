from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def build_context(docs):

    context = ""

    for d in docs:
        context += d["content"] + "\n"

    return context