from core.api.responses.v1 import APIResponse


class TweetDetail(APIResponse):
    __versions_compatible__ = ('1.0',)

    def __init__(self, **kwargs):
        super(TweetDetail, self).__init__(**kwargs)
