# ==================================================
# BASIC CHATBOT
# A simple rule-based chatbot using only built-in Python
# ==================================================

# --------------------------------------------------
# 1. Welcome message
# --------------------------------------------------
print("====================================")
print("        BASIC CHATBOT")
print("====================================")
print()
print("Bot: Hello! I am a simple rule-based chatbot.")
print('Bot: Type "help" to see what I can understand.')
print('Bot: Type "bye" to exit the chatbot.')
print()
print("====================================")
print()


# --------------------------------------------------
# 2. Function that decides the chatbot's reply
# --------------------------------------------------
def chatbot_response(user_input):
    # Compare the user's message with each predefined rule
    if user_input == "hello":
        return "Hi! How can I help you?"

    elif user_input == "hi":
        return "Hello! Nice to meet you."

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "what is your name":
        return "I'm a simple Python chatbot."

    elif user_input == "who are you":
        return "I'm a rule-based chatbot created using Python."

    elif user_input == "help":
        return ("I understand these commands:\n"
                "- hello\n"
                "- hi\n"
                "- how are you\n"
                "- what is your name\n"
                "- who are you\n"
                "- thanks\n"
                "- thank you\n"
                "- help\n"
                "- bye")

    elif user_input == "thanks":
        return "You're welcome!"

    elif user_input == "thank you":
        return "You're welcome!"

    elif user_input == "bye":
        return "Goodbye! Have a nice day!"

    else:
        # No rule matched, so this is an unknown message
        return 'Sorry, I don\'t understand that. Try typing "help" to see what I can understand.'


# --------------------------------------------------
# 3. Main chatbot loop
# --------------------------------------------------
while True:
    # Take input from the user
    # .lower() makes the input case-insensitive
    # .strip() removes extra spaces at the start and end
    user_input = input("You: ").lower().strip()

    # Check for empty input (user just pressed Enter)
    if user_input == "":
        print("Bot: Please type something.")
        print()
        continue  # go back to the start of the loop

    # Get the reply from the function and show it
    response = chatbot_response(user_input)
    print("Bot:", response)
    print()

    # Stop the loop when the user says bye
    if user_input == "bye":
        break
