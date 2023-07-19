import tiktoken
import streamlit as st


def streamlit_render(text: str) -> None:
    st.write(text)


def encode_text_to_tokens(text: str) -> None:
    GPT_MODEL = "gpt-3.5-turbo"

    encoding = tiktoken.encoding_for_model(GPT_MODEL)
    tokens = encoding.encode(text)

    print(f"Text length: {len(text)}")
    print(f"Tokens: {tokens}")
    print(f"Tokens length: {len(tokens)}")


if __name__ == "__main__":
    # encode_text_to_tokens("Test text.")
    streamlit_render("Hello world!!!!!!!!")
