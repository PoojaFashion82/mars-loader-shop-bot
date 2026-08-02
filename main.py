from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8735279973:AAF4W2ody2wP5wuoO8RmB7mK1NfnyJi-gj8"

CHANNEL = "https://t.me/KavyaisLiveBgmi"
SUPPORT = "https://t.me/Kavya_is_Live"

UPI_LINK = (
    "upi://pay?pa=8949220131@yapl"
    "&pn=Kavya"
    "&cu=INR"
)

WELCOME = f"""
👋 Welcome

👋 एडमिन सर्वर में आपका स्वागत है

📢 ऑफिशियल चैनल से जुड़ें 💝🙏🏻
{CHANNEL}
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📋 Menu", callback_data="menu")],
        [InlineKeyboardButton("💬 Support", url=SUPPORT)],
    ]
    await update.message.reply_text(
        WELCOME,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "menu":
        keyboard = [
            [InlineKeyboardButton("🔒 MARS_LOADER_KEY 🔑", callback_data="mars")],
            [InlineKeyboardButton("🔒 ZTRAX_LOADER_KEY 🔑", callback_data="ztrax")],
            [InlineKeyboardButton("🔒 FIRE.X_LOADER_KEY 🔑", callback_data="firex")],
        ]
        await query.edit_message_text(
            "🔑 Select Loader",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data in ["mars", "ztrax", "firex"]:
        keyboard = [
            [InlineKeyboardButton("🕒 6 HOURS — ₹70", url=UPI_LINK + "&am=70")],
            [InlineKeyboardButton("🕐 1 DAY — ₹150", url=UPI_LINK + "&am=150")],
            [InlineKeyboardButton("📅 3 DAY — ₹299", url=UPI_LINK + "&am=299")],
            [InlineKeyboardButton("📅 7 DAY — ₹499", url=UPI_LINK + "&am=499")],
            [InlineKeyboardButton("📅 15 DAY — ₹699", url=UPI_LINK + "&am=699")],
            [InlineKeyboardButton("📅 30 DAY — ₹799", url=UPI_LINK + "&am=799")],
            [InlineKeyboardButton("💬 Support", url=SUPPORT)],
        ]

        await query.edit_message_text(
            "🔑 KEY PRICE\n\nChoose your plan:",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot Running...")
    app.run_polling()

if __name__ == "__main__":
    main()
