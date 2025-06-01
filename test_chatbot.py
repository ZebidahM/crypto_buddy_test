def test_chatbot():
    """Runs basic test cases to validate chatbot responses."""
    from chatbot_core import chatbot_response
    
    test_cases = [
        "Which crypto is trending?",
        "What's the most sustainable coin?", 
        "Tell me about long-term investment options.",
        "Which crypto is most profitable?",
        "Give me eco-friendly coins",
        "How does crypto work?",  # Should trigger error handling
        "Random nonsense text"   # Should trigger error handling
    ]
    
    print("Running Chatbot Test Cases")
    print("=" * 50)
    
    for i, query in enumerate(test_cases, 1):
        print(f"Test {i}:")
        print(f"User: {query}")
        response = chatbot_response(query)
        print(f"CryptoBuddy: {response}")
        print("-" * 50)

def test_recommendation_algorithms():
    """Tests the recommendation algorithms with different strategies."""
    from chatbot_core import recommend_crypto
    
    print("Testing Recommendation Algorithms")
    print("=" * 40)
    
    strategies = ["profitability", "sustainability", "balanced"]
    
    for strategy in strategies:
        print(f"Strategy: {strategy}")
        result = recommend_crypto(strategy)
        print(f"Result: {result}")
        print("-" * 30)

def run_all_tests():
    """Runs all test functions."""
    print("🧪 Starting Comprehensive Testing Suite")
    print("=" * 60)
    
    # Test data validation
    from data_validator import validate_crypto_data
    print("Testing Data Validation:")
    validate_crypto_data()
    print()
    
    # Test recommendation algorithms
    test_recommendation_algorithms()
    print()
    
    # Test chatbot responses
    test_chatbot()
    
    print("✅ All tests completed!")

if __name__ == "__main__":
    run_all_tests()
