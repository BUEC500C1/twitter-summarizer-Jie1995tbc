import tweepy
from googlevision import google_vision_api



def tweepy_api(queue):
    consumer_key = 'BePXBQnnodwym2KOVSVaDGMJt'
    consumer_secret = 'vj4G9SYGRzHWZLwHoHtsUjqeBNgQQY7q4FFPnxs3SkTDGfaQ7E'
    access_token = '1171640747352842244-WPkonJaaXqQFSDJPwyT218uYW6WsSO'
    access_token_secret = 'izFind6UV5DghAsQLdXxoo2TVpks7hv8mJ5lEKG32r0Kl'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    #public_tweets = api.search(q='tesla', count=10)

    public_tweets = []
    new_tweets = api.user_timeline(screen_name = queue,count=50)
    public_tweets.extend(new_tweets)

    #take the first 5 tweets with image and sent to google vision api for image interpretation
    count = 6

    result = ''

    for tweet in public_tweets:
        #not all tweets will have media url, so lets skip them
        try:
            print(tweet.entities['media'][0]['media_url'])
        except(NameError, KeyError):
            pass

        else:
            result += google_vision_api(tweet.entities['media'][0]['media_url'])
            result += '\n'
            count = count - 1
        if count==0:
            break

    return result


if __name__ == '__main__':
    tweepy_api('tesla')

