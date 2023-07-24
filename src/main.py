import tiktoken
import streamlit as st
from function import langchain_chat


def streamlit_render() -> None:
    st.set_page_config(page_title="GPT Assistant", page_icon=":rocket:")
    st.header(":rocket: GPT Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = [langchain_chat.system_message_content()]

    form_container = st.container()
    with form_container:
        with st.form(key="form_textarea", clear_on_submit=True):
            user_input = st.text_area(label="何でも聞いてくれ", key="input", height=80)
            submit_button = st.form_submit_button(label="送信")

    if user_input and submit_button:
        st.session_state.messages.append(
            langchain_chat.human_message_content(user_input)
        )
        with st.spinner("Generating ..."):
            response = langchain_chat.llm_generate(st.session_state.messages)

        st.session_state.messages.append(langchain_chat.ai_message(response.content))

        messages = st.session_state.get("messages", [])

        for message in messages:
            if langchain_chat.is_human_message(message):
                with st.chat_message("user"):
                    st.markdown(message.content)
                    st.write(f"> {encode_text_to_tokens(message.content)}")
            elif langchain_chat.is_ai_message(message):
                with st.chat_message("assistant"):
                    st.markdown(message.content)
                    st.write(f"> {encode_text_to_tokens(message.content)}")
            else:
                st.write(f"system message: {message.content}")


def encode_text_to_tokens(text: str) -> str:
    GPT_MODEL = "gpt-3.5-turbo"

    encoding = tiktoken.encoding_for_model(GPT_MODEL)
    tokens = encoding.encode(text)

    return f"Text length: {len(text)}, \
        Tokens: {tokens}, \
        Tokens length: {len(tokens)}"


if __name__ == "__main__":
    streamlit_render()
