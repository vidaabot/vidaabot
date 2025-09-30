import telebot

TOKEN = "TEU_TOKEN_AQUI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Olá! Eu sou o VidaaBot e já estou ativo!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Recebi tua mensagem: {message.text}")

bot.infinity_polling()
