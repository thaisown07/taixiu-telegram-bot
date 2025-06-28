import os
from flask import Flask, request, render_template
import telegram
import analyze

app = Flask(__name__)
TOKEN = os.getenv("BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form["results"]
    chat_id = request.form["chat_id"]
    prediction = analyze.predict(data)
    bot.send_message(chat_id=chat_id, text=prediction)
    return render_template("result.html", prediction=prediction)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    return "OK", 200

if __name__ == "__main__":
    app.run()
