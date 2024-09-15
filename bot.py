import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# OpenAI API Key
openai.api_key = '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'

# Telegram Bot Token
telegram_bot_token = '7308665138:AAH4BjAi5i9zOejRguMUkgSeHV4G3wwHeZQ'

# Function to get response from GPT-4O
def get_openai_response(prompt):
    try:
        response = openai.Completion.create(
            engine="gpt-4",  # GPT-4O ka model specify karein
            prompt=prompt,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Function to handle messages from Telegram
def handle_message(update, context):
    user_message = update.message.text
    ai_response = get_openai_response(user_message)
    update.message.reply_text(ai_response)

# Set up the Telegram bot
def main():
    updater = Updater(telegram_bot_token, use_context=True)
    dp = updater.dispatcher

    # Handle text messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
