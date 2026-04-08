import subprocess
import time

def run_app():
    output = subprocess.check_output(["python", "inference.py"]).decode()
    return output

while True:
    print(run_app())
    time.sleep(60)
