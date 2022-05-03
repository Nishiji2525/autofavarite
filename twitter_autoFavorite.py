import tweepy
import time
import datetime

def main():
    CONSUMER_KEY="H3BsdZVEuqKfFsqnhYBOO8stQ"
    CONSUMER_SECRET="SjsDfge7U2EzUdWSQsJQ7R8mRezXsmE6mlWcr2ieKvju98RIyf"
    ACCESS_TOKEN="925157072341106688-wO6TRRAtTQiCFKkxjhZPTSd4s93D3eD"
    ACCESS_SECERET="d0Ok6UyeoBJxeW6qcrJRV1Z3dE3jQiXIefmKZKW1MiHky"

    auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_SECERET)
    api=tweepy.API(auth)

    q_list=["#プログラミング初心者","#駆け出しエンジニアと繋がりたい","#プログラミング"]
    count=50

    for q in q_list:
       # dt_now = datetime.datetime.now()
       # print(dt_now)
       print("Now:QUERY-->>{}".format(q))
       search_results=api.search_tweets(q=q,count=count)
       for status in search_results:
           tweet_id=status.id
           try:
               api.create_favorite(tweet_id)
               time.sleep(1)
           except:
               pass
if __name__ == '__main__':
    main()

# Endtime = datetime.datetime.now()
# print (str(Endtime) + "に終了です")