import json

with open("./settings/config.json", "r") as f:
    config: dict = json.loads(f.read())