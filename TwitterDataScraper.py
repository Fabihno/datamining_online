import os
import tweepy as tw
import pandas as pd

import tkinter as tk
import requests
import base64
from tkinter import messagebox
import tkinter.font as font


def scrapeData():
    search_words = searchWord.get()
    path = direc.get()
    no = n.get()
 
    twitter_data = []
    #payload = {'api_key': 'APIKEY', 'user_id': 'TWITTER_USER_ID', 'next_cursor': 'NEXT_CURSOR_VALUE'}
    
    payload = {
    'api_key': '7a6782380340d8d9e3de4f85724546b1', #Your ScraperAPI API key – you can find it in your dashboard
    'query': search_words, #The query you want to get data from
    'num': no,#Number of maximum returned tweets and profiles combined
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
    path = path+'data/scraped_tweets.csv'
    df.to_csv(path, index=False)
    print('Tweets exported to a CSV file')
    print(df)



wn = tk.Tk()
wn.geometry("500x500")
wn.configure(bg='azure2')
wn.title("Trizzo254 Twitter Data Scraper")
searchWord = tk.StringVar()
direc=tk.StringVar(wn)
n=tk.IntVar(wn)

headingFrame1 = tk.Frame(wn,bg="gray91",bd=5)
headingFrame1.place(relx=0.05,rely=0.1,relwidth=0.9,relheight=0.16)

headingLabel = tk.Label(headingFrame1, text=" Welcome to Trizzo254 Twitter Data Srcaper", fg='grey19', font=('Courier',12,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


tk.Label(wn, text='Enter the word to be searched on twitter',bg='azure2', font=('Courier',10)).place(x=20,y=150)

tk.Entry(wn, textvariable=searchWord,  width=35,font=('calibre',10,'normal')).place(x=20,y=170)

tk.Label(wn, text='Please enter number of data values you require',bg='azure2', anchor="e").place(x=20, y=200)
tk.Entry(wn,textvariable=n, width=35, font=('calibre',10,'normal')).place(x=20,y=220)

#Getting the path of the folder 
tk.Label(wn, text='Please enter the folder location where csv file is to be saved',bg='azure2', anchor="e").place(x=20, y=250)
tk.Entry(wn,textvariable=direc, width=35, font=('calibre',10,'normal')).place(x=20,y=270)

ScrapeBtn = tk.Button(wn, text='Scrape', bg='honeydew2', fg='black', width=15,height=1,command=scrapeData)
ScrapeBtn['font'] = font.Font( size=12)
ScrapeBtn.place(x=15,y=350)

QuitBtn = tk.Button(wn, text='Exit', bg='old lace', fg='black',width=15,height=1, command=wn.destroy)
QuitBtn['font'] = font.Font( size=12)
QuitBtn.place(x=345,y=350)

wn.mainloop()
