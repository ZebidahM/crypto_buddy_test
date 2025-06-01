from chatbot_core import chatbot_response
from ui_handler import chat_loop
from data_validator import validate_crypto_data

def main():
    """Runs the full chatbot application."""
    print("Welcome to CryptoBuddy! 🚀 Your AI-powered financial sidekick is ready.")
    validate_crypto_data()  # Ensure data integrity
    chat_loop()  # Begin chatbot conversation

if __name__ == "__main__":
    main()
