from django.shortcuts import render_to_response

def homepage(request):
    return render_to_response('index.html')

def battleGroup(request):
    return render_to_response('battles.html')

