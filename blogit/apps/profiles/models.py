from django.db import models
from blogit.apps.core.models import TimestampedModel


class Profile(TimestampedModel):
    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE
    )

    bio = models.TextField(blank=True)

    image = models.URLField(blank=True)

    follows=models.ManyToManyField('self',related_name='followed_by',symmetrical=False)

    favourites=models.ManyToManyField('articles.Article',related_name='favourited_by')

    def __str__(self):
        return self.user.username

    def follow(self,profile):
        self.follows.add(profile)

    def unfollow(self,profile):
        self.follows.remove(profile)

    def is_following(self,profile):
        return self.follows.filter(pk=profile.pk).exists()

    def is_followed_by(self,profile):
        return self.followed_by.filter(pk=profile.pk).exists()

    def favourite(self,article):
        return self.favourites.add(article)

    def unfavourite(self,article):
        return self.favourites.remove(article)

    def has_favourited(self,article):

        return self.favourites.filter(pk=article.pk).exists()