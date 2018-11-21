import tweepy

auth = tweepy.OAuthHandler('Public API Key', 'Secret API Key')
access_token = 'Insert Public Access Token'
secret_access = 'Insert Secret Access Token'
auth.set_access_token(access_token, secret_access)


api = tweepy.API(auth)


class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_data(self, data):
        print(data)
        return True


StreamListener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=StreamListener)

stream.filter(track=['hudl'])
