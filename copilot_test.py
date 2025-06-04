import os
import platform
import subprocess

def get_system_uptime():
    system = platform.system()
    if system == "Windows":
        # Use 'net stats srv' and parse the output
        try:
            output = subprocess.check_output("net stats srv", shell=True, encoding="utf-8")
            for line in output.splitlines():
                if "Statistics since" in line:
                    return f"System uptime (since): {line.split('since')[1].strip()}"
        except Exception as e:
            return f"Error retrieving uptime: {e}"
    elif system == "Linux":
        # Use /proc/uptime
        try:
            with open('/proc/uptime', 'r') as f:
                uptime_seconds = float(f.readline().split()[0])
                uptime_hours = uptime_seconds // 3600
                uptime_minutes = (uptime_seconds % 3600) // 60
                return f"System uptime: {int(uptime_hours)} hours, {int(uptime_minutes)} minutes"
        except Exception as e:
            return f"Error retrieving uptime: {e}"
    elif system == "Darwin":
        # macOS - use 'uptime'
        try:
            output = subprocess.check_output("uptime", shell=True, encoding="utf-8")
            return f"System uptime: {output.strip()}"
        except Exception as e:
            return f"Error retrieving uptime: {e}"
    else:
        return "Unsupported OS"

if __name__ == "__main__":
    print(get_system_uptime())
