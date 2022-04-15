import praw 
from better_profanity import profanity
import time

profanity.load_censor_words()


#reddit instance 
reddit = praw.Reddit(client_id = 'zvQhnJJEAkqleN3hhWU1Zg',  
                     client_secret = 'qB-bGI16vJhawMOY4SghNARaOyjc9g',  
                     username = 'anti-profanity-bot',  
                     password = 'F@ceBook2002', 
                     user_agent = 'No-Profanity')

subreddit = reddit.subreddit("memes")

reply = "Your comment has Profanity!"
for submission in subreddit.rising(limit=10):
    for comment in submission.comments:
        text = comment.body
        print(comment.body)
        censored_text = profanity.censor(text)
        print(censored_text)

        if censored_text!=comment.body:
            comment.reply(reply)    
            time.sleep(30)