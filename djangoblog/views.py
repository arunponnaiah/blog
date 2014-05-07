from django.shortcuts import render_to_response

def view_page(request):
    return render_to_response("create.html","")