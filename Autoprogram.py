import twitter_autoFavorite
import schedule,time,datetime

def job():
    twitter_autoFavorite.main()
    now=datetime.datetime.now()
    print("<<DONE>>",now.strftime('%Y-%m-%d %H:%M:%S'))

schedule.every().hour.at(":00").do(job)
#schedule.every(60).minutes.do(job)
#schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)