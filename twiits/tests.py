from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Tweet

User = get_user_model()

class TweetModelTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='test')

    def test_tweet_creation(self):
        tweet = Tweet.objects.create(user=User.objects.first(), content='TweetModelTestCase')
        self.assertTrue(tweet.content == 'TweetModelTestCase')
