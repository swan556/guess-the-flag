import json
import random
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open("static/flags_dataset/countries.json", "r", encoding="utf-8") as f:
    countries = json.load(f)

n = len(countries)

@app.route("/random-flag")
def pickRandomFlag():
    random_pos = random.randint(0, n)
    return jsonify({
        "country_name": countries[random_pos]["\ufeffCountry"], 
        "country_code": countries[random_pos]["Country code"]
        })

if(__name__=="__main__"):
    app.run(debug=True)