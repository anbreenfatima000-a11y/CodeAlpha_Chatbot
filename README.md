# CodeAlpha Chatbot

A simple **rule-based chatbot developed in Python** as part of my **CodeAlpha Internship**.

The chatbot is designed to handle basic conversations with the user, including greetings, common questions, date and time requests, thank-you messages, and goodbyes. It uses predefined responses and simple keyword matching to keep the interaction straightforward and beginner-friendly.

## Features

* Responds to common greetings such as "Hello" and "Hi".
* Handles basic "How are you?" conversations.
* Answers simple questions about its name and purpose.
* Displays the current time.
* Displays the current date.
* Responds to thank-you messages.
* Provides a help option with supported commands.
* Handles goodbye messages and exits the conversation.
* Gives a friendly response when it does not understand the input.
* Uses random responses for some conversation types to make interactions less repetitive.

## Technologies Used

* **Python 3**
* `random` module
* `datetime` module
* Functions
* Lists
* Dictionaries
* Loops
* Conditional statements
* Basic input handling

## How to Run

1. Make sure Python 3 is installed on your system.
2. Clone this repository:

```bash
git clone https://github.com/your-username/CodeAlpha_Chatbot.git
```

3. Open the project folder:

```bash
cd CodeAlpha_Chatbot
```

4. Run the chatbot:

```bash
python chatbot.py
```

## How to Use

After running the program, the chatbot will greet you and wait for your input.

You can try messages such as:

```text
Hello
How are you?
What is your name?
What can you do?
What time is it?
What is the date today?
Thanks
Help
Goodbye
```

The chatbot matches the entered message with predefined categories and provides an appropriate response. The current implementation uses exact input matching rather than natural language processing.

## Example

```text
Hello! I'm your chatbot. How can I assist you today?

You: hello
Chatbot: Hello! What can I do for you today?

You: what is your name?
Chatbot: I'm PyBot! Your simple Python chatbot.

You: what time is it?
Chatbot: The current time is 17:30:25.

You: goodbye
Chatbot: Goodbye! Have a great day!
```

## Project Structure

```text
CodeAlpha_Chatbot/
│
├── chatbot.py
└── README.md
```

## How It Works

The chatbot organizes possible user inputs into different categories such as greetings, user questions, time and date questions, thanks, and goodbyes.

Each category is connected to a separate handler function. When the user enters a message, the program checks the available categories and calls the corresponding handler when a match is found.

The project also uses Python's `datetime` module to provide the current date and time and the `random` module to select different responses for some interactions.

## Internship Task

This project was completed as part of the **CodeAlpha Python Programming Internship**.

Through this project, I practiced:

* Python functions
* Lists and dictionaries
* Loops
* Conditional statements
* User input handling
* Keyword matching
* Random responses
* Date and time handling
* Basic program structure

## Author

**Anbreen Fatima**

BS Information Technology Student
Python Programming Intern — CodeAlpha

