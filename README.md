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
# Result
![result_image](https://github.com/BUEC500C1/twitter-summarizer-Jie1995tbc/raw/master/result_image.png)
The Twitter API will get the url. Users can use these links to download and save images on your device. Then use google vision api to describe images.
