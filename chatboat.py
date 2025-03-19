# import cohere  

# # Replace with your actual Cohere API key
# api_key = "q8l1oSgrBfQBINy0DU7O26jccaQYcgzVlAK7VWl9"

# # Initialize Cohere client
# co = cohere.Client(api_key)

# def chat_with_cohere(prompt):
#     try:
#         response = co.generate(
#             model="command",  # Use "command" or "command-nightly"
#             prompt=prompt,
#             max_tokens=200
#         )
#         return response.generations[0].text.strip()
#     except Exception as e:
#         return f"Error: {str(e)}"

# print("Chatbot: Hello! Type 'exit' to end the chat.")

# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "exit":
#         print("Chatbot: Goodbye! 👋")
#         break
#     else:
#         response = chat_with_cohere(user_input)
#         print("Chatbot:", response)


###########################################################
import cohere  # Import Cohere library

# Your Cohere API key (⚠️ Do not share this publicly)
api_key = "q8l1oSgrBfQBINy0DU7O26jccaQYcgzVlAK7VWl9"

# Initialize Cohere client
co = cohere.Client(api_key)

def chat_with_cohere(prompt):
    """
    Sends user input to Cohere's API and returns a chatbot response.
    Includes error handling to prevent crashes.
    """
    try:
        response = co.generate(
            model="command",  # Use "command" or "command-nightly"
            prompt=prompt,  # User's message
            max_tokens=200,  # Limits response length
            temperature=0.7  # Adjusts randomness (higher = more creative)
        )

        # Check if a valid response exists
        if response.generations and response.generations[0].text:
            return response.generations[0].text.strip()
        else:
            return "Sorry, I couldn't generate a response. Try again!"
    
    except Exception as e:
        return f"Error: {str(e)}"  # Handle API errors

# Start chatbot interaction
print("Chatbot: Hello! Type 'exit' to end the chat.")

while True:
    user_input = input("You: ")  # Get user input
    
    # Check if the user wants to exit
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! 👋")
        break  # Exit the loop
    
    # Get response from Cohere AI
    response = chat_with_cohere(user_input)
    
    # Print chatbot's response
    print("Chatbot:", response)
