from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from users.api import FollowUnFollowUser, UserDetail


urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetail.as_versioned_view(), name='detail'),
    url(r'^(?P<username>[\w.@+-]+)/followunfollow/$', csrf_exempt(FollowUnFollowUser.as_versioned_view()), name='followunfollow'),
]
