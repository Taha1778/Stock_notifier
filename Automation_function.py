import schedule,time
import datetime
from datetime import datetime
from Data_fetcher import *

LATEST_DATA = None  # variable to store daily fetched data

def Automation_function(data,companies,set_time):
    global LATEST_DATA
    time_set=set_time
    def job():
        global LATEST_DATA
        print(f"⏰ Running daily fetch at {time_set}...")
        data(companies)  # store fetched data
        print("✅ Data fetched and saved in LATEST_DATA")

    # schedule it once per day
    schedule.every().day.at(time_set).do(job)

    try:
        while True:         
            print(f"🕒 Scheduler started — waiting for {time_set} each day...")
            schedule.run_pending()
            time.sleep(55)   # checks every 30 seconds (fine for daily jobs)
    except KeyboardInterrupt:
        print("\n🛑 Scheduler stopped by user.")
    return LATEST_DATA  # return the latest fetched data


