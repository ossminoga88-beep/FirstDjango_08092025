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


items = [
    {"id": 1, "name": "Кроссовки adidas", "quantity":5},
    {"id": 2, "name": "Куртка кожаная", "quantity":2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity":12},
    {"id": 7, "name": "Картофель фри", "quantity":0},
    {"id": 8, "name": "Кепка", "quantity":124},
]


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


#/item/1
#/item/2
#/item/3
#/....
#/item/n-1
#/item/n
def get_item(request, item_id: int):
    """По указанному id вщзвращает элемент из списка"""
    for item in items:
        if item["id"] == item_id:
            result = f"""
            <h2> Имя: {item["name"]} </h2>
            <p> Количество: {item["quantity"]} </p>
            """
            return HttpResponse(result)
    return HttpResponseNotFound(f' Item with ad={item_id} not found')