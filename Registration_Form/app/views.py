from django.shortcuts import render
from django.http import HttpResponse
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
        Current_Address = request.POST['Current_Address']
        Permanent_Address = request.POST['Permanent_Address']
        city = request.POST['city']
        district = request.POST['district']
        state = request.POST['state']
        pin = request.POST['pin']
        fname = request.POST['fname']
        fname = request.POST['fname']
        fname = request.POST['fname']
        fname = request.POST['fname']
        comment = request.POST['comment']
        msg = "Student Record Successfully Submitted.."
        return render(request,"app/home.html",{'msg':msg})
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")