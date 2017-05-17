
import tweepy
import sys

CONSUMER_KEY='REPLACE_CONSUMER_KEY'
CONSUMER_SECRET='REPLACE_CONSUMER_SECRET'
ACCESS_TOKEN_KEY='REPLACE_ACCESS_TOKEN_KEY'
ACCESS_TOKEN_SECRET='REPLACE_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

pageCount = 5
if len(sys.argv) >= 2:
	pageCount = int(sys.argv[1])
hashtags = ['deal', 'deals', 'discount']

for tag in hashtags:
	maxId = 999999999999999999999
	for i in range(1, pageCount + 1):
		results = api.search(q='#%s' % tag, max_id=maxId, count=100)
		print len(results)
		for result in results:
			print result.text
			maxId = min(maxId, result.id)
			# only keep tweets pointing to a web page
			if result.text.find("http:") != -1:
				print "%s	%s" % (result.id, result.text.encode('utf-8').replace('\n', ' '))
