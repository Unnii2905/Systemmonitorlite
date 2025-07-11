def analyze_data(data):
    alerts = []

    for p in data['processes']:
        if 'powershell' in str(p['cmdline']).lower() and 'winword' in str(p['cmdline']).lower():
            alerts.append({
                'type': 'process',
                'message': f"Suspicious powershell spawned by Word: {p['cmdline']}"
            })

    keywords = ['ncat', 'netcat', 'wget', 'curl', 'bash', 'sh']
    for line in data['crontab']:
        for kw in keywords:
            if kw in line:
                alerts.append({
                    'type': 'crontab',
                    'message': f"Suspicious crontab entry: {line}"
                })

    for conn in data['network']:
        if conn['raddr'] == '' and conn['pid']:
            suspicious_ports = ['4444', '1337', '8080']
            for port in suspicious_ports:
                if port in conn['laddr']:
                    alerts.append({
                        'type': 'network',
                        'message': f"Port {port} bound by PID {conn['pid']}"
                    })

    for f in data['systemd']:
        if 'reverse' in f or 'backdoor' in f:
            alerts.append({
                'type': 'systemd',
                'message': f"Suspicious service name: {f}"
            })

    return alerts
