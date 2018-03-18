from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from twiits.api.tweets.list_tweets import ListTweets
from twiits.api.tweets.create_tweet import CreateTweet
from twiits.api.tweets.tweet_detail import TweetDetail
from twiits.api.tweets.update_tweet import UpdateTweet
from twiits.api.tweets.delete_tweet import DeleteTweet

urlpatterns = [
    url('^list/$', ListTweets.as_versioned_view(), name='tweets'),
    url('^create/$', csrf_exempt(CreateTweet.as_versioned_view()), name='create'), # /tweet/create/
    url('^(?P<tweet_id>\d+)/$', TweetDetail.as_versioned_view(), name='detail'), # /tweet/1/
    url('^(?P<tweet_id>\d+)/update/$', csrf_exempt(UpdateTweet.as_versioned_view()), name='update'), # /tweet/1/update/
    url('^(?P<tweet_id>\d+)/delete/$', csrf_exempt(DeleteTweet.as_versioned_view()), name='delete'), # /tweet/1/delete/
]
