from core.api.responses.v1 import APIResponse


class UserRegister(APIResponse):
    __versions_compatible__ = ('1.0',)

    def __init__(self, **kwargs):
        super(UserRegister, self).__init__(**kwargs)
