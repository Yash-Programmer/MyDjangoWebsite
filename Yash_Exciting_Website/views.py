from django.http import HttpResponse
from django.shortcuts import render

def Hello(request):
    return render(request, 'index.html')
def About(request):
    return HttpResponse('<h2>This is about Yash</h2>')
def Contact(request):
    return HttpResponse('Contact Yash')
def Projects(request):
    return HttpResponse('Yash Project')