from django.shortcuts import render
from django.http import HttpResponse
from .models import departments, doctors
from .forms import bookingForm

def indexView(request):

    person = {
        'name' : 'Naruto',
        'age' : 17,
        'place' : 'konohakore'
    }


    
    return render(request, 'home/index.html', person)

def aboutView(request):
    return render(request, 'home/about.html')

def bookingView(request):
    form = bookingForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'home/confirmation.html')

    form = bookingForm()
    dict_form = {
        'form' : form
    }
    return render(request, 'home/booking.html', dict_form)

def doctorView(request):
    doc_dict = {  
        'doc' : doctors.objects.all()
    }
    return render(request, 'home/doctors.html', doc_dict)

def contactView(request):
    return render(request, 'home/contact.html')

def departmentView(request):

    dept_dict = {
        'dept' : departments.objects.all()
    }
    return render(request, 'home/department.html', dept_dict)
