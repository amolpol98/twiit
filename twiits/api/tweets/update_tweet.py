from core.api.responses.v1 import APIResponse


class UpdateTweet(APIResponse):
    __versions_compatible__ = ('1.0',)

    def __init__(self, **kwargs):
        super(UpdateTweet, self).__init__(**kwargs)
