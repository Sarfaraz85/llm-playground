import tiktoken
import streamlit as st


def streamlit_render() -> None:
    st.set_page_config(page_title="GPT Assistant", page_icon=":rocket:")
    st.header(":rocket: GPT Assistant")

    form_container = st.container()
    with form_container:
        with st.form(key="form_textarea", clear_on_submit=True):
            user_input = st.text_area(label="何でも聞いてくれ", key="input", height=80)
            submit_button = st.form_submit_button(label="送信")

        if user_input and submit_button:
            st.write(f"> {user_input}")
            st.write(encode_text_to_tokens(user_input))


def encode_text_to_tokens(text: str) -> str:
    GPT_MODEL = "gpt-3.5-turbo"

    encoding = tiktoken.encoding_for_model(GPT_MODEL)
    tokens = encoding.encode(text)

    return f"Text length: {len(text)}, \
        Tokens: {tokens}, \
        Tokens length: {len(tokens)}"


if __name__ == "__main__":
    streamlit_render()
