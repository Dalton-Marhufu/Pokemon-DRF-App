from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=255)
    type_1 = models.CharField(max_length=255)
    type_2 = models.CharField(max_length=255)
    total = models.IntegerField()
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    sp_atk = models.IntegerField()
    sp_deffense = models.IntegerField()
    speed = models.IntegerField()
    generation = models.IntegerField()
    lengendary = models.CharField(max_length=255)

    def __str__(self):
        return self.name
