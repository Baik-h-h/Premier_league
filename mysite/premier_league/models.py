from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    total_point = models.FloatField()
    goals = models.IntegerField()
    points_lst = models.JSONField(default=list)
    match_num_lst = models.JSONField(default=list)

    def __str__(self):
        return str(self.name) + ',' + str(self.point) + ',' + str(self.goals)