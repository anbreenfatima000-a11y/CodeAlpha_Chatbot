import random
import datetime

greetings = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"]
how_are_you = ["how are you", "how do you do", "how's it going", "how's everything", "how's life"]
user_responses = ["i am good", "i'm good", "i am fine", "i'm fine", "fine", "good", "great"]
user_questions = ["what is your name?", "who are you?", "what can you do?", "what is your purpose?", "what is your function?", "name", "who are you", "what can you do", "what is your purpose", "what is your function", "what is your name"]
time_questions = ["what time is it?","time", "current time", "can you tell me the time?", "what's the current time?", "do you know the time?"]
date_questions = ["what is the date today?", "date", "current date", "can you tell me the date?", "what's today's date?", "do you know the date?"]
thanks = ["thanks", "thank you", "thanks a lot", "thank you so much"]
goodbyes = ["goodbye", "see you later", "bye", "farewell"]

greetings_replies = [
    "Hi! How can I help you?",
    "Hello! What can I do for you today?",
    "Hey there! How can I assist you?",
    "Greetings! How may I help you?",
    "Good to see you! What can I do for you?"
] 

how_are_you_replies = [
    "I'm doing well, thank you! How about you?",
    "I'm great! How are you doing?",
    "I'm fine, thanks for asking! How about yourself?",
    "I'm good! How's your day going?",
    "I'm doing well! How can I assist you today?"
]   

thanks_replies = [ 
    "You're welcome!",
    "Anytime!",
    "Glad I could help!",
    "You're very welcome!",
    "Happy to help!"
]

help_message = "Here are some things you can ask me:- \n -Hello/Hi \n -How are you? \n -What is your name? \n -What can you do? \n -What time is it? \n -What is the date today? \n -Goodbye"

def handle_greetings(user_input):
    if user_input in greetings:
        print("Chatbot: " + random.choice(greetings_replies))
        return True
    return False

def handle_how_are_you(user_input):
    if user_input in how_are_you:
        print("Chatbot: " + random.choice(how_are_you_replies))
        return True
    return False

def handle_time_questions(user_input):
    if user_input in time_questions:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Chatbot: The current time is {current_time}.")
        return True
    return False

def handle_date_questions(user_input):
    if user_input in date_questions:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        print(f"Chatbot: Today's date is {current_date}.")
        return True
    return False

def handle_user_responses(user_input):
    if user_input in user_responses:
        print("Chatbot: That's great to hear!")
        return True
    return False

def handle_user_questions(user_input):
    if user_input in user_questions:
        print("Chatbot: I'm PyBot! Your simple Python chatbot. I can respond to basic greetings, answer simple questions, and have a small conversation with you.")
        return True
    return False

def handle_thanks(user_input):
    if user_input in thanks:
        print("Chatbot: " + random.choice(thanks_replies))
        return True
    return False

def handle_goodbyes(user_input):
    if user_input in goodbyes:
        print("Chatbot: Goodbye! Have a great day!")
        return True
    return False

def handle_help(user_input):
    if user_input in ["help"]:
        print("Chatbot: " + help_message)
        return True
    return False

def handle_unknown():
    print("Chatbot: I'm sorry, I didn't understand that. " + "Can you please rephrase?")

mapping = {
    "greetings": (greetings, handle_greetings),
    "how_are_you": (how_are_you, handle_how_are_you),
    "user_responses": (user_responses, handle_user_responses),
    "user_questions": (user_questions, handle_user_questions),
    "time_questions": (time_questions, handle_time_questions),
    "date_questions": (date_questions, handle_date_questions),
    "thanks": (thanks, handle_thanks),
    "goodbyes": (goodbyes, handle_goodbyes),
    "help": (["help"], handle_help)
}


def chatbot():
    print("Hello! I'm your chatbot. How can I assist you today?")

    while True:
        user_input = input("You: ").lower().strip()

        matched = False
        exit_chat = False

        for category in mapping:
            keywords, handler = mapping[category]

            if user_input in keywords:
                handler(user_input)
                matched = True

                if category == "goodbyes":
                    exit_chat = True

                break

        if not matched:
            handle_unknown()

        if exit_chat:
            break

chatbot()