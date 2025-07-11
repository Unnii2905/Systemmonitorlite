# SysmonLite: Endpoint Threat Visibility Tool

**SysmonLite** is a  threat detection tool for Linux systems. It collects process, network, crontab, and systemd activitythen analyzes the data for suspicious behaviors

##  Features

-  Process & command-line inspection
-  Network connection monitoring
-  Crontab entry analysis
-  Systemd service scan
---



##  How It Works

1. Collects telemetry using `psutil`, `platform`, and system commands
2. Runs that data through custom detection rules
3. Prints alerts to terminal or GUI
4. Saves output to `alerts.json`

---

## Sample Detection Rules

- Powershell spawned by MS Word (`winword.exe → powershell`)
- Reverse shell in crontab (`bash -i >& /dev/tcp/...`)
- Backdoor-named `.service` files
- Ports like `4444` or `1337` in use

---

## Requirements

- Python 3.8+
- Linux (Kali, Ubuntu, etc.)
- Tkinter (usually comes with Python)

USAGE:
CLI mode:python main.py<br/>

GUI mode:python gui.py<br/>

Educational Purpose Only<br/>
SysmonLite is built for learning, testing, and security awareness. It is not a full EDR or anti-virus system.

License<br/>
This project is licensed under the MIT License.
