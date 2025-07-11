import psutil
import os
import platform
import subprocess

def get_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'ppid', 'name', 'cmdline']):
        try:
            processes.append(proc.info)
        except:
            continue
    return processes

def get_network_connections():
    conns = []
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == 'LISTEN' or conn.status == 'ESTABLISHED':
            conns.append({
                'laddr': str(conn.laddr),
                'raddr': str(conn.raddr) if conn.raddr else '',
                'pid': conn.pid
            })
    return conns

def get_crontab_entries():
    try:
        output = subprocess.check_output(['crontab', '-l'], text=True)
        return output.strip().split('\n')
    except:
        return []

def get_systemd_services():
    try:
        files = os.listdir('/etc/systemd/system/')
        return files
    except:
        return []

def collect_all():
    return {
        'processes': get_processes(),
        'network': get_network_connections(),
        'crontab': get_crontab_entries(),
        'systemd': get_systemd_services(),
        'os': platform.system()
    }
