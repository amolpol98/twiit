from core.api.decorators.validators import allowed_methods
from twiits.models import Tweet
from .list_tweets import ListTweets
from users.models import UserProfile


class ListTweetsV1(ListTweets):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(ListTweetsV1, self).__init__(**kwargs)
        self.allowed_methods = ('GET',)

    @allowed_methods
    def get_or_create_data(self):
        ctxt = dict()
        self._data = ctxt

        user = self.get_user()
        user_profile = UserProfile.objects.get(user=user)
        following_users = user_profile.following.all()
        _tweets = Tweet.objects.filter(user__in=following_users).order_by('-created_on')
        tweets = []
        for tweet in _tweets:
            tweets.append(tweet.to_json())

        ctxt['tweets'] = tweets

        return self._data
