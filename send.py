import json
import os

import requests
from dotenv import load_dotenv


def main():
    load_dotenv(override=True)
    url = os.getenv("WEB_HOOKS_URL")

    data = json.dumps({"text": "text"})
    resp = requests.post(url=url, data=data)
    print(resp.json)


if __name__ == "__main__":
    main()
