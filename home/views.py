# from django.shortcuts import render

# # Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <html>
            <head>
                <title>Bakht CICD Backend</title>
            </head>
            <body style="font-family: Arial; text-align: center; margin-top: 50px;">
                <h1>Bakht CICD Backend</h1>
                <p>This is a CI/CD test project deployed via GitHub Actions on Apache.</p>
            </body>
        </html>
    """)
