import telebot
import re
import random

# === Replace with your own bot token ===
Token = "8030004533:AAHAPHOiNmt3Q26Cx37Xwv3VZ4_pnCVkIfc"
bot = telebot.TeleBot(Token)

# =====================
# COMMAND HANDLERS
# =====================

@bot.message_handler(commands=['start', 'hello', 'hi', 'namaste', 'bonjour'])
def start(message):
    bot.reply_to(message, f"✨ Hey {message.from_user.first_name}! Welcome to *Arnu*, your Beauty + Math Bot 💄🧮", parse_mode='Markdown')

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, """
🤖 *Here are my commands:*
/start - Greeting Message
/help - Show all commands
/beauty_tips - Get a random beauty tip 💋
/inspire - Get a motivational quote 🌟
/calc - Type a math expression to calculate 🔢
/about - Know more about me 👑
""", parse_mode='Markdown')

@bot.message_handler(commands=['about'])
def about(message):
    bot.reply_to(message, "👑 I'm *Arnu*, created by a Beauty Influencer 💅 who loves glam & logic! 💄✨\nI can chat, calculate, inspire, and make your day fabulous 💖", parse_mode='Markdown')

# =====================
# RANDOM BEAUTY TIPS
# =====================

beauty_tips = [
    "💧 Stay hydrated — beauty starts from within!",
    "🧴 Always remove your makeup before bed!",
    "🌸 Use sunscreen every day — your future self will thank you!",
    "🍯 DIY honey masks can help keep your skin glowing!",
    "💋 Blend your foundation with a beauty blender for a flawless finish!",
    "🌿 Green tea helps detoxify your skin and soul!"
]

@bot.message_handler(commands=['beauty_tips'])
def beauty(message):
    tip = random.choice(beauty_tips)
    bot.reply_to(message, tip)

# =====================
# MOTIVATIONAL QUOTES
# =====================

quotes = [
    "✨ Believe in yourself and you’ll be unstoppable!",
    "💪 You are beautiful, powerful, and capable!",
    "🌟 Keep shining, the world needs your light!",
    "💖 Makeup can enhance your face, but confidence enhances your soul!"
]

@bot.message_handler(commands=['inspire'])
def inspire(message):
    quote = random.choice(quotes)
    bot.reply_to(message, quote)

# =====================
# CALCULATOR FEATURE
# =====================

@bot.message_handler(func=lambda message: re.match(r'^[0-9\+\-\*/\.\(\)\s]+$', message.text))
def calc(message):
    try:
        result = eval(message.text)
        bot.reply_to(message, f"🧮 Result: {result}")
    except Exception:
        bot.reply_to(message, "⚠️ This can’t be evaluated! Please check your math expression.")

# =====================
# FALLBACK (GENERAL)
# =====================

@bot.message_handler(func=lambda message: True)
def fallback(message):
    responses = [
        "💬 Hmm… I didn’t get that! Try /help for commands.",
        "👑 Oops! I only do glam & math — try /beauty_tips or /calc.",
        "💖 You can always ask me for /inspire quotes or /beauty_tips!"
    ]
    bot.reply_to(message, random.choice(responses))

# =====================
print("🤖 Bot is running...")
bot.polling()
