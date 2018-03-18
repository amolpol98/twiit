from django.contrib.auth import get_user_model

from core.api.decorators.validators import allowed_methods
from .follow_unfollow_user import FollowUnFollowUser
from users.models import UserProfile

User = get_user_model()


class FollowUnFollowUserV1(FollowUnFollowUser):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(FollowUnFollowUserV1, self).__init__(**kwargs)
        self.allowed_methods = ('POST', )

    @allowed_methods
    def get_or_create_data(self):
        ctxt = dict()
        self._data = ctxt

        username = self.kwargs.get('username')
        user_profile = UserProfile.objects.get(user=self.get_user())

        other_user = User.objects.get(username=username)
        if other_user in user_profile.following.all():
            user_profile.following.remove(other_user)
            ctxt['following'] = False
        else:
            user_profile.following.add(other_user)
            ctxt['following'] = True

        return self._data
