from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=50)
    pg_goal = models.FloatField()

    def __str__(self):
        return self.choice_text