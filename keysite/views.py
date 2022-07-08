from django.shortcuts import render
from .models import Cmd


def key_list(request):
    cmd_list = Cmd.objects.all()
    return render(request, '../templates/keylist.html',{'cmd_list':cmd_list})