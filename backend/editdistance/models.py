from django.db import models
from .utils.edit_distance_cpsc_485 import *


class EditDistanceWords(models.Model):
    word_one = models.CharField(max_length=60)
    word_two = models.CharField(max_length=60)
    word_one_calc = models.CharField(max_length=60, default="")
    word_two_calc = models.CharField(max_length=60, default="")
    distance = models.CharField(max_length=5, default="")

    # def __str__(self):
    #     return self.word_one, self.word_two

    def save(self, *args, **kwargs):
        self.update_edit_distance()
        super().save(*args, **kwargs)

    def update_edit_distance(self):
        self.word_one_calc, self.word_two_calc, self.distance = edit_distance_alg(self.word_one, self.word_two)
