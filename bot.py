from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "YAHAN_APNA_NAYA_BOT_TOKEN_DALNA"

WELCOME = """
👋 Welcome

👋 एडमिन सर्वर में आपका स्वागत है

📢 ऑफिशियल चैनल से जुड़ें 💝🙏🏻
https://t.me/KavyaisLiveBgmi
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📋 MENU", callback_data="menu")],
        [InlineKeyboardButton("💬 SUPPORT", url="https://t.me/Kavya_is_Live")]
    ]

    await update.message.reply_text(
        WELCOME,
        reply_markup=InlineKeyboardMarkup(keyboard),
        disable_web_page_preview=True
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "menu":
        keyboard = [
            [InlineKeyboardButton("🔒 MARS_LOADER_KEY 🔑", callback_data="mars")],
            [InlineKeyboardButton("🔒 ZTRAX_LOADER_KEY 🔑", callback_data="ztrax")],
            [InlineKeyboardButton("🔒 FIRE.X_LOADER_KEY 🔑", callback_data="firex")]
        ]

        await query.edit_message_text(
            "👇 अपना Loader चुनें",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

app.run_polling()
