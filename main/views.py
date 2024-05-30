from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):
    categories = Categories.objects.all()
    context = {
        "title": "Home -Главная",
        "content": "Магаз ВСЕ У ЛЕХИ!!",
        "categories": categories,
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "О нас",
        "content": "О нас",
        "text_on_page": "Добро пожаловать! - Втюхаем все что угодно!!",
    }
    return render(request, "main/about.html", context)
