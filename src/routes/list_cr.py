import json
import random
from flask import Flask, jsonify

with open("static/flags_dataset/countries.json", "r", encoding="utf-8") as f:
    countries = json.load(f)

n = len(countries)

random_pos = random.