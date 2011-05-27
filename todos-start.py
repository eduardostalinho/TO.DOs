#-*- coding: utf-8 -*-

import oauth2 as oauth
import urlparse
import twitter
import dulwich
import os

PROJECT_DIR = os.path.dirname(__file__)


request_url = 'https://api.twitter.com/oauth/request_token'
access_url = 'https://api.twitter.com/oauth/access_token'
authorize_url = 'https://api.twitter.com/oauth/authorize'

consumer_key = 'sler7ISJ7YCBqsotbpslQ'
consumer_secret = '0GS34b5Tfzxv2e4s5pbmUxboaOyoqdnGPBErJv6nQ'

consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

client = oauth.Client(consumer)

resp, content = client.request(request_url, 'GET')

request_token = dict(urlparse.parse_qsl(content))

print
print 'In order to use this tool, go to the following link on your browser:'
print
print '%s?oauth_token=%s \n' % (authorize_url, request_token['oauth_token'])

accepted = 'n'
while accepted.lower() == 'n':
    accepted = raw_input('Have you accepted me? (y/n)' )
oauth_verifier = raw_input('What\'s in the pin? ')
token = oauth.Token(request_token['oauth_token'],
request_token['oauth_token_secret'])
token.set_verifier(oauth_verifier)
client = oauth.Client(consumer, token)

resp, content = client.request(access_url, 'POST')
access_token = dict(urlparse.parse_qsl(content))


token_file = open('to.dos.tk', 'w')

token_file.write(':'.join(['oauth_token',access_token['oauth_token']]))
token_file.write('\n')
token_file.write(':'.join(['oauth_token_token',
                          access_token['oauth_token_secret']]))
token_file.write('\n')
token_file.close

status = '@' + access_token['screen_name'] + ' joined our #TO.DOs session.'

api_logged = twitter.Api(consumer_key=consumer_key,
                         consumer_secret=consumer_secret,
                         access_token_key=access_token['oauth_token'],
                         access_token_secret=access_token['oauth_token_secret'])

tweet = api_logged.PostUpdate(status)

print 'Your to.dos twitter token was written to the file to.dos.tk.'
print

print
accept_git = raw_input('Do you want to initalize your git repository?(y/n)')
if accept_git == 'y':
    repository = dulwich.repo.Repo
    repository.init(PROJECT_DIR)
    print 'Git initialized at this directory'


