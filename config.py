import os

# This module contains configuration settings for the chat application.

# Retrieve the OpenAI API key from the environment variables.
# This API key is used to interact with the OpenAI API for generating responses.
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# CHAT_SETTINGS is a dictionary that contains settings for the chat application.
# "temperature" is a parameter that controls the randomness of the generated responses.
# Lower values (e.g., 0.4) make the responses more focused and deterministic,
# while higher values (e.g., 1.0) make the responses more diverse and creative.
# "max_tokens" is the maximum number of tokens (words or word pieces) in the generated response.
CHAT_SETTINGS = {
    "temperature": 0.4,
    "max_tokens": 4000,
}
