from django.http import HttpResponse as hr
from django.shortcuts import render


def index(request, name):
    return render(request, "hello/index.html", {"name": name.capitalize()
                         
                         
                                       })
    

def greet(request, name):
    return render(request, "hello/greet.html", {"name": name.capitalize()
                         
                         
                                       })
    

# def greet(request, name):
#     return hr(f"Hello {name.capitalize()}!")