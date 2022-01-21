from django.db import models
from django.contrib.auth.models import AbstractUser


class TimestampModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Category(TimestampModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.name)


class User(AbstractUser, TimestampModel):
    preferences = models.ManyToManyField(
        Category, blank=True, null=True, related_name="user_preference")

    def __str__(self):
        return str(self.username)


class NewsSource(TimestampModel):
    url = models.URLField()
    headers = models.JSONField(null=True, blank=True)
    params = models.JSONField(null=True, blank=True)

    def __str__(self):
        return str(self.url)


class NewsData(TimestampModel):
    url = models.URLField(unique=True)
    title = models.TextField()
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    positive_votes = models.BigIntegerField(default=0)
    negative_votes = models.BigIntegerField(default=0)

    def __str__(self):
        return str(self.url)
