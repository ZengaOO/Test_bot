import telebot 


TOKEN = "8721893046:AAG8FxS6cpuWhN8y44AK5d77pmriWDywgcs"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот. Напиши мне что-нибудь!")

#(Эхо)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    
    bot.reply_to(message, f"🤖 Вы написали: {message.text}")

print("🚀 Бот запущен...")
bot.polling()