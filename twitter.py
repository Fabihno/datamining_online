import requests
import pandas as pd
 
twitter_data = []
#payload = {'api_key': 'APIKEY', 'user_id': 'TWITTER_USER_ID', 'next_cursor': 'NEXT_CURSOR_VALUE'}
 
payload = {
   'api_key': '7a6782380340d8d9e3de4f85724546b1', #Your ScraperAPI API key – you can find it in your dashboard
   'query': input("Enter What you want to scrape from Twitter"), #The query you want to get data from
   'num': '10',#Number of maximum returned tweets and profiles combined
   'time_period': '1D', #data on a single day
   #'user': 'HarronMugo'
}
#To send the initial request, let’s send a request to retrieve 3 things the query, tweets and time period
response = requests.get('https://api.scraperapi.com/structured/twitter/search', params=payload)
# To test fields that are displayed in the tweets
print(response.text)

data = response.json()
 
all_tweets = data['organic_results']

for tweet in all_tweets:
   twitter_data.append({
       'ID': tweet['position'],
       'Title': tweet["title"],
       'Snippet': tweet["snippet"],
       'URl': tweet["link"],
       'Tags': tweet["tags"]
   })
 
df = pd.DataFrame(twitter_data)
#df.to_csv('data/scraped_tweets.csv', index=False)
print('Tweets exported to a CSV file')
