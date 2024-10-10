import tiktoken


class TokenUtils:
    """A utility class for tokenization tasks.
    - This class uses a specific model to encode text into tokens and provides
    information about the length of the text and the number of tokens.

    Attributes:
        model_name (str): The name of the model to use for tokenization.
    """

    def __init__(self, model_name: str):
        """Initializes the TokenUtils class with a specific model name. (e.g. "gpt-4o-mini-2024-07-18", etc.)

        Args:
            model_name (str): The name of the model to use for tokenization.
        """
        self.model_name = model_name

    def encode_text_to_tokens(self, text: str) -> str:
        """Encodes a given text into tokens using the specified model.

        Args:
            text (str): The text to be encoded.

        Returns:
            str: Information about the length of the text and the number of tokens.
        """
        encoding = tiktoken.encoding_for_model(self.model_name)
        tokens = encoding.encode(text)

        return f"Text length: {len(text)}, Tokens length: {len(tokens)}"
