import openai
import threading
from chat_api import logger
from config import MAX_OUTPUT_TOKENS, MAX_CONTEXT_TOKENS, MODEL_ID

def initialize(api_key):
    openai.api_key = api_key

def count_tokens(text):
    return len(text.split())

def fetch_response(user_input, callback):
    response = openai.ChatCompletion.create(
        model=MODEL_ID,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ],
        max_tokens=MAX_OUTPUT_TOKENS
    )
    response_text = response['choices'][0]['message']['content']
    callback(response_text)

def get_chat_response(user_input, callback):
    thread = threading.Thread(target=fetch_response, args=(user_input, callback))
    thread.start()
    thread.join()
