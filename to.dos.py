import twitter
import sys
import dulwich
import os

PROJECT_DIR = os.path.dirname(__file__)

consumer_key = 'sler7ISJ7YCBqsotbpslQ'
consumer_secret = '0GS34b5Tfzxv2e4s5pbmUxboaOyoqdnGPBErJv6nQ'

token_file = open('to.dos.tk', 'r')

oauth_line = token_file.readline()
oauth_key = oauth_line.split(':')[1].rstrip('\n')

oauth_secret_line = token_file.readline()
oauth_secret = oauth_secret_line.split(':')[1].rstrip('\n')

api_logged = twitter.Api(consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token_key=oauth_key,
                    access_token_secret=oauth_secret)

tweet = 'commit at #TODOs ' + sys.argv[1]
api_logged.PostUpdate(tweet)

repository = dulwich.repo.Repo
dulwich.do_commit(repository, sys.argv[1])

