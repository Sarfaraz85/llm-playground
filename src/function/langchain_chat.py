from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

class LangchainChat:
    """A utility class for generating and managing chat messages.
    - This class provides methods for generating AI and human messages,
        and also for identifying the type of a message.
    """

    def __init__():
        vaultUri = "https://sarfaraz-openai-api-key.vault.azure.net"
        credential = DefaultAzureCredential()
        self.vaultClient = SecretClient(vault_url=vaultUri, credential=credential)
        vault_secret = vaultClient.get_secret("Sarfaraz-OPENAI-API-KEY")
        os.setenv("OPENAI_API_KEY", vault_secret.value)

    def system_message_content(self, prompt: str) -> SystemMessage:
        """Generates a SystemMessage with a predefined content."""
        return SystemMessage(content=prompt)

    def human_message_content(self, question: str) -> HumanMessage:
        """Wraps the given question into a HumanMessage."""
        return HumanMessage(content=question)

    def llm_generate(
        self, messages: list[SystemMessage | HumanMessage | AIMessage]
    ) -> AIMessage:
        """Generates a language model response based on given messages."""
        os.getenv("OPENAI_API_KEY")

        llm = ChatOpenAI(temperature=0.1)
        response = llm(messages)

        return response

    def ai_message(self, response_content: str) -> AIMessage:
        """Wraps the given content into an AIMessage."""
        return AIMessage(content=response_content)

    def is_human_message(
        self, message: SystemMessage | HumanMessage | AIMessage
    ) -> bool:
        """Determines whether the given message is a HumanMessage."""
        return isinstance(message, HumanMessage)

    def is_ai_message(self, message: SystemMessage | HumanMessage | AIMessage) -> bool:
        """Determines whether the given message is an AIMessage."""
        return isinstance(message, AIMessage)
