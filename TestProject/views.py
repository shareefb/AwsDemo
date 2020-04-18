from django.shortcuts import render
# from django.http import HttpResponse



def hello(request, name):
	return render(request, "hello.html", {"name":name})


   #return HttpResponse("<b>Hello " + name +"</b>")