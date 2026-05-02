from flask import Flask, request
from account import Account
 
app = Flask(__name__)
account = Account(pin=1234)
 
@app.route("/")
def home():
    return "Web ATM is Running"
 
@app.route("/withdraw", methods=["POST"])
def withdraw():
    amount = int(request.form["amount"])
    return account.withdraw(amount)
 
if __name__ == "__main__":
    app.run()
