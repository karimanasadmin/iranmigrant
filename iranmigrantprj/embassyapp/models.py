from django.db import models

class Service(models.Model):
    service_name = models.CharField(max_length=100)
    # additional detail fields
    department = models.CharField(max_length=100)
    description = models.TextField()
    # ...

    def __str__(self):
        return self.service_name


class Appointment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateField()
    # additional detail fields
    applicant_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    # ...

    def __str__(self):
        return f"Appointment ID: {self.pk}"
