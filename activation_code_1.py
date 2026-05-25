from flask import Flask, request, jsonify
from urllib.parse import urlparse
import webbrowser

app = Flask(__name__)

ACTIVATION_CODE = "1234"

def is_valid_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)

@app.route("/open")
def open_link():
    code = request.args.get("code", "")
    url = request.args.get("url", "")

    if code != ACTIVATION_CODE:
        return jsonify(ok=False, error="DENIED"), 403

    if not is_valid_url(url):
        return jsonify(ok=False, error="BAD_URL"), 400

    opened = webbrowser.open_new_tab(url)
    return jsonify(ok=True, opened=opened), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)