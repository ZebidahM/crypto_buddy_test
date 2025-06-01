def validate_crypto_data():
    """Validates that all cryptocurrencies have necessary attributes with correct data types."""
    from chatbot_core import crypto_db
    
    required_keys = {"price_trend", "market_cap", "energy_use", "sustainability_score"}
    valid_trends = {"rising", "stable", "falling"}
    valid_caps = {"high", "medium", "low"}
    valid_energy = {"high", "medium", "low", "very low"}
    
    errors_found = False

    for crypto, data in crypto_db.items():
        if not required_keys.issubset(data.keys()):
            print(f"Error: {crypto} is missing required attributes.")
            errors_found = True
        elif data["price_trend"] not in valid_trends:
            print(f"Error: {crypto} has invalid price trend '{data['price_trend']}'")
            errors_found = True
        elif data["market_cap"] not in valid_caps:
            print(f"Error: {crypto} has invalid market cap '{data['market_cap']}'")
            errors_found = True
        elif data["energy_use"] not in valid_energy:
            print(f"Error: {crypto} has invalid energy use '{data['energy_use']}'")
            errors_found = True
        elif not (0 <= data["sustainability_score"] <= 1):  # Note: scores are 0-1 range
            print(f"Error: {crypto} has invalid sustainability score '{data['sustainability_score']}'")
            errors_found = True
    
    if not errors_found:
        print("✅ Data validation completed successfully - all crypto data is valid!")
    else:
        print("❌ Data validation found errors - please fix the issues above.")
    
    return not errors_found
