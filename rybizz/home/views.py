from django.shortcuts import render
from . models import Student
# Create your views here.
def home(request):
    return render(request, "index.html")

def SampleTable(request):
    if request.method=="POST":
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        db = Student(name=name,age=age,email=email)
        db.save()
    d = Student.objects.all()
    for f  in d:
        print(f.name,f.age)
    return render(request, "SampleTable.html")
