from django.http import HttpResponse
from django.shortcuts import render
import datetime
def hello(request):
    return HttpResponse("Witaj w Django!")
def hello_name(request, name):
    return HttpResponse(f"Witaj, {name}!")
def hello_template(request, name):
    return render(request, "witaj/hello.html", {"name": name})
def time(request):
    now = datetime.datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Aktualna data i godzina: {now_str}")