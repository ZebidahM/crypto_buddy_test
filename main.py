from chatbot_core import chatbot_response
from ui_handler import chat_loop
from data_validator import validate_crypto_data


def main():
    """Runs the full chatbot application."""
    print("Welcome to CryptoBuddy! 🚀 Your AI-powered financial sidekick is ready.")
    if validate_crypto_data():  # Ensure data integrity
        chat_loop()  # Begin chatbot conversation
    else:
        print("❌ Startup aborted due to data validation errors.")


if __name__ == "__main__":
    main()
