from django.db import models

class Taxpayer(models.Model):
    taxpayer_name = models.CharField(max_length=100)
    # additional detail fields
    tax_id = models.CharField(max_length=20)
    email = models.EmailField()
    # ...

    def __str__(self):
        return self.taxpayer_name


class TaxSubmission(models.Model):
    taxpayer = models.ForeignKey(Taxpayer, on_delete=models.CASCADE, related_name='tax_submissions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # additional detail fields
    submission_date = models.DateField()
    is_approved = models.BooleanField(default=False)
    # ...

    def __str__(self):
        return f"TaxSubmission ID: {self.pk}"
