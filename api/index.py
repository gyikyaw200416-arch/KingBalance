import telebot
import requests
from flask import Flask, request

app = Flask(__name__)
BOT_TOKEN = '8871290779:AAEBWy17HHbYpMuc9D-ZKI7h8x2R5Ky5Cws'
ADMIN_BOT_TOKEN = '8621994173:AAF8RmT72IVpLp5VBJH3_MLWfXa6ynXi1ks'
bot = telebot.TeleBot(BOT_TOKEN)
admin_bot = telebot.TeleBot(ADMIN_BOT_TOKEN)

# When someone requests a withdrawal
def send_withdrawal_to_admin(user_id, username, amount):
    # Replace with your actual Telegram User ID to receive the alert
    MY_ADMIN_ID = "YOUR_TELEGRAM_ID" 
    alert = f"🚨 NEW WITHDRAWAL REQUEST\n👤 User: {username}\n🆔 ID: {user_id}\n💰 Amount: {amount} 💸"
    admin_bot.send_message(MY_ADMIN_ID, alert)

# Game Logic (Simplified)
@bot.message_handler(commands=['spin'])
def spin(message):
    # Logic: Random choice for 🍇, 🍋, 7️⃣, 🍫
    # If match, update Supabase balance
    # Update logic here...
    bot.reply_to(message, "🎰 Spinning... [Result]")

# Webhook route
@app.route('/api', methods=['POST'])
def webhook():
    # Standard webhook processing
    return 'OK', 200
