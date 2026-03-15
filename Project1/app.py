from flask import Flask, render_template, request
import random

app = Flask(__name__)

def check_winner(user, computer):
    if user == computer:
        return "It's a Draw!"
    elif (user == "snake" and computer == "water") or \
         (user == "water" and computer == "gun") or \
         (user == "gun" and computer == "snake"):
        return "You Win! 🎉"
    else:
        return "Computer Wins! 💻"

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    computer_choice = ""

    if request.method == "POST":
        user_choice = request.form["choice"]
        computer_choice = random.choice(["snake", "water", "gun"])
        result = check_winner(user_choice, computer_choice)

    return render_template("index.html", result=result, computer_choice=computer_choice)

if __name__ == "__main__":
    app.run(debug=True)
