from django.shortcuts import render
from .models import Cmd

def home(request):
    return render(request, '../templates/home.html')

def Win_HWP_key_list(request):
    cmd_list = Cmd.objects.filter(choice_OS='Windows', program='HWP')
    return render(request, '../templates/Win_HWP_key_list.html',{'cmd_list':cmd_list})

def Win_Word_key_list(request):
    cmd_list = Cmd.objects.filter(choice_OS='Windows', program='Word')
    return render(request, '../templates/Win_Word_key_list.html',{'cmd_list':cmd_list})

def MacOS_HWP_key_list(request):
    cmd_list = Cmd.objects.filter(choice_OS='MacOS', program='HWP')
    return render(request, '../templates/MacOS_HWP_key_list.html',{'cmd_list':cmd_list})

def MacOS_Word_key_list(request):
    cmd_list = Cmd.objects.filter(choice_OS='MacOS', program='Word')
    return render(request, '../templates/MacOS_Word_key_list.html',{'cmd_list':cmd_list})

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        searched_list = Cmd.objects.filter(name__contains=searched)
        return render(request, 'searched.html', {'searched': searched, 'recipes': recipes})
    else:
        return render(request, 'searched.html', {})