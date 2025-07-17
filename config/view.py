from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello Bakht!</h1><p>This is a sample Django app for CI/CD using Apache.</p>")