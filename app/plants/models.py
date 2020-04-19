from datetime import date, datetime, timedelta

from django.db import models

# Create your models here.

class Plant(models.Model):
    name = models.CharField(max_length=64)

    def watered_today(self):
        if self.water_set.latest('time').time.date() == date.today():
            return True
        return False

    def get_watering_history(self):
        start_date = self.water_set.earliest('time').time.date()
        end_date = self.water_set.latest('time').time.date()

        watering_history = []

        while start_date <= end_date:
            print(self.water_set.filter(time__date=start_date).count())
            watering_history.append((start_date, self.water_set.filter(time__date=start_date).count()))
            print(watering_history)
            start_date += timedelta(days=1)

        return watering_history
