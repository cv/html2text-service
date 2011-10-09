import os
from html2text import html2text
from flask import Flask, request

html2text.options['ul_item_mark'] = '-'
html2text.BODY_WIDTH = 140

app = Flask(__name__)

@app.route("/")
def get():
    return "POST your HTML to this URL to convert it to text using Aaron Swartz's great html2text.py package!"

@app.route("/", methods=['POST'])
def post():
    return html2text(request.form['html'])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
