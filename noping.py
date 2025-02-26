import subprocess
import time
import ipaddress
import sys

target = input("IP address to ping: ")

if not target:
    print("Error: IP address cannot be empty.")
    sys.exit(1)

try:
    ipaddress.ip_address(target)
except ValueError:
    print("Error: Invalid IP address format.")
    sys.exit(1)

def ping_ip(target):
    successful_pings = 0
    ping_count = 0
    ping_fail = False
    consecutive_fails = 0
    max_consecutive_fails = 20

    try:
        while not ping_fail:
            ping_count += 1
            try:
                subprocess.check_output(["ping", "-c", "1", target], universal_newlines=True, stderr=subprocess.STDOUT)
                successful_pings += 1
                consecutive_fails = 0
                percentage = (successful_pings / ping_count) * 100
                print(f"Ping {ping_count} succeeded to {target} ({percentage:.2f}%)", end="\r")
            except subprocess.CalledProcessError:
                consecutive_fails += 1
                print(f"\aPing {ping_count} failed to {target}", end="\r")
                if consecutive_fails >= max_consecutive_fails:
                    ping_fail = True
                    print(f"\nPing failed {max_consecutive_fails} times in a row to {target} aborting.")
            
            time.sleep(2)
    except KeyboardInterrupt:  # Catch KeyboardInterrupt
        print("\nScript interrupted by user. Exiting...")
        sys.exit(0)
if __name__ == "__main__":

    ping_ip(target)
