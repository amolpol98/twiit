from django.conf.urls import include, url

urlpatterns = [
    url(r'^v(?P<_v>[0-9.]+)/tweet/', include('twiits.api_urls')),
    url(r'^v(?P<_v>[0-9.]+)/profiles/', include('users.api_urls'))
]