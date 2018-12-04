# flask-tweepy-oauth

### Changes from original branch

This project was originally created by whichlight in 2012. The author used Python2 and a much older version of Tweepy, which rendered the original project nonfunctional as I couldn't get it to run on my machine. I've since updated it to work with Python3 and the latest version of Tweepy.

### Blog post

You can find the original author's blog post about this project here:
http://whichlight.com/tag/tutorial/ 

Look for the title "twitter applications and oauth in python with tweepy and flask".

### About this project

This is an example project demonstrating how to authorize a Twitter application in Python with Flask
and Tweepy using OAuthentication. The access tokens are retrieved upon authentication. The callback URL 
is where the app is redirected after the user authenticates with Twitter through their browser.

If you want to look into more documentation, see https://wiseodd.github.io/techblog/2015/08/29/twitter-auth-flask/ and http://docs.tweepy.org/en/3.7.0/auth_tutorial.html, as they both do a much better job of explaining this than I can.

### Requirements

* Dependencies
  * Python3
  * Flask
  * Tweepy
  
* dev.twitter
  * Consumer API key & consumer API secret key
  * Access token & access token secret

You'll need to have Flask and Tweepy installed.  To get access to the API keys and access tokens (four in total), you'll need to create a Twitter developer account at dev.twitter.com and then create an app. You'll find everything under "Keys and token" for the app you just made.

### How to run

To run the program, just open up `server.py` with your favorite text editor and fill in the necessary keys at the top. Once that's done, just open up your terminal interface, `cd` to the project directory, and then run `python server.py`. Open http://localhost:5000 in your browser when you're ready to start.

### Credits
Find the original author on GitHub at https://github.com/whichlight.

You can find me at https://github.com/ctrinh98.
