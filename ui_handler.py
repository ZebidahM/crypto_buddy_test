def chat_loop():
    """Handles continuous user interaction."""
    from chatbot_core import chatbot_response
    from personality import get_personality_response
    
    print(get_personality_response("welcome"))
    print("Type 'help' for assistance or 'exit' to quit.")
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() == "exit":
            print(f"CryptoBuddy: {get_personality_response('goodbye')}")
            break
        elif user_input.lower() == "help":
            print(f"CryptoBuddy: {get_personality_response('help')}")
        else:
            response = chatbot_response(user_input)
            print(f"CryptoBuddy: {response}")

def display_sample_interactions():
    """Shows example conversations for demonstration."""
    print("Sample Conversations:")
    print("=" * 50)
    
    sample_conversations = [
        ("User: Which crypto is trending?", "CryptoBuddy: 🔥 These cryptos are on the rise: Bitcoin, Cardano, Solana!"),
        ("User: What's the most sustainable coin?", "CryptoBuddy: 🌱 Invest in Algorand! It's eco-friendly with a strong future."),
        ("User: How does crypto work?", "CryptoBuddy: 🤔 I didn't quite get that. Try asking about trends or sustainability!")
    ]
    
    for user_msg, bot_msg in sample_conversations:
        print(user_msg)
        print(bot_msg)
        print("-" * 30)
