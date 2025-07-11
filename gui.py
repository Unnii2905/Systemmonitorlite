import tkinter as tk
from tkinter import scrolledtext, messagebox
from collector import collect_all
from rules import analyze_data
from utils import save_alerts

class SysmonLiteGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SysmonLite - Threat Detection")

        self.button = tk.Button(root, text="Start Scan", command=self.run_scan, font=("Segoe UI", 12), bg="green", fg="white")
        self.button.pack(pady=10)

        self.output = scrolledtext.ScrolledText(root, width=100, height=25, font=("Consolas", 10))
        self.output.pack(padx=10, pady=10)

    def run_scan(self):
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, "[*] Collecting system telemetry...\n")
        data = collect_all()

        self.output.insert(tk.END, "[*] Analyzing for suspicious activity...\n")
        alerts = analyze_data(data)

        if alerts:
            self.output.insert(tk.END, "\n🚨 Alerts:\n")
            for alert in alerts:
                self.output.insert(tk.END, f" - {alert['type'].upper()} ALERT: {alert['message']}\n")

            save_alerts(alerts)
            self.output.insert(tk.END, "\n✅ Alerts saved to alerts.json\n")
        else:
            self.output.insert(tk.END, "✅ No suspicious activity detected.\n")

        self.output.see(tk.END)
        messagebox.showinfo("Scan Complete", f"{len(alerts)} alert(s) found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SysmonLiteGUI(root)
    root.mainloop()
