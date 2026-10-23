from dotenv import load_dotenv
load_dotenv()

from model.chat import chat
from langchain_core import __version__ as core_version
from langgraph.version import __version__ as lg_version
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama


print(f"langchain-core version :{core_version}")
print(f"langgraph version :{lg_version}")


def main ():
    
    chat()
    



if __name__ == "__main__":
    main()