# main.py
try:
    with open("last_ip.txt", "r") as f:
        last_ip = f.read().strip()
    print(f"Last known IP: {last_ip}")
except FileNotFoundError:
    print("No IP file found. Wi-Fi may not have connected yet.")
