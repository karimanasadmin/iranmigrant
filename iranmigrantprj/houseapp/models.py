from django.db import models

class Address(models.Model):
    street_name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    # additional detail fields
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    # ...

    def __str__(self):
        return f"{self.street_name}, {self.city_name}"


class House(models.Model):
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='house')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # additional detail fields
    num_bedrooms = models.PositiveIntegerField()
    num_bathrooms = models.PositiveIntegerField()
    # ...

    def __str__(self):
        return f"House ID: {self.pk}"
