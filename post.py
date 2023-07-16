
import praw
import pandas as pd
from praw.models import MoreComments
import datetime as dt
reddit_authorized = praw.Reddit(client_id="XQpDA5IIwO8aBT31lLbtYQ",		 # your client id
							client_secret="sokOef6x-Irex_AfCMRC6XVbJB07jQ",	 # your client secret
							user_agent="CypherScraping")	 # your user agent

name_subreddit = input("Enter the name of Sub-reddit : ")

subreddit = reddit_authorized.subreddit(name_subreddit)

#posts = subreddit.top(time_filter ="week")
#posts = subreddit.top(time_filter ="month")
posts = subreddit.top(time_filter ="year")
#posts = subreddit.top(time_filter ="day")


 
posts_dict = {"Title": [],
              "Total Comments": [],
              "Post URL": [],
              "Created":[]}
 
for post in posts:
    posts_dict["Title"].append(post.title)
    posts_dict["Total Comments"].append(post.num_comments)
    posts_dict["Post URL"].append(post.url)
    posts_dict["Created"].append(post.created)
 
top_posts = pd.DataFrame(posts_dict)
#Fixing the date column
def get_date(created):
    return dt.datetime.fromtimestamp(created)

_timestamp = top_posts["Created"].apply(get_date)
top_posts = top_posts.assign(timestamp = _timestamp)

 
print("Number of posts extracted : ",top_posts.shape[0])
print(top_posts.head())
# creating a csv file 
#to_csv = top_posts.to_csv('F:\cypher\mining\data\covid19.csv', index=False)

"""
#extract the best comments from the initial post 
url = top_posts['Post URL'][0]
submission = reddit_authorized.submission(url=url)
 
post_comments = []
for comment in submission.comments:
    if type(comment) == MoreComments:
        continue
    post_comments.append(comment.body)
 
comments_df = pd.DataFrame(post_comments, columns=['comment'])
 
print("Number of Comments : ",comments_df.shape[0])
comments_df.head()
"""