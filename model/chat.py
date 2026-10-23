from langchain_ollama import ChatOllama


def chat ():
    llm = ChatOllama(model="qwen3:1.7b", temperature=0, reasoning=False)
    response_ollama = llm.invoke("replay setup completed successfully").content 
    print(response_ollama)


if __name__ == "__main__":
    chat()