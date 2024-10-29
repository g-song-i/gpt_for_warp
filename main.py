# main.py
import sys
import time
import env_variables
import chat_api.chat_complete as chat_complete

def handle_response(response):
    print("🤖 GPT-4's response:", response)
    print("\n🔚 End of conversation.")

def main():
    api_key = env_variables.load_api_key()
    print("🚀 Starting the program...")
    chat_complete.initialize(api_key)

    while True:
        user_input = input("👉 Please enter your question ('exit' to terminate the program): ")
        if user_input.lower() == 'exit':
            print("🛑 Terminating the program.")
            break

        chat_complete.get_chat_response(user_input, handle_response)

if __name__ == "__main__":
    main()
