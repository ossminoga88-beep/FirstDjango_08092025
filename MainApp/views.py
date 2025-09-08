from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
author = {
    "Имя": "Владимир",
    "Отчество": "Сергеевич",
    "Фамилия": "Васин",
    "телефон": "8-916-678-85-17",
    "email": "ossminoga88@gmail.com",
}


def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Васин В.С.</i>
    """
    return HttpResponse(text)


def about(request):
    text = f"""
        Имя: {author['Имя']}<br>
        Отчество: {author['Отчество']}<br>
        Фамилия: {author['Фамилия']}<br>
        телефон: {author['телефон']}<br>
        email: {author['email']}<br>
        """
    return HttpResponse(text)

def get_item(request, item_id: str):
    return HttpResponse(item_id)