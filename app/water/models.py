from django.db import models

from plants.models import Plant

class Water(models.Model):
  plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
  time = models.DateTimeField(auto_now_add=True)
