import subprocess
import time
import sys

def ping_ip(target):
    successful_pings = 0
    ping_count = 0
    ping_fail = False

    while not ping_fail:
        ping_count += 1
        try:
            subprocess.check_output(["ping", "-c", "1", target], universal_newlines=True, stderr=subprocess.STDOUT)
            successful_pings += 1
            percentage = (successful_pings / ping_count) * 100
            print(f"Ping {ping_count} succeeded to {target} ({percentage:.2f}%)", end="\r")
        except subprocess.CalledProcessError:
            print(f"\aPing {ping_count} failed to {target}", end="\r")

        time.sleep(2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an IP address to ping.")
        sys.exit(1)

    target = sys.argv[1]
    ping_ip(target)
