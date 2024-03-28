from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    point = models.FloatField()
    goals = models.IntegerField()
    point_lst = models.JSONField()
    match_info_lst = models.JSONField()

    def __str__(self):
        return str(self.name) + ',' + str(self.point) + ',' + str(self.goals)