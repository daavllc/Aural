import json

def Serialize(path: str, settings: dict):
     with open (path, "w", encoding="utf-8") as f:
        f.write(json.dumps(settings, indent=4))

def Deserialize(path: str):
    settings = dict()
    with open(path, "r", encoding="utf-8") as f:
        settings = json.load(f)
    return settings