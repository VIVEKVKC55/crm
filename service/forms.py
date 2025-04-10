from django import forms
from .models import ServiceRequest

TIME_SLOT_CHOICES = [
    ('10:00-12:00', '10:00 - 12:00'),
    ('12:00-14:00', '12:00 - 14:00'),
    ('14:00-16:00', '14:00 - 16:00'),
]

class ServiceRequestForm(forms.ModelForm):
    requested_time = forms.ChoiceField(
        choices=TIME_SLOT_CHOICES,
        widget=forms.RadioSelect,
        label='Requested Time'
    )

    class Meta:
        model = ServiceRequest
        fields = ['customer', 'service_type', 'service_description', 'requested_time']
        widgets = {
            'service_description': forms.Textarea(attrs={'rows': 3}),
        }
