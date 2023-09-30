from django import forms
from .models import booking




class DateInput(forms.DateInput):
    input_type = 'date'


class bookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = '__all__'

        widgets = {
            'booking_date' : DateInput(),

        }

        labels = {
            'p_name' : "Patient Name ",
            'p_phone' : "Patient Phone",
            'p_email' : "Patient Email",
            'dep_name' : "Department Name",
            'booking_date' : "Booking Date",
        }