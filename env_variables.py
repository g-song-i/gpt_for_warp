import configparser
import os

def load_api_key():
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '.config.ini'))
    return config['DEFAULT']['OPENAI_API_KEY']
