import requests
import tweepy
import giphy_client
from credentials import *
import json


def init_tweepy():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)


def init_giphy():
    # create an instance of the API class
    api_instance = giphy_client.DefaultApi()
    api_key = 'Qos2ut9wu6XBN2woR6LmNkb9uS46e7QV'  # str | Giphy API Key.
    q = 'puppy'  # str | Search query term or phrase.
    limit = 1  # int | The maximum number of records to return. (optional) (default to 25)
    offset = 0  # int | An optional results offset. Defaults to 0. (optional) (default to 0)
    rating = 'g'  # str | Filters results by specified rating. (optional)
    lang = 'en'  # str | Specify default country for regional content; use a 2-letter ISO 639-1 country code. See
    # list of supported languages <a href = \"../language-support\">here</a>. (optional)
    fmt = 'json'  # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)
    api_response = api_instance.gifs_search_get(api_key, q, limit=limit, offset=offset, rating=rating, lang=lang,
                                                fmt=fmt)
    print(api_response.data[0])
    print(json.dump(api_response.data[0], ))


# data=json.loads(urllib("http://api.giphy.com/v1/gifs/search?q=puppy&api_key=" + YOUR_API_KEY + "&limit=5").read())
# json.dumps(data, sort_keys=True, indent=4)

def gif_post(gif_url_list, msg):
    """
    tweets GIFs and sleeps for a specific time
    """
    for i in range(len(gif_url_list)):
        try:
            gif_download(gif_url_list[i])
            m = modifier(msg[i])
            tweet(m)
        except:
            continue


def tweet(tweet_msg):
    api = init_tweepy()
    message = tweet_msg + " #funny #gif #lol #humor"  # TODO: Add desired tweet message here
    api.update_with_media('image.gif', status=message)


def modifier(s):
    """
    returns hashtags based on the GIF names from GIPHY
    """
    ms = ''
    for i in range(len(s)):
        if s[i] == '-':
            ms += ' '
        else:
            ms += s[i]
    ls = ms.split()
    del ls[-1]
    ls[0] = "#" + ls[0]
    return " #".join(ls)


def gif_download(gif_url):
    """
    Takes the URL of an Image/GIF and downloads it
    """
    gif_data = requests.get(gif_url).content
    with open('image.gif', 'wb') as handler:
        handler.write(gif_data)
        handler.close()


init_giphy()
