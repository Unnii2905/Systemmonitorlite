import json

def save_alerts(alerts):
    with open("alerts.json", "w") as f:
        json.dump(alerts, f, indent=2)
