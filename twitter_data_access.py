from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener

consumer_key ='AxOaYpOn28fJjYomZeW89ZNgp'
consumer_secret ='JufKpDgGP5o9J0ZYgau5NbQxPKusUSxEp6Sn5VRj9qRe8d2aAX'
access_token ='1339262838083375107-5ZoPnH1jwDQaI3TUyQlqLseDR9kRHD'
access_token_secret ='2I7pwBEMCXeBx0UyPHmAuxOyBUn9frDizQrstfKxCzlFB'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

class PrintListener(StreamListener):
    def on_status(self, status):
        if not status.text[:3] == 'RT ':
            print(status.text)
            print(status.author.screen_name, status.created_at, status.source, '\n')
            
    def on_error(self, status_code):
        print("Error Code: {}".format(status_code))
        return True  #keep Stream Alive

    def on_timeout(self):
        print("Listener Timed out!")
        return True
        
def print_to_terminal():
    listener = PrintListener()
    stream = Stream(auth, listener)
    languages = ('en',)
    stream.sample()

if __name__ == '__main__':
    print_to_terminal()
