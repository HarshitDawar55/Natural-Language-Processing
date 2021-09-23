from flask import Flask, render_template, request
import numpy as np
from pickle import load

# Flask App Name
app = Flask("Linear Regression Basic App")

@app.route("/")
def home():
    return render_template("Form.html")

@app.route("/LRP", methods=["POST"])
def main():
    gaj = int(request.form.get("Area"))


    # Loading the Saved Model
    model = load(open("LR.pkl", "rb"))

    print(str(model.predict([[gaj]])))
    return str(model.predict([[gaj]])[0])


app.run(host = "0.0.0.0", port=80)
