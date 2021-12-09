# mytwitterbot.py
# IAE 101, Fall 2021
# Project 04 - Building a Twitterbot
# Name: 
# netid:      
# Student ID: 

import sys
import time
import random
import simple_twit
from tqdm import trange

me = "IAE101111905504"
# Assign the string values that represent your developer credentials to
# each of these variables; credentials provided by the instructor.
# If you have your own developer credentials, then this is where you add
# them to the program.
# Consumer Key also known as API key
CONSUMER_KEY = "MOFfxZET6mazN5oMUYg5xDD9I"
# Consumer Secret also known as API Key Secret
CONSUMER_SECRET = "9fj8g0NPdhweuWV2JCf75gYbFo62wnYNiD4ZK6VoGPNtNFWuvj"

# Project 04 Exercises
    
# Exercise 1 - Get and print 10 tweets from your home timeline
# For each tweet, print the tweet ID, the author's name,
# the author's screen_name, the tweet creation date, and the
# tweet full_text
def exercise1(api):
    list_of_tweets = simple_twit.get_home_timeline(api, 10)
    for tweet in list_of_tweets:
        print("Tweet ID:", tweet.id)
        print("Author:", tweet.author.name)
        print("Screen Name:", tweet.author.screen_name)
        print("Created:", tweet.created_at)
        print("Tweet:", tweet.full_text)
        print()
    # pass  # remove this and replace with your solution code


# Exercise 2 - Get and print 10 tweets from another user's timeline
# For each tweet, print the tweet ID, the author's name,
# the author's screen_name, the tweet creation date, and the
# tweet full_text
def exercise2(api):
    list_of_tweets = simple_twit.get_user_timeline(api, "IAE101_ckane", 10)
    for tweet in list_of_tweets:
        print("Tweet ID:", tweet.id)
        print("Author:", tweet.author.name)
        print("Screen Name:", tweet.author.screen_name)
        print("Created:", tweet.created_at)
        print("Tweet:", tweet.full_text)
        print()
    # pass  # remove this and replace with your solution code


# Exercise 3 - Post 1 tweet to your timeline.
def exercise3(api):
    tweet = "Hello, I am a bot! This is a test tweet!\r\n"
    tweet += "Have a good day!\r\n"
    print(simple_twit.send_tweet(api, tweet))
    # pass  # remove this and replace with your solution code


# Exercise 4 - Post 1 media tweet to your timeline.
def exercise4(api):
    tweet = "Hello, I am a bot! This is a test media tweet!\r\n"
    img = "./P1010337.JPG"
    print(simple_twit.send_media_tweet(api, tweet, img))
    # pass  # remove this and replace with your solution code

# End of Project 04 Exercises

def sleep(num):
    print("Sleeping for", num, "seconds")
    for i in trange(num): 
        time.sleep(1)

# YOUR BOT CODE GOES IN HERE
def twitterbot(api):
    delay_time = 60 
    list_of_tweets = simple_twit.get_home_timeline(api, 10)
    for tweet in list_of_tweets:
        if tweet.retweeted is False and tweet.author.screen_name != me:
            if "IAE101" in tweet.full_text or "IAE101" in tweet.author.screen_name:
                if tweet.author.following is False:
                    simple_twit.follow_user(api, tweet.author.screen_name)
                    print("Followed", tweet.author.screen_name)
                print("Retweeting:", tweet.full_text)
                simple_twit.retweet(api, tweet.id)
                sleep(delay_time)
            else:
                print("Not Retweeting:", tweet.full_text)
    my_friends = simple_twit.get_my_friends(api, 10)
    for friend in my_friends:
        reply_flag = False
        user_timeline = simple_twit.get_user_timeline(api, friend.screen_name, 3)
        for tweet in user_timeline:
            if tweet.retweeted is False and tweet.author.screen_name != me:
                print("Retweeting:", tweet.full_text)
                simple_twit.retweet(api, tweet.id)
                sleep(delay_time)
                if reply_flag is False:
                    reply = "Thanks for the RT @" + tweet.author.screen_name + "!\r\n"
                    simple_twit.send_reply_tweet(api, reply, tweet.id)
                    reply_flag = True
    search_queray = "classical music"
    search_results = simple_twit.search(api, search_queray, 10)
    for tweet in search_results:
        if tweet.retweeted is False:
            if tweet.author.following is False and tweet.author.screen_name != me:
                    simple_twit.follow_user(api, tweet.author.screen_name)
                    print("Followed", tweet.author.screen_name)
            print("Retweeting:", tweet.full_text)
            simple_twit.retweet(api, tweet.id)
            reply = "Thanks for the RT @" + tweet.author.screen_name + "!\r\n"
            simple_twit.send_reply_tweet(api, reply, tweet.id)
            sleep(delay_time)
    sleep(300)
    # pass  # remove this and replace with your solution code


if __name__ == "__main__":
    # This call to simple_twit.create_api will create the api object that
    # Tweepy needs in order to make authenticated requests to Twitter's API.
    # Do not remove or change this function call.
    # Pass the variable "api" holding this Tweepy API object as the first
    # argument to simple_twit functions.
    simple_twit.version()
    api = simple_twit.create_api(CONSUMER_KEY, CONSUMER_SECRET)

    # use http proxy if needed
    # proxy = "https://192.168.2.1:1282"
    # print(simple_twit.set_proxy(api, proxy))

    # Once you are satisified that your exercises are completed correctly
    # you may comment out these function calls.
    exercise1(api)
    exercise2(api)
    exercise3(api)
    exercise4(api)

    # # This is the function call that executes the code you defined above
    # # for your twitterbot.
    twitterbot(api)
