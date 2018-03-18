from core.api.decorators.validators import allowed_methods
from twiits.models import Tweet
from .delete_tweet import DeleteTweet
import core.api.responses.error_codes as error_codes


class DeleteTweetV1(DeleteTweet):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(DeleteTweetV1, self).__init__(**kwargs)
        self.allowed_methods = ('POST', )

    @allowed_methods
    def get_or_create_data(self):
        ctxt = dict()
        self._data = ctxt

        tweet_id = self.kwargs.get('tweet_id')
        if not tweet_id:
            self.set_bad_req('tweet id not passed', error_code=error_codes.MISSING_PARAMS)
            return self._data

        user = self.get_user()
        try:
            tweet = Tweet.objects.get(id=tweet_id, user=user)
            tweet.delete()
            ctxt['is_deleted'] = True
        except Tweet.DoesNotExist:
            ctxt['is_deleted'] = False

        return self._data
