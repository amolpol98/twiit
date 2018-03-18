from core.api.responses.v1 import APIResponse


class DeleteTweet(APIResponse):
    __versions_compatible__ = ('1.0',)

    def __init__(self, **kwargs):
        super(DeleteTweet, self).__init__(**kwargs)
