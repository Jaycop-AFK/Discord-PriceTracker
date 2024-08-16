from random import choice, randint

def get_response(user_input: str) -> str:
    if not isinstance(user_input, str):
        return "Invalid input. Please send a valid message."

    lowered: str = user_input.lower().strip()  # Ensure any surrounding whitespace is removed

    if lowered == '':
        return "Well, you're awfully silent..."
    elif 'hello' in lowered:
        return "Hello there!"
    elif 'how are you' in lowered:
        return "I'm doing great, thank you!"
    elif 'what is your name' in lowered:
        return "My name is "
    elif 'what time is it' in lowered:
        hour = randint(0, 23)
        minute = randint(0, 59)
        return f"The current time is {hour:02d}:{minute:02d}"
    elif 'what is the weather like' in lowered:
        weather_options = ["sunny", "cloudy", "rainy", "snowy"]
        return f"The weather is {choice(weather_options)}."
    elif 'bye' in lowered:
        return "Goodbye!"
    else:
        return "I'm sorry, I couldn't understand that. Please try again."
