# boot.py - Runs first on Pico W startup
import network
import time
import sys
import json
import os

CONFIG_FILE = "boot.json"
IP_FILE = "last_ip.txt"

def load_config():
    """Load Wi-Fi credentials and settings from boot.json."""
    if CONFIG_FILE not in os.listdir():
        raise FileNotFoundError(f"{CONFIG_FILE} not found on device.")

    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
    except Exception as e:
        raise ValueError(f"Error reading {CONFIG_FILE}: {e}")

    # Validate required fields
    if not isinstance(config.get("ssid"), str) or not isinstance(config.get("password"), str):
        raise ValueError("Invalid Wi-Fi credentials in config file.")

    # Optional hostname
    hostname = config.get("hostname", "pico-w")

    return config["ssid"], config["password"], hostname


def save_ip(ip_address):
    """Save the last known IP address to a file."""
    try:
        with open(IP_FILE, "w") as f:
            f.write(ip_address)
        print(f"Last IP saved to {IP_FILE}: {ip_address}")
    except Exception as e:
        print(f"Failed to save IP address: {e}")


def connect_wifi(ssid, password, hostname):
    """Connect Pico W to Wi-Fi using provided credentials."""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(hostname=hostname)
    wlan.connect(ssid, password)

    print(f"Connecting to Wi-Fi SSID: {ssid} ...")
    start_time = time.time()
    while not wlan.isconnected():
        if time.time() - start_time > 15:  # Timeout after 15 seconds
            raise TimeoutError("Wi-Fi connection timed out.")
        time.sleep(0.5)

    ip_info = wlan.ifconfig()  # (IP, subnet, gateway, DNS)
    print("Connected:", ip_info)
    save_ip(ip_info[0])  # Save only the IP address


# Main boot sequence
try:
    ssid, password, hostname = load_config()
    connect_wifi(ssid, password, hostname)
except Exception as e:
    print("Boot setup failed:", e)
    sys.print_exception(e)
