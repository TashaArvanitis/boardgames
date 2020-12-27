from django.db import models


# Create your models here.
class GameSite(models.Model):
    game = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    donation_url = models.CharField(max_length=200, blank=True, null=True)
    have_played = models.BooleanField()
    min_players = models.IntegerField(default=0)
    max_players = models.IntegerField(default=0)

    is_intrigue = models.BooleanField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.game
