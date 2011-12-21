import os, urllib
from feedparser import _getCharacterEncoding
import chardet
import html2text
from flask import Flask, request, make_response

# html2text.BODY_WIDTH = 140

app = Flask(__name__)
app.config['DEBUG'] = True

def text_response(output):
    response = make_response(output, 200)
    response.mimetype = 'text/plain'
    return response

@app.route("/")
def get():
    url = request.args.get('url')
    if not url:
        return """
<!doctype html>
<html>
  <head>
    <title>html2text</title>
  </head>
  <body>
    <p>This a RESTful web service that converts HTML to
      <a href="http://daringfireball.net/projects/markdown/">Markdown</a>-compatible text using
      <a href="http://www.aaronsw.com/">Aaron Swartz</a>'s <a href="http://www.aaronsw.com/2002/html2text/">html2text.py</a>.</p>
    </p>
    <form action="/" method="get">
      <p>URL: <input type="text" name="url" /> <button type="submit">Go</button></p>
    </form>
      
    <form action="/" method="post">
      <p>Or just paste in some HTML:</p>
      <textarea name="html" rows="20" cols="80"></textarea>
      <p><button type="submit">Go</button>
    </form>
    
    <address><a href="https://github.com/aaronsw/html2text-service/">Get the source code.</a></address>
  </body>
</html>
"""
    else:
        req = urllib.urlopen(url)
        text = req.read()
        encoding = _getCharacterEncoding(req.headers, text)[0]
        if encoding == 'us-ascii': encoding = 'utf-8'
        try:
            text = text.decode(encoding)
        except UnicodeDecodeError:
            text = text.decode(chardet.detect(text)['encoding'])
        output = html2text.html2text(text, url)
        return text_response(output)

@app.route("/", methods=['POST'])
def post():
    output = html2text.html2text(request.form['html'])
    return text_response(output)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
