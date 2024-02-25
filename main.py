
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import MessageHandler, ContextTypes, filters, CommandHandler, Application, CallbackContext
from fastapi import FastAPI


app = FastAPI()
TOKEN = "7146202590:AAEyU2YFUlbEHVaXqVsTCp_8b7k6t_EECuk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("/start")
    reply_keyboard=[["Red", "Green", "Blue"]]
    await update.message.reply_text("pick a color", reply_markup=ReplyKeyboardMarkup(reply_keyboard))

async def get_color(update: Update, context: ContextTypes.DEFAULT_TYPE):
    color = update.message.text
    with open("color.txt", "w") as file:
        file.write(color)
    print(color)
    return color
@app.get("/get-color")
async def color() -> str:
    with open("color.txt", "r") as file:
        color = file.read()
        return color
def main():
    print("Starting...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Regex("^(Red|Green|Blue)$"),get_color))
    print("Polling")
    app.run_polling(poll_interval=2)
if __name__ == "__main__":
    main()

