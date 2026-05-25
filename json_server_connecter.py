import requests
import time
import webbrowser

RAW_URL = "https://github.com/N1oGey/Json-servers/blob/main/link_opener.json"

last_version = -1

while True:
    try:
        r = requests.get(RAW_URL, timeout=5)
        data = r.json()

        version = data.get("version", 0)
        url = data.get("url")

        if version != last_version and url:
            print("OPEN:", url)
            webbrowser.open(url)
            last_version = version

    except Exception as e:
        print("error:", e)

    time.sleep(3)