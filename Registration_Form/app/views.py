from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Register
# Create your views here.
def home(request):
    return render(request,"app/home.html")

def Send_Student_Info(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        Phone1 = request.POST['Phone1']
        email = request.POST['email']
        gender = request.POST['Gender']
        address = request.POST['address']
        city = request.POST['city']
        pin = request.POST['pin']
        branch = request.POST['branch']
        course = request.POST['course']
        year = request.POST['year']
        Register(fname = fname,lname = lname,Phone1 = Phone1,email = email,address = address,city = city,pin = pin,gender = gender,course = course,year = year,branch = branch).save()
        msg = "Student Record Successfully Submitted.."
        return render(request,"app/home.html",{'msg':msg})
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")
    
def show(request):
    rec = Register.objects.all()
    return render(request,"app/show.html",{'rec':rec})
    
def Delete(request):
    ID = request.GET['id']
    Register.objects.filter(id=ID).delete()
    msg = "Student Record Successfully Deleted.."
    rec = Register.objects.all()
    return render(request,"app/show.html",{'msg':msg,'rec':rec})

def edit(request):
    ID = request.GET['id']
    request.session['ID'] = ID
    for i in Register.objects.filter(id=ID):
        fname = i.fname
        lname = i.lname
        Phone1 = i.Phone1
        email = i.email
        address = i.address
        city = i.city
        pin = i.pin
        gender = i.gender
        course = i.course
        year = i.year
        branch = i.branch
    return render(request,"app/edit.html",{'fname':fname,'lname':lname,'Phone1':Phone1,'email':email,'address':address,'city':city,'pin':pin,'gender':gender,'course':course,'year':year,'branch':branch})

def Edit_Detail(request):
    if request.method == 'POST':
        ID = request.session['ID']
        fname = request.POST['fname']
        lname = request.POST['lname']
        Phone1 = request.POST['Phone1']
        email = request.POST['email']
        gender = request.POST['Gender']
        address = request.POST['address']
        city = request.POST['city']
        pin = request.POST['pin']
        branch = request.POST['branch']
        course = request.POST['course']
        year = request.POST['year']
        Register.objects.filter(id=ID).update(fname = fname,lname = lname,Phone1 = Phone1,email = email,gender = gender,address = address,city = city,pin = pin,branch = branch,course = course,year = year)
        msg = "Student Record Successfully Edited.."
        rec = Register.objects.all()
        return render(request,"app/show.html",{'msg':msg,'rec':rec})
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")