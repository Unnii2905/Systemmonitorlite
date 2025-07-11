from collector import collect_all
from rules import analyze_data
from utils import save_alerts
def main():
    print("[*0]Collecting system datas...")
    data = collect_all()

    print("[*] Analyzing for suspicious activity...")
    alerts = analyze_data(data)

    if alerts:
        print("\n Alerts:")
        for alert in alerts:
            print(f" - {alert['type'].upper()} ALERT: {alert['message']}")
        save_alerts(alerts)
        print("\n Alerts saved to alerts.json")
    else:
        print(" No suspicious activity detected.")

if __name__ == "__main__":
    main()
