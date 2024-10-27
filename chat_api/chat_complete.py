import openai
import threading
from chat_api import logger
from config import MAX_OUTPUT_TOKENS, MAX_CONTEXT_TOKENS, MODEL_ID

def initialize(api_key):
    openai.api_key = api_key

def count_tokens(text):
    # This function counts the number of tokens in the input text.
    # Note: The actual token count in a specific language model might differ slightly.
    return len(text.split())

def fetch_response(user_input, callback):
    def run():
        if count_tokens(user_input) > MAX_CONTEXT_TOKENS:
            error_message = f"Error: Input exceeds the maximum allowed {MAX_CONTEXT_TOKENS} tokens."
            logger.log_response(error_message)
            callback(error_message)
            return

        response = openai.ChatCompletion.create(
            model=MODEL_ID,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=MAX_OUTPUT_TOKENS
        )
        response_text = response['choices'][0]['message']['content']
        logger.log_response(response_text)
        callback(response_text)
    thread = threading.Thread(target=run)
    thread.start()

def get_chat_response(user_input, callback):
    fetch_response(user_input, callback)
