# Py LLM

This repository contains a sample Dockerized Python application that uses LangChain and Streamlit together. The application encodes a given text into GPTed and displays it using Streamlit.

__Note:__ This repository is intended for personal verification purposes and is not primarily intended for production development use. Preparation is required to use OpenAI's LangChain.

## Sample Usage

### Building and Running Locally

You can build the Docker image and launch the application using the following commands:

- Prepare `.env` file

  ```sh
  cp .env.sample .env
  ```

- Set `OPENAI_API_KEY` (required)

- docker build and docker run

  ```sh
  docker build -t py_llm .
  ```

  ```sh
  docker run --rm -p 8501:8501 -e OPENAI_API_KEY=$(cat .env | grep OPENAI_API_KEY | cut -d '=' -f2) py_llm
  ```

- After launch, access http://localhost:8501 in your browser to display the application's UI.

## Application Features

WIP
