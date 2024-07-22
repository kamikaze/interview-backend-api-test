from django.db import models


class Event(models.Model):
    EVENT_TYPES = {'PushEvent', 'ReleaseEvent', 'WatchEvent'}

    type = models.CharField(max_length=256, choices=tuple((item, item) for item in EVENT_TYPES))
    public = models.BooleanField()
    repo_id = models.IntegerField()
    actor_id = models.IntegerField()
