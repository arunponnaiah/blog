from django.shortcuts import render
from djangoblog.models import  Journal
from django.core.context_processors import csrf

def create(request):
    return render(request,"create.html")

def update(request):
    l_title = request.POST["title"]
    l_content = request.POST["content"]

    journal = Journal(title=l_title,content=l_content)
    journal.save()
    return render(request,"create.html")