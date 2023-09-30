from django.contrib import admin
from .models import departments, doctors, booking


admin.site.register(departments)
admin.site.register(doctors)
class bookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_name', 'p_phone', 'p_email', 'dep_name', 'booking_date', 'booked_on')
admin.site.register(booking, bookingAdmin)
