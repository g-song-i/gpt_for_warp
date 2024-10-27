import chat_api.chat_complete as chat_complete
import env_variables
import time

response_received = False
response_content = ""

def handle_response(response):
    global response_received, response_content
    response_content = response
    response_received = True
    print("🤖 GPT-4's response:", response)

def main():
    global response_received, response_content
    api_key = env_variables.load_api_key()
    print("🚀 Starting the program...")
    chat_complete.initialize(api_key)

    while True:
        response_received = False 
        user_input = input("👉 Please enter your question ('exit' to terminate the program): ")
        if user_input.lower() == 'exit':
            print("🛑 Terminating the program.")
            break

        chat_complete.get_chat_response(user_input, handle_response)

        while not response_received:
            time.sleep(0.1)

if __name__ == "__main__":
    main()
