from core.api.decorators.validators import allowed_methods
from twiits.models import Tweet
from .create_tweet import CreateTweet


class CreateTweetV1(CreateTweet):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(CreateTweetV1, self).__init__(**kwargs)
        self.allowed_methods = ('POST', )

    @allowed_methods
    def get_or_create_data(self):
        ctxt = dict()
        self._data = ctxt

        user = self.get_user()
        content = self.request.POST.get('content', 'dummy content')
        tweet = Tweet.objects.create(user=user, content=content)
        ctxt['tweet'] = tweet.to_json()

        return self._data
