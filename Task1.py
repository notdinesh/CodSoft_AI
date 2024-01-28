def simple_chatbot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    elif "how are you" in user_input:
        return "I'm just a computer program, but thanks for asking!"

    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day."

    elif "your name" in user_input:
        return "I'm a simple chatbot."

    elif "weather" in user_input:
        return "I'm sorry, I don't have information about the weather."

    else:
        return "I'm not sure how to respond to that. Can you ask something else?"

def main():
    print("Welcome to the Simple Chatbot!")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        response = simple_chatbot(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
