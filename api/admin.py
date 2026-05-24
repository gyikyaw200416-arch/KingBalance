import telebot
# This script is meant to be run via: python admin.py
bot = telebot.TeleBot('8621994173:AAF8RmT72IVpLp5VBJH3_MLWfXa6ynXi1ks')

@bot.message_handler(commands=['add'])
def add_balance(message):
    # Logic to parse user_id and amount, then PATCH to Supabase
    bot.reply_to(message, "✅ Balance updated in database.")

@bot.message_handler(commands=['cut'])
def cut_balance(message):
    # Logic to parse user_id and amount, then PATCH to Supabase
    bot.reply_to(message, "📉 Balance deducted.")

bot.infinity_polling()
