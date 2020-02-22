# Google Vision/Twitter API to analyze text/image
Get feeds(image) from Twitter by tweepy and descripe the image with text

# Prerequisite
Set up the Twitter API/Google Vision API
- [Twitter API](https://developer.twitter.com/en/apps)
- [Google Vision API](https://cloud.google.com/vision/docs/quickstart-cli?hl=en)

Install tweepy
```python
  pip install tweepy
  ```
Enable Vision API
Add the GOOGLE_CREDENTIAL_ENVIRONMENT into your path
```python

  eg: export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"
  ```
# Continuous Integrate
Since googleAPI keys doesn't upload here, once provided it's valid. The pytest work and pass on my local laptop when the api json file under the same directory.

# Result
Here is the sample from the twitterapi.py file. Url from the twitter and then google vision api analyze this url and get the result.

![result_image](https://github.com/BUEC500C1/twitter-summarizer-Jie1995tbc/blob/master/getURLandVisionResult.png)

