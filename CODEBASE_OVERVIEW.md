# Codebase Overview

This project is a simple Streamlit application that integrates **LangChain** with OpenAI models to act as a small GPT-powered assistant. It exposes a chat interface where users can send messages and receive responses from a language model. The repository includes:

- `src/main.py` – the Streamlit app that maintains conversation state and renders chat messages.
- `src/function/langchain_chat.py` – a wrapper around `ChatOpenAI` to generate and identify message types.
- `src/function/token_utils.py` – a helper that shows how many tokens each message uses.
- Docker files (`Dockerfile` and `docker-compose.yml`) to build and run the app in a container.

Sample usage instructions and additional context can be found in `README.md`.
