from django.db import models

class Applicant(models.Model):
    full_name = models.CharField(max_length=100)
    # additional detail fields
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    # ...

    def __str__(self):
        return self.full_name


class Credit(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='credits')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # additional detail fields
    credit_date = models.DateField()
    is_approved = models.BooleanField(default=False)
    # ...

    def __str__(self):
        return f"Credit ID: {self.pk}"
