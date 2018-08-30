from django.db import models


class Url(models.Model):
    hash = models.SlugField(max_length=6)
    url = models.URLField(max_length=2048)
    created = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.url

    class Meta:
        indexes = [
            models.Index(fields=['hash'])
        ]
