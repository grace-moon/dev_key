from django.shortcuts import render
from .models import Cmd

# 절대경로로 입력
def key_list(request):
    cmd_list = Cmd.objects.all()
    return render(request, '/Users/tanya/PycharmProjects/dev_key/templates/keylist.html',{'cmd_list':cmd_list})