from django.db import models




class departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name



class doctors(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_spec = models.CharField(max_length=100)
    dep_name = models.ForeignKey(departments, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')  
    
    def __str__(self):
        return self.doc_name


class booking(models.Model):
    p_name = models.CharField(max_length=100)
    p_phone = models.IntegerField()
    p_email = models.EmailField()
    dep_name = models.ForeignKey(doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.p_name
    