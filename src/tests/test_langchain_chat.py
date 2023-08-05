import pytest
from src.function.langchain_chat import LangchainChat


@pytest.fixture
def langchain_chat() -> LangchainChat:
    return LangchainChat()


def test_system_message_content(langchain_chat: LangchainChat):
    system_message = langchain_chat.system_message_content(
        "Keep your replies as brief and as few sentences."
    )

    assert system_message.content == "Keep your replies as brief and as few sentences."


def test_human_message_content(langchain_chat: LangchainChat) -> None:
    question = "Hello, I am human. How do you do?"
    human_message = langchain_chat.human_message_content(question)

    assert human_message.content == question


def test_ai_message(langchain_chat: LangchainChat):
    response = "I'm AI."
    ai_message = langchain_chat.ai_message(response)

    assert ai_message.content == response


def test_is_human_message(langchain_chat: LangchainChat) -> None:
    message = "Hello, I am human. How do you do?"
    human_message = langchain_chat.human_message_content(message)

    assert langchain_chat.is_human_message(human_message) is True
    assert langchain_chat.is_ai_message(human_message) is False


def test_is_ai_message(langchain_chat: LangchainChat) -> None:
    response = "I'm AI."
    ai_message = langchain_chat.ai_message(response)

    assert langchain_chat.is_ai_message(ai_message) is True
    assert langchain_chat.is_human_message(ai_message) is False
