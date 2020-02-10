import io
import os
import pandas as pd
import wget
import tweepy

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


def tweepy_api(input_q):
    consumer_key = 'BePXBQnnodwym2KOVSVaDGMJt'
    consumer_secret = 'vj4G9SYGRzHWZLwHoHtsUjqeBNgQQY7q4FFPnxs3SkTDGfaQ7E'
    access_token = '1171640747352842244-WPkonJaaXqQFSDJPwyT218uYW6WsSO'
    access_token_secret = 'izFind6UV5DghAsQLdXxoo2TVpks7hv8mJ5lEKG32r0Kl'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    public_tweets = api.search(q=input_q, count=20)

    media_file = set()
    for status in public_tweets:
        media = status.entities.get('media', [])
        if len(media) > 0:
            media_file.add(media[0]['media_url'])

    for medias in media_file:
        print (medias)



# Instantiates a client
def google_vision_api():
# wget.download(medias)
    client = vision.ImageAnnotatorClient()

    file_name = 'getfromtweepy.jpg'
    file_path = r'/Users/lujie/PycharmProjects/test1'
# Loads the image into memory
    with io.open(os.path.join(file_path, file_name), 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

# Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    df = pd.DataFrame(columns=['local', 'description'])
    for test in labels:
        df = df.append(
            dict(
                local=test.locale,
                description=test.description
            ),
            ignore_index=True
        )

    print(df)

