from django.shortcuts import render

# 절대경로로 입력
def key_list(request):
    return render(request, '/Users/tanya/PycharmProjects/dev_key/templates/keylist.html',{})