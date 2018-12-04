#
# flask-tweepy-oauth
#
# An example program showing how to authorize a Twitter application
# in Python with Flask and Tweepy.
#

from flask import Flask
from flask import request
import flask
import tweepy
app = Flask(__name__)

# config

# you usually want to store these in a hidden file
CONSUMER_TOKEN = 'fill this out'
CONSUMER_SECRET = 'and this'
ACCESS_TOKEN = 'and this too'
ACCESS_SECRET = 'and finally this'

CALLBACK_URL = 'http://localhost:5000/verify'
session = dict()

# you can save these values to a database
db = dict()

@app.route("/")
def send_token():
	auth = tweepy.OAuthHandler(CONSUMER_TOKEN,
		CONSUMER_SECRET,
		CALLBACK_URL)

	try:
		# get the request tokens
		redirect_url= auth.get_authorization_url()
		session['request_token']= (auth.request_token)
	except tweepy.TweepError:
		print('Error! Failed to get request token.')

	# this is Twitter's url for authentication
	return flask.redirect(redirect_url)

@app.route("/verify")
def get_verification():

	# get the verifier key from the request url
	verifier = request.args.get('oauth_verifier')

	auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

	token = session['request_token']
	del session['request_token']

	auth.request_token = { 'oauth_token' : token,
                             'oauth_token_secret' : verifier }

	try:
		    auth.get_access_token(verifier)
	except tweepy.TweepError:
		    print('Error! Failed to get access token.')

	# now you have access!
	api = tweepy.API(auth)

	# store in a db
	db['api'] = api
	return flask.redirect(flask.url_for('start'))

@app.route("/start")
def start():
	# authorization done, app logic can begin
	api = db['api']

	#example, print your latest status posts
	return flask.render_template('tweets.html', tweets=api.user_timeline())

if __name__ == "__main__":
	app.run()
