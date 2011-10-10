html2text-service
-----------------

This a RESTful web service that converts HTML to [Markdown][1]-like syntax using [Aaron Schwartz's][2] [html2text.py][3]. The code is
available [on GitHub][4].

Try it out and help us make it better!

[1]: http://daringfireball.net/projects/markdown/
[2]: http://www.aaronsw.com
[3]: https://github.com/aaronsw/html2text
[4]: http://github.com/cv/html2text-service

Running
-------

With `$` as your command prompt:

    $ python web.py
    ...
    $ curl --data-urlencode "html=<html><body><h1>Hello,</h1>World</body></html>" localhost:5000
    # Hello,

    World

License
-------

`html2text-service` is distributed under the terms of the [GPLv3][5].

[5]: http://www.gnu.org/licenses/gpl-3.0.html
