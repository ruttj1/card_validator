from crypt import methods
from lib2to3.pgen2.token import EQUAL
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    #TODO
        #Get card number from form as string
        #store card number as an array of strings
        cardNumber = request.form.get("cardNumber")
        #converts string to int
        list_of_cardNumber = list(map(int, cardNumber))
        #Start at the right most position (assume that is position 0)
        #For every second position (every odd index position) (change increment)
        temp = []
        counter = 0
        for number in reversed(list_of_cardNumber):
            if counter % 2 == 0:
                temp.append(number)
                counter += 1
            else:
                counter += 1
                number = number * 2
                if number > 9:
                    luhnList = list(map(int, str(number)))
                    temp.append(sum(luhnList)) 
                else:
                    temp.append(number)
        luhnCard = sum(temp)
        if luhnCard % 10 == 0:
            return render_template("valid.html")
        else: 
            return render_template("invalid.html")