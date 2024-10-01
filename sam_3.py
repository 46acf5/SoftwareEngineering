import time
from datetime import datetime

def timedisp():
    for _ in range (5):
        now = datetime.now().strftime('%H:%M:%S')
        print(f"Current time: {now}")
        time.sleep(1)
        continue

if __name__ == '__main__':
    timedisp()
