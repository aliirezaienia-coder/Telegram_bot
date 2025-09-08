import os
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# توکن و لینک‌ها از Environment Variables خوانده می‌شوند
BOT_TOKEN   = os.getenv("8431573732:AAEsHunpa6yNlm6X91wFCjU62OhEUdV2WV0")      # توکن BotFather
VIDEO_URL   = os.getenv("BAACAgQAAxkBAAECvbNovrp9e1qbWeMmSeQtSH2q5veT-gACaxwAAq1d-VFGUL8J4e6v3TYE")      # لینک mp4 یا file_id
WEBSITE_URL = os.getenv("https://t.me/Casinotel_bot/app")    # لینک سایت

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("📹 دریافت ویدیو آموزش", callback_data="show_video")],
        [InlineKeyboardButton("🌐 لینک سایت", url=WEBSITE_URL)]
    ]
    update.message.reply_text(
        """🎉 خوش اومدی 🎉

✅ خبر خوب اینکه نیاز به ثبت نام نداری،
کافیه روی لینک بزنی و خودت به صورت خودکار ثبت نام می‌شی ✨

از همین لحظه می‌تونی استفاده کنی و لذت ببری 🎊""",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def on_button(update, context):
    q = update.callback_query
    q.answer()
    if q.data == "show_video":
        chat_id = q.message.chat_id
        context.bot.send_video(chat_id=chat_id, video=VIDEO_URL, caption="این هم ویدیو آموزشی 🎥")

def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN تنظیم نشده است")
    if not WEBSITE_URL:
        raise ValueError("WEBSITE_URL تنظیم نشده است")
    if not VIDEO_URL:
        raise ValueError("VIDEO_URL تنظیم نشده است (mp4 یا file_id بده)")

    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(on_button))
    updater.start_polling(drop_pending_updates=True, timeout=20, read_latency=5)
    updater.idle()

if name == "main":
    main()
