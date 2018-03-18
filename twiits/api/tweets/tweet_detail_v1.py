from core.api.decorators.validators import allowed_methods
from twiits.models import Tweet
from .tweet_detail import TweetDetail
import core.api.responses.error_codes as error_codes


class TweetDetailV1(TweetDetail):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(TweetDetailV1, self).__init__(**kwargs)
        self.allowed_methods = ('GET', )

    @allowed_methods
    def get_or_create_data(self):
        ctxt = dict()
        self._data = ctxt

        user = self.get_user()
        tweet_id = self.kwargs.get('tweet_id')
        if not tweet_id:
            self.set_404('tweet id not passed', error_code=error_codes.MISSING_PARAMS)
            return self._data
        try:
            tweet = Tweet.objects.get(id=tweet_id, user=user)
        except Tweet.DoesNotExist:
            self.set_bad_req('tweet doesnt exist', error_code=error_codes.INVALID_PARAMS)
            return self._data

        ctxt['tweet'] = tweet.to_json()

        return self._data
