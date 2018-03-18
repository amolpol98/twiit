from django.contrib.auth import get_user_model

from core.api.decorators.validators import allowed_methods
from .user_detail import UserDetail
from twiits.models import Tweet

User = get_user_model()


class UserDetailV1(UserDetail):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(UserDetailV1, self).__init__(**kwargs)
        self.allowed_methods = ('GET', )

    @allowed_methods
    def get_or_create_data(self):
        ctxt = dict()
        self._data = ctxt

        username = self.kwargs.get('username')
        user = User.objects.get(username=username)

        _tweets = Tweet.objects.filter(user=user)
        tweets = []
        for tweet in _tweets:
            tweets.append(tweet.to_json())

        _following = user.profile.following.all()
        following = []
        for f in _following:
            following.append({
                'username': f.username
            })

        _followed_by = user.followed_by.all()
        followed_by = []
        for f in _followed_by:
            followed_by.append({
                'username': f.username
            })

        ctxt['user'] = {
            'username': user.username
        }
        ctxt['tweets'] = tweets
        ctxt['following'] = following
        ctxt['followed_by'] = followed_by

        return self._data
