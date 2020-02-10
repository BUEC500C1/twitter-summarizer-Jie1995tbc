from gcloud_tweepy import tweepy_api


if __name__ == '__main__':
    queue = input("What would you like to search?")
    assert tweepy_api(queue) is not '0'
