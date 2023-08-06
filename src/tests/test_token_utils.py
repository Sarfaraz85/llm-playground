import pytest
from src.function.token_utils import TokenUtils


def test_encode_text_to_tokens(mocker):
    mock_encoding_for_model = mocker.patch(
        "src.function.token_utils.tiktoken.encoding_for_model"
    )

    # Set value returned by mock
    mock_encoding = mocker.Mock()
    mock_encoding.encode.return_value = [1, 2, 3]
    mock_encoding_for_model.return_value = mock_encoding
    assert len(mock_encoding.encode.return_value) == 3

    model_name = "gpt-3.5-turbo"
    tokenizer = TokenUtils(model_name)
    text = "Test"

    actual_result = tokenizer.encode_text_to_tokens(text)
    expected_result = "Text length: 4, Tokens length: 3"
    assert actual_result == expected_result
