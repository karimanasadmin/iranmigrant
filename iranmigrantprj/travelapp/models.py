from django.db import models

class Destination(models.Model):
    place_name = models.CharField(max_length=100)
    # additional detail fields
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    # ...

    def __str__(self):
        return self.place_name


class Travel(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='travels')
    travel_date = models.DateField()
    # additional detail fields
    traveler_name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    # ...

    def __str__(self):
        return f"Travel ID: {self.pk}"
