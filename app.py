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
        cardNumber = list(request.form.get("cardNumber"))
        #converts string to int
        list_of_cardNumber = list(map(int, cardNumber))
        #Start at the right most position (assume that is position 0)
        #For every second position (every odd index position) (change increment)
        temp = []
        for number in reversed(list_of_cardNumber):
            #multiply position i by 2
            if (number % 2) != 0:
                temp.append(cardNumber[number])
            else: 
                doubledValue = cardNumber[number] * 2
                # add the first and second digit together
                if doubledValue > 9:
                    luhnValue = list(doubledValue)
                    temp.append(luhnValue[0] + luhnValue[1])
        #Add all the numbers together
        luhnSum = 0
        for numbers in temp:
            luhnSum += temp[numbers]
        if (luhnSum % 10) == 0:
            return render_template("valid.html") 
        return render_template("invalid.html")