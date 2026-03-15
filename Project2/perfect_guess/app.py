from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Generate a secret number when server starts
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 5

@app.route("/", methods=["GET", "POST"])
def home():
    global attempts, secret_number
    
    message = ""
    
    if request.method == "POST":
        guess = int(request.form["guess"])
        attempts += 1
        
        if guess > secret_number:
            message = "Too high!"
        elif guess < secret_number:
            message = "Too low!"
        else:
            message = f"🎉 Correct! You guessed it in {attempts} attempts."
        
        if attempts >= max_attempts and guess != secret_number:
            message = f"❌ Game Over! The number was {secret_number}"
    
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)