from flask import Flask, render_template, request, jsonify
from clips import Environment
import os
import json

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)