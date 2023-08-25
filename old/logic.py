import time
import random

import subprocess

def get_batState():
    result = subprocess.run(["python", "getBatteryState.py"], capture_output=True, text=True)
    if result.returncode == 0:
        # Extract the battery state value from the output
        output = result.stdout.strip()
        state = float(output)
        return state
    else:
        # An error occurred while running the script
        print("Error:", result.stderr)
        return None


def turn_off_ac():
    print("battery state fell below 85. Turning AC off...")
    subprocess.run(["python", "turn_ac_off.py"])

def turn_on_ac():
    print("battery state rose above 98. Turning AC on...")
    subprocess.run(["python", "turn_ac_on.py"])

def main():
    # Assuming the initial battery state is in acceptable range
    batState = 90
    ac_on = False

    while True:
        batState = get_batState()
        print(f"Current battery state: {batState}")

        if batState > 95 and not ac_on:
            turn_on_ac()
            ac_on = True
        elif batState <= 85 and ac_on:
            turn_off_ac()
            ac_on = False

        time.sleep(1)  # Wait for 1 second before checking again

if __name__ == "__main__":
    main()
