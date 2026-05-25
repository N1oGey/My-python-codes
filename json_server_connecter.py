import requests
import time
import webbrowser

RAW_URL = "https://raw.githubusercontent.com/N1oGey/Json-servers/refs/heads/main/link_opener.json"

last_version = -1

while True:
    try:
        r = requests.get(RAW_URL, timeout=10)
        r.raise_for_status()

        data = r.json()

        url = data.get("url", "")
        version = int(data.get("version", 0))

        if url and version != last_version:
            print("OPEN:", url)
            webbrowser.open(url)
            last_version = version

    except Exception as e:
        print("ERROR:", e)

    time.sleep(3)