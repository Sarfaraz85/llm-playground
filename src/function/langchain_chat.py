from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
import os


os.getenv("OPENAI_API_KEY")


def chat(question: str):
    llm = ChatOpenAI(temperature=0.1)

    questions = [
        SystemMessage(content="なるべく簡潔かつ文量少なく返答せよ。"),
        HumanMessage(content=question),
    ]
    response = llm(questions)

    return response
