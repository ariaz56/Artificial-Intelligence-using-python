print("Simple Rule-Based Chatbot")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How can I help you?")

    elif "how are you" in user:
        print("Bot: I am fine. Thank you!")

    elif "your name" in user:
        print("Bot: My name is SimpleBot.")

    elif "what can you do" in user:
        print("Bot: I can answer simple questions.")

    elif "thank" in user:
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")