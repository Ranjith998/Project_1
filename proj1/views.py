from django.http import HttpResponse

def home (request):
    return HttpResponse('Hello World')

def welcome(request):
    data='''<html>
            <head>
            <title>welcome page</title>
            </head>
            <body>
            <h1>welcome to DJANGO class</h1>
            </body>
            </html>'''
    return HttpResponse(data)

def index1(request):
    fp=open(r'C:\Users\ACER\Desktop\Django\Project_1\proj1\welcome.html','r')
    temp=fp.read()
    return HttpResponse(temp)

def demo(request):
    fp=open(r'C:\Users\ACER\Desktop\Django\Project_1\proj1\Home.html','r')
    temp=fp.read()
    return HttpResponse(temp)
    