import datetime

# Define some responses for keywords
responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What's on your mind?",
    "weather": "I'm not sure about the weather, but it's always a good day to code!",
    "time": f"The current time is {datetime.datetime.now().strftime('%H:%M')}.",
    "day": f"Today is {datetime.datetime.now().strftime('%A')}.",
    "python": "Python is a versatile programming language, great for web development, data science, and more.",
    "bye": "Bye! Have a great day!",
}

def greet_user():
    print("Hi!! I'm here to chat. I speak enaglish becasue my owner prectice this language; Type 'bye' to exit")



def get_response(user_input):
    for key in responses:
        if key in user_input.lower():
            return responses[key]
    return "I'm not sure how to respond to that"

def chat():
    greet_user()
    while True:
        user_input = input("you: ")
        if user_input.lower() == "bye":
            print(responses["bye"])
            break
        response = get_response(user_input)
        print("ChatBot: " + response)

if __name__ == "__main__":
    chat()