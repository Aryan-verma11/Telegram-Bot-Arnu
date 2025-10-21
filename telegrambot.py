import telebot
import re
Token="Api key"

bot=telebot.TeleBot(Token)

@bot.message_handler(commands=['Start','Hii','Hello','hi','namasty','bonjour',]) #you can also add msg send by user (['start',/start])
def start(message):
    bot.reply_to(message,"Welcome Welcome I Am a bot named arnu")

@bot.message_handler(command=['help'])
def start(message):
    bot.reply_to(message,"""/start->Greeting
                 /help-> Will give you all commands list




""")


@bot.message_handler(func=lambda message: True)
def calc(message):
    try:
        if re.match(r'^[0-9\+\-\*/\.\(\)\s]+$', message.text):
            msg = eval(message.text)
        else:
            msg = "Please enter a valid math expression!"
    except Exception:
        msg = "This can’t be evaluated!"
    bot.reply_to(message, str(msg))


print("Bot is running...")

bot.polling()