import streamlit as st
from function.langchain_chat import LangchainChat
from function.token_utils import TokenUtils


class Main:
    # GPT_MODEL = "gpt-4o-mini-2024-07-18"
    GPT_MODEL = "gpt-3.5-turbo"
    SYSTEM_PROMPT: str = "Please respond as concisely and with as little text as possible."

    tokenizer = TokenUtils(GPT_MODEL)
    langchain_chat = LangchainChat()

    def __init__(self):
        self.streamlit_render()

    def streamlit_render(self) -> None:
        """Renders the main Streamlit page."""
        st.set_page_config(page_title="GPT Assistant", page_icon=":rocket:")
        st.header(":rocket: GPT Assistant")

        if "messages" not in st.session_state:
            st.session_state.messages = [
                self.langchain_chat.system_message_content(self.SYSTEM_PROMPT)
            ]

        form_container = st.container()
        with form_container:
            with st.form(key="form_textarea", clear_on_submit=True):
                user_input = st.text_area(label="Please ask me anything", key="input", height=100)
                submit_button = st.form_submit_button(label="Send")

        if user_input and submit_button:
            self._handle_user_input(user_input)
            self._display_messages()

        self._initialize_messages()

    def _handle_user_input(self, user_input: str) -> None:
        """Handles user input by generating a language model response."""
        st.session_state.messages.append(
            self.langchain_chat.human_message_content(user_input)
        )
        with st.spinner("Generating ..."):
            response = self.langchain_chat.llm_generate(st.session_state.messages)

        st.session_state.messages.append(
            self.langchain_chat.ai_message(response.content)
        )

    def _display_messages(self) -> None:
        """Displays the messages in the messages session state."""
        messages = st.session_state.get("messages", [])

        for message in messages:
            if self.langchain_chat.is_human_message(message):
                with st.chat_message("user"):
                    st.markdown(message.content)
                    st.write(
                        f"> {self.tokenizer.encode_text_to_tokens(message.content)}"
                    )
            elif self.langchain_chat.is_ai_message(message):
                with st.chat_message("assistant"):
                    st.markdown(message.content)
                    st.write(
                        f"> {self.tokenizer.encode_text_to_tokens(message.content)}"
                    )
            else:
                st.write(f"system message: {message.content}")

    def _initialize_messages(self) -> None:
        """Initialize messages."""
        initialize_button = st.button("Clear to initial state", key="clear")

        if initialize_button or "messages" not in st.session_state:
            st.session_state.messages = [
                self.langchain_chat.system_message_content(self.SYSTEM_PROMPT)
            ]


if __name__ == "__main__":
    Main()
