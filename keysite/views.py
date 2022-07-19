from django.shortcuts import render
from .models import Cmd
from django.db.models import Q

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

def Search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        searched_list = Cmd.objects.filter(
            Q(choice_OS__icontains=searched)|
            Q(program__icontains=searched)|
            Q(cmd_category__icontains=searched)|
            Q(cmd_name__icontains=searched)|
            Q(cmd_description__icontains=searched)
        )
        return render(request, 'Search_list.html', {'searched': searched, 'searched_list': searched_list})
    else:
        return render(request, 'Search_list.html', {})