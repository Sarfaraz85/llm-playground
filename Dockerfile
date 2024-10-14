FROM --platform=linux/x86_64 python:3.11.4-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=./

# NOTE: Uncomment if experiencing timeouts when running `docker run`
# ENV PIP_DEFAULT_TIMEOUT=600

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry==1.8.3
RUN pip install azure-identity
RUN pip install azure-keyvault-secrets

COPY pyproject.toml ./
COPY poetry.lock ./

RUN poetry config virtualenvs.create false \
  && poetry install

COPY ./src ./src
# COPY ./.env ./.env

EXPOSE 443 

CMD ["streamlit", "run", "src/main.py"]
