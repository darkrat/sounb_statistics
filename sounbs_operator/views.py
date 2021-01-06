from django.shortcuts import render

# Create your views here.
def main(request):
    data = {"app_title": "Статистика", "username": "Пользователь"}
    return render(request, 'index.html', context=data)