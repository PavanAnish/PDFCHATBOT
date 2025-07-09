# app.py
from loader import load_pdf_text
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# Load PDF content
pdf_text = load_pdf_text("24HUT100 (133).pdf")

# Build prompt
template = """
You are a helpful assistant. Use the following context from a PDF to answer the user's question.

Context:
{context}

Question:
{question}

Answer:
"""

prompt = ChatPromptTemplate.from_template(template)
llm = OllamaLLM(model="llama3")
chain = prompt | llm

# Terminal loop
def chat():
    print("🤖 PDF Chatbot Ready! (type 'exit' to quit)")
    while True:
        question = input("You: ")
        if question.lower() == "exit":
            break
        result = chain.invoke({"context": pdf_text, "question": question})
        print("Bot:", result)

if __name__ == "__main__":
    chat()
