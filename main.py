import schedule
import time
from fetch import func

print("program started")


#schedule.every().minutes.do(func)
schedule.every().day.at("17:19", "Europe/Amsterdam").do(func)

while True:
    schedule.run_pending()
    time.sleep(1)


