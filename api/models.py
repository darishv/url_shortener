from django.db import models

class Url(models.Model):
    source_url = models.URLField()
    shortened_url = models.URLField()

    def __str__(self):
        return f"{self.source_url} -> {self.shortened_url}"