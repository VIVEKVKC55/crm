from django.db import models
from customer.models import Customer  # Adjust import if needed

class ServiceRequest(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('free', 'Free'),
        ('paid', 'Paid'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='service_requests')
    service_type = models.CharField(max_length=10, choices=SERVICE_TYPE_CHOICES)
    service_description = models.TextField()
    requested_date = models.DateField()
    requested_time = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer} - {self.service_type.capitalize()} - {self.requested_date} {self.requested_time}"
    
    class Meta:
        db_table = 'service_request'
