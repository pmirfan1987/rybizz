from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def SampleTable(request):
    return render(request, "SampleTable.html")