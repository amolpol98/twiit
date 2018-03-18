from core.api.decorators.validators import allowed_methods
from twiits.models import Tweet
from .update_tweet import UpdateTweet
import core.api.responses.error_codes as error_codes


class UpdateTweetV1(UpdateTweet):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(UpdateTweetV1, self).__init__(**kwargs)
        self.allowed_methods = ('POST', )

    @allowed_methods
    def get_or_create_data(self):
        ctxt = dict()
        self._data = ctxt

        ctxt['is_updated'] = False

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

        content = self.request.POST.get('content')
        if not content:
            self.set_404('new tweet content not sent', error_code=error_codes.MISSING_PARAMS)
            return self._data

        tweet.content = content
        tweet.save()
        ctxt['is_updated'] = True

        return self._data
