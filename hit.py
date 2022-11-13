import requests
import json
class hit:
    payload = { "nokontrak" : input("nokontrak:") }
    r = requests.post('http://127.0.0.1:8000/open-api/INFO-REKENING', json=payload)
    pretty_json = json.loads(r.text)
    hit = print(json.dumps(pretty_json, indent=4))