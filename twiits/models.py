from django.conf import settings
from django.db import models


class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=155)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.content)

    def to_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id if self.user else 0,
            'content': self.content,
            'created_on': self.created_on,
            'updated_on': self.updated_on
        }
