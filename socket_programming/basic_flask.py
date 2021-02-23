from flask import Flask, redirect, request

from hashlib import md5

app = Flask("url_shortener")

mapping = {}

@app.route("/shorten", methods=["POST"])
def shorten():
    global mapping
    payload = request.json

    if "url" not in payload:
        return "Missing URL Parameter", 400

    # TODO: check if URL is valid

    hash_ = md5()
    hash_.update(payload["url"].encode())
    digest = hash_.hexdigest()[:5]  # limiting to 5 chars. Less the limit more the chances of collission

    if digest not in mapping:
        mapping[digest] = payload["url"]
        return f"Shortened: r/{digest}\n"
    else:
        # TODO: check for hash collission
        return f"Already exists: r/{digest}\n"


@app.route("/r/<hash_>")
def redirect_(hash_):
    if hash_ not in mapping:
        return "URL Not Found", 404
    return redirect(mapping[hash_])


if __name__ == "__main__":
    app.run(debug=True)

"""
OUTPUT:


===> SHORTENING

$ curl localhost:5000/shorten -H "content-type: application/json" --data '{"url":"https://linkedin.com"}'
Shortened: r/a62a4


===> REDIRECTING, notice the response code 302 and the location header

$ curl localhost:5000/r/a62a4 -v
* Uses proxy env variable NO_PROXY == '127.0.0.1'
*   Trying ::1...
* TCP_NODELAY set
* Connection failed
* connect to ::1 port 5000 failed: Connection refused
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 5000 (#0)
> GET /r/a62a4 HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.64.1
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 302 FOUND
< Content-Type: text/html; charset=utf-8
< Content-Length: 247
< Location: https://linkedin.com
< Server: Werkzeug/0.15.4 Python/3.7.7
< Date: Tue, 27 Oct 2020 09:37:12 GMT
<
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
* Closing connection 0
<p>You should be redirected automatically to target URL: <a href="https://linkedin.com">https://linkedin.com</a>.  If not click the link.
"""
