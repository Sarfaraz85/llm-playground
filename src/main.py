import tiktoken
import streamlit as st


def streamlit_render(text: str) -> None:
    st.set_page_config(page_title="GPT Assistant", page_icon=":rocket:")
    st.header(":rocket: GPT Assistant")

    st.write(text)


def encode_text_to_tokens(text: str) -> str:
    GPT_MODEL = "gpt-3.5-turbo"

    encoding = tiktoken.encoding_for_model(GPT_MODEL)
    tokens = encoding.encode(text)

    return f"Text length: {len(text)}, \
        Tokens: {tokens}, \
        Tokens length: {len(tokens)}"


if __name__ == "__main__":
    sample_text = "Hello world!!!!!!!!"
    tokens_info = encode_text_to_tokens(sample_text)

    streamlit_render(f"{sample_text}\n\n{tokens_info}")
