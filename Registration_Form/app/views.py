from django.shortcuts import render
from django.http import HttpResponse
from .models import Register
# Create your views here.
def home(request):
    return render(request,"app/home.html")

def Send_Student_Info(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        mname = request.POST['mname']
        lname = request.POST['lname']
        Phone1 = request.POST['Phone1']
        Phone2 = request.POST['Phone2']
        email = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        district = request.POST['district']
        state = request.POST['state']
        pin = request.POST['pin']
        gender = request.POST['Gender']
        course = request.POST['course']
        year = request.POST['year']
        branch = request.POST['branch']
        comment = request.POST['comment']
        Register(fname = fname,mname = mname,lname = lname,Phone1 = Phone1,Phone2 = Phone2,email = email,address = address,city = city,district = district,state = state,pin = pin,gender = gender,course = course,year = year,branch = branch,comment = comment).save()
        msg = "Student Record Successfully Submitted.."
        return render(request,"app/home.html",{'msg':msg})
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")