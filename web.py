import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def get():
    return "POST your HTML to this URL to convert it to text using Aaron Swartz's great html2text.py package!"

@app.route("/", methods=['POST'])
def post():
    return "Thank you for trying! Here's your data: '%s'\n" % request.data

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
