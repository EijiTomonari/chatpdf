import json
import os
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

with open("env.json") as f:
    env = json.load(f)

api_key = env["api_key"]
os.environ["OPENAI_API_KEY"] = api_key

reader = PdfReader("pdf/sample.pdf")

raw_text = ''
for i, page in enumerate(reader.pages):
   text = page.extract_text()
   if text:
       raw_text += text

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function = len,
)

chunks = text_splitter.split_text(raw_text)

embeddings = OpenAIEmbeddings()

docsearch = FAISS.from_texts(chunks, embeddings)

chain = load_qa_chain(OpenAI(model_name="text-davinci-002"), chain_type="stuff")

while True:
    question = input("Ask a question: ")
    if question == "exit":
        break
    else:
        docs = docsearch.similarity_search(question)
        answer = chain.run(input_documents=docs, question=question)
        print(answer)