from django.shortcuts import render
from . models import Student

# Create your views here.
def home(request):
    return render(request, "index.html")

def SampleTable(request):
    return render(request, "SampleTable.html")

def StudentTable(request):
    fname = ""
    lname = ""
    email = ""
    phone = ""
    DOB = ""
    if request.method=="POST":
       fname = request.POST['fname']
       lname = request.POST['lname']
       email = request.POST['email']
       phone = request.POST['phone']
       DOB = request.POST['DOB']

       db = Student(fname=fname,lname=lname,email=email,phone=phone,DOB=DOB)
       db.save()
    db = Student.objects.all()
    # for d in db:
    #     print(d.DOB)
       
    return render(request, "StudentTable.html",{"students":db})

def StudentDetail(request,id):
    db = Student.objects.get(id=id) # select * from Student where id=id
    
    return render(request, "StudentDetail.html",{"student":db})