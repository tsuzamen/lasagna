# import base64
import requests
import os

TOKEN = os.environ.get('API_TOKEN', '')

def authorize():
    response = requests.post("https://api.twitter.com/oauth2/token", {
        "grant_type": "client_credentials"
    }, headers={
        "Authorization": "Basic {}".format(TOKEN)
    })
    if response.status_code != 200:
        raise Exception("Couldn't get token")
    return response.json()['access_token']

def get_tweets(token, n=10):
    INITIAL_QUERY = '?q="me+when"+filter%3Aimages'
    tweets, next_url = get_tweets_helper(token, INITIAL_QUERY)
    for i in range(n):
        new_tweets, next_url = get_tweets_helper(token, next_url)
        tweets += new_tweets
    return tweets

def get_tweets_helper(token, url_query):
    response = requests.get('https://api.twitter.com/1.1/search/tweets.json{}'.format(url_query), headers={
        "Authorization": "Bearer {}".format(token)
    })
    tweets = []
    for tweet in response.json()['statuses']:
        text = tweet['retweeted_status']['text'] if 'retweeted_status' in tweet else tweet['text']
        if not text.lower().startswith('me when'): continue
        if 'media' in tweet['entities']:
            tweet_data = {'text': text, 'media':[]}
            for media in tweet['entities']['media']:
                if media['type'] == 'photo':
                    tweet_data['media'].append(media['media_url_https'])
            if len(tweet_data['media']) > 0:
                tweets.append(tweet_data)
    return tweets, response.json()['search_metadata']['next_results']

def main():
    token = authorize()
    print(token)
    tweets = get_tweets(token)
    print(tweets)

if __name__ == '__main__':
    main()
