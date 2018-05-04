from django.db import models
from django.contrib.auth.models import User
# Create your models here.

GAME_STATUS_CHOICE =(
    ('F', 'First Player to move'),
    ('S', 'Second Player to move'),
    ('W', 'First Player wins'),
    ('L', 'Second Player wins'),
    ('D', 'Draw')
)


class Game(models.Model):
    first_player = models.ForeignKey(User,on_delete=models.CASCADE, related_name="games_first_player")
    second_player = models.ForeignKey(User, on_delete=models.CASCADE, related_name="games_second_player")

    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,default='F', choices=GAME_STATUS_CHOICE)

    def __str__(self):
        return "{0} vs {1}".format(self.first_player, self.second_player)


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    by_first_player  = models.BooleanField()

    game = models.ForeignKey(Game, on_delete=models.CASCADE)