from core.api.responses.v1 import APIResponse


class CreateTweet(APIResponse):
    __versions_compatible__ = ('1.0',)

    def __init__(self, **kwargs):
        print ('entered create tweet v0')
        super(CreateTweet, self).__init__(**kwargs)
