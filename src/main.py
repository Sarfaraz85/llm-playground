import streamlit as st
from function.langchain_chat import LangchainChat
from function.token_utils import TokenUtils

GPT_MODEL = "gpt-3.5-turbo"
tokenizer = TokenUtils(GPT_MODEL)
langchain_chat = LangchainChat()


def streamlit_render() -> None:
    """Renders the main Streamlit page."""
    st.set_page_config(page_title="GPT Assistant", page_icon=":rocket:")
    st.header(":rocket: GPT Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = [langchain_chat.system_message_content()]

    form_container = st.container()
    with form_container:
        with st.form(key="form_textarea", clear_on_submit=True):
            user_input = st.text_area(label="何でも聞いてください", key="input", height=80)
            submit_button = st.form_submit_button(label="送信")

    if user_input and submit_button:
        _handle_user_input(user_input)
        _display_messages()

    _initialize_messages()


def _handle_user_input(user_input: str) -> None:
    """Handles user input by generating a language model response."""
    st.session_state.messages.append(langchain_chat.human_message_content(user_input))
    with st.spinner("Generating ..."):
        response = langchain_chat.llm_generate(st.session_state.messages)

    st.session_state.messages.append(langchain_chat.ai_message(response.content))


def _display_messages() -> None:
    """Displays the messages in the messages session state."""
    messages = st.session_state.get("messages", [])

    for message in messages:
        if langchain_chat.is_human_message(message):
            with st.chat_message("user"):
                st.markdown(message.content)
                st.write(f"> {tokenizer.encode_text_to_tokens(message.content)}")
        elif langchain_chat.is_ai_message(message):
            with st.chat_message("assistant"):
                st.markdown(message.content)
                st.write(f"> {tokenizer.encode_text_to_tokens(message.content)}")
        else:
            st.write(f"system message: {message.content}")


def _initialize_messages() -> None:
    """Initialize messages."""
    initialize_button = st.button("クリアして最初の状態にする", key="clear")

    if initialize_button or "messages" not in st.session_state:
        st.session_state.messages = [langchain_chat.system_message_content()]


if __name__ == "__main__":
    streamlit_render()
