import os
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from answer import openai_create

# Load your Telegram bot token from environment variable
key = os.environ['TOKEN']
print("🤖 Bot has Started...")

# Command: /start
def start_command(update, context):
    update.message.reply_text(
        "👶 Hello! I am your Baby Care Bot!\n"
        "You can ask me anything about pregnancy, baby care, or parenting tips.\n\n"
        "📌 Commands:\n"
        "/start - Start the bot\n"
        "/help - Help info\n"
        "/question - Ask a question"
    )

# Command: /help
def help_command(update, context):
    update.message.reply_text(
        "📖 Help Menu:\n"
        "/start - Start the bot\n"
        "/help - Show this help menu\n"
        "/question - Ask a baby care question"
    )

# Command: /question
def question_command(update, context):
    update.message.reply_text("🍼 Please type your baby care question!")

# Handle user messages
def handle_message(update, context):
    user_text = str(update.message.text).lower()
    response = openai_create(user_text)
    update.message.reply_text(response)

# Bot Setup
updater = Updater(key, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start_command))
dp.add_handler(CommandHandler("help", help_command))
dp.add_handler(CommandHandler("question", question_command))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

updater.start_polling()
updater.idle()

  update.message.reply_text(response)


def error(update, context):
  print(f"Update {update} caused error {context.error}")


def main():
  updater = Updater(key, use_context=True)
  dp = updater.dispatcher

  dp.add_handler(CommandHandler("start", start_command))

  dp.add_handler(CommandHandler("help", help_command))

  dp.add_handler(CommandHandler("question", question_command))

  dp.add_handler(MessageHandler(Filters.text, handle_message))

  dp.add_error_handler(error)

  updater.start_polling()
  updater.idle()


main()