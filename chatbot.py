def chatbot():
    responses = {
        "hello": "Hi there! How can I help you?",
        "hi": "Hello! What brings you here?",
        "how are you": "I'm doing well, thank you! How about you?",
        "fine": "Glad to hear that!",
        "not good": "I'm sorry to hear that. Is there anything I can do to help?",
        "goodbye": "Goodbye! Have a great day!",
        "bye": "Goodbye! Take care!",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "thank you": "You're welcome!",
        "how's the weather": "I'm not sure, but you can check the weather forecast online!",
        "who are you": "I'm a chatbot designed to assist you with information. How can I help?",
        "default": "I'm not sure how to respond to that. Can you ask something else?"
    }

    print("Hello! I'm a simple chatbot. What's your name?")
    user_name = input("Enter your name: ")
    print(f"Nice to meet you, {user_name}!")

    while True:
        user_input = input("How can I help you today? (Type 'bye' to exit): ").lower()

        if user_input in responses:
            print(responses[user_input])
            if user_input in ['goodbye', 'bye']:
                break
        else:
            print(responses["default"])

chatbot()
