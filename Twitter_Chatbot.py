import tweepy as tw

consumer_key='5zUuS9D0opAlpKQ2R8zALaxP2'
consumer_secret='uLs4sa6CVLvmZubu6IRE0GHJKdzvIalDIjGY0KjcG4bpH5hLM4'
access_token='1547854988030136321-dqjkeOpzGjWd3W3UqIhNCaDSZqu3Ch'
access_token_secret='sMTojA5Qr8vCnvUOshEeW0UO1PVKDfFNgPmE4yhLGp6qv'

auth=tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tw.API(auth)

#My personal info
user=api.verify_credentials()
print('User details are:')
print(user.name)
print(user.screen_name)
print(user.followers_count)

#My friends
for friend in user.friends():
    print(friend.name)

#Recent tweets
public_tweets=api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
    
#follow all
for follower in tw.Cursor(api.get_followers).items():
    follower.follow()    

    