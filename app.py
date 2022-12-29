from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

stories=[
    {
        "inputs":6,
        "category":"sports",
        "word":"chess"
    },
    {
        "inputs":6,
        "category":"European Country Name",
        "word":"france"
    },
]
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-template")
def get_template():
    return jsonify({
        "status":"success",
        "word":random.choice(templates)
    })
