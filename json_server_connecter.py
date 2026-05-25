import requests
import time
import webbrowser

RAW_URL = "https://raw.githubusercontent.com/N1oGey/Json-servers/refs/heads/main/link_opener.json"

def get_data():
    r = requests.get(RAW_URL, timeout=10)
    r.raise_for_status()
    return r.json()

def main():
    try:
        start_data = get_data()
        last_version = int(start_data.get("version", 0))
        print("Listener started. Current version:", last_version)
    except Exception as e:
        print("Startup ERROR:", e)
        return

    while True:
        try:
            data = get_data()
            version = int(data.get("version", 0))
            url = data.get("url", "").strip()

            if version > last_version and url:
                print("NEW URL:", url)
                webbrowser.open_new_tab(url)
                last_version = version

        except Exception as e:
            print("ERROR:", e)

        time.sleep(2)

if __name__ == "__main__":
    main()