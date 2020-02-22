from googlevision import google_vision_api
from twitterapi import tweepy_api

# Every test include 6 label analysis
def test_exam1():
    tweepy_api('tesla')

def test_exam2():
    tweepy_api('BMW')

def test_exam3():
    tweepy_api('Honda')

if __name__ == '__main__':
    test_exam1()
    test_exam2()
    test_exam3()