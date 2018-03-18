from core.api.responses.base import APIResponseBase


class APIResponse(APIResponseBase):
    """
    Base class for all doc API responses
    """

    def __init__(self, **kwargs):
        super(APIResponse, self).__init__(**kwargs)
        self.profile_id = None

    def before_creating_context(self):
        self.profile_id = self.request.META.get('HTTP_USER_PROFILE_ID')
