from core.api.responses.v1 import APIResponse


class ListTweets(APIResponse):
    __versions_compatible__ = ('1.0',)

    def __init__(self, **kwargs):
        print ('1')
        super(ListTweets, self).__init__(**kwargs)
