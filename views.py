from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish(request):
    return render(request,'testApp/wish.html')