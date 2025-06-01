def welcome_message():
    return "Hey there! 🚀 I'm CryptoBuddy, your AI-powered financial sidekick. Ready to find you a green and growing crypto? Ask away!"

responses = {
    "welcome": "Hey there! 🚀 I'm CryptoBuddy, your AI-powered financial sidekick. Let's find you a promising crypto!",
    "help": "You can ask me about crypto trends, sustainability, or investment tips. Try: 'Which crypto is trending?'",
    "error": "Oops! That doesn't seem right. Try asking about crypto trends or sustainability.",
    "goodbye": "Thanks for chatting! 🚀 See you soon!"
}

def get_personality_response(response_type):
    """Returns personality-driven messages based on response type."""
    return responses.get(response_type, responses["error"])

# Conversation flow functions
def handle_trending_query():
    """Handle queries about trending cryptocurrencies."""
    from chatbot_core import crypto_db
    recommend = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
    return f"🔥 These cryptos are on the rise: {', '.join(recommend)}!"

def handle_sustainability_query():
    """Handle queries about sustainable cryptocurrencies."""
    from chatbot_core import crypto_db
    recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
    return f"🌱 Invest in {recommend}! It's eco-friendly with a strong future."

def handle_general_query():
    """Handle general or unclear queries."""
    return "Hmm... I'm not sure about that one. Try asking about trends, sustainability, or investment advice!"
