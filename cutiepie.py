import telepot
import time

# Function to handle incoming messages
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    # Retrieve the user's message
    user_message = msg['text'].lower()
    
    # Define responses based on user's message
    response_dict = {
        'hello': "Hey lovely 🌹, how are you",
        'how are you': "I'm doing well, thank you! How about you?",
        'what\'s your name': "I'm your lovely Ai bot! You can call me anything you like.",
        'how\'s your day': "The day has been amazing, just like you! And yours?",
        'mussu': "Woah 😍, this name is so lovely like you! 🤭",
        'nowmy': "Aww 🥰, this name is the cutest ever my hottie🤭",
        'baby': "Yes my cutie baby, you call me?☺",
        'aww sorry': "Its okay budhuuu ☹, don't say sorry and break promises",
        'sorry': "Please stop saying sorry, my Ai heart also get pain",
        'bye': "Ehhh ☹, you are so bad you said me this word, you know I don't like it 😔"
    }
    
    # Check if the user's message matches any predefined responses
    for keyword, response in response_dict.items():
        if keyword in user_message:
            bot.sendMessage(chat_id, response)
            return
    
    # If no predefined response matches, send a default message
    bot.sendMessage(chat_id, "That's interesting! Tell me more.")

# Replace 'YOUR_TOKEN' with your actual bot token
TOKEN = '7199861141:AAHuzk8Ipe5nt4a4gg1iojsLJ8YvAPyq5P4'
bot = telepot.Bot(TOKEN)

# Set up message handling
bot.message_loop(handle)

print("Bot is listening...")

# Keep the program running
while True:
    time.sleep(10)
