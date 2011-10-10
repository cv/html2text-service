import os
import html2text
from flask import Flask, request, make_response

html2text.BODY_WIDTH = 140

app = Flask(__name__)

@app.route("/")
def get():
    return """
<!doctype html>
<html>
  <head>
    <title>html2text</title>
  </head>
  <body>
    <p>This a RESTful web service that converts HTML to
      <a href="http://daringfireball.net/projects/markdown/">Markdown</a>-like syntax using
      <a href="http://www.aaronsw.com">Aaron Schwartz's</a> <a href="https://github.com/aaronsw/html2text">html2text.py</a>.
      The code is available <a href="http://github.com/cv/html2text-service">on GitHub</a>.
    </p>
    <p>
      Try it out!
    </p>
    <form action="/" method="post">
      <input type="submit"/>
      <br/>
      <textarea name="html" rows="40" cols="80"></textarea>
    </form>
  </body>
</html>
"""

@app.route("/", methods=['POST'])
def post():
    response = make_response(html2text.html2text(request.form['html']), 200)
    response.mimetype = 'text/plain'
    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
