from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = '6675490107:AAGqekKFOOVj-qQcuJXfmH_5NVuoxxrUgCw'


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! Use /start to get the Amharic Books",
        reply_markup=ForceReply(selective=True),
    )


async def books_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Use /start to get recent books")


def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("books", books_command))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
