import pytest
from src.function.langchain_chat import LangchainChat


@pytest.fixture
def langchain_chat():
    return LangchainChat()


def test_human_message_content(langchain_chat):
    question = "Hello, I am human. How do you do?"
    human_message = langchain_chat.human_message_content(question)

    assert human_message.content == question
