from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
author = {
    "name": "Владимир",
    "middle_name": "Сергеевич",
    "last_name": "Васин",
    "phone": "8-916-678-85-17",
    "email": "ossminoga88@gmail.com",
}


items = [
    {"id": 1, "name": "Кроссовки adidas", "quantity":5},
    {"id": 2, "name": "Куртка кожаная", "quantity":2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity":12},
    {"id": 7, "name": "Картофель фри", "quantity":0},
    {"id": 8, "name": "Кепка", "quantity":124},
]


def home(request) -> HttpResponse:
    context = {
        "name": "Васин Владимир Сергеевич",
        "email": "ossminoga@rambler.ru",
        "phone": "8-916-678-85-17"
    }
    return render(request, 'index.html', context)

#def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Васин В.С.</i>
    """
    return HttpResponse(text)


def about(request):
    author = {
        "name": "Владимир",
        "middle_name": "Сергеевич",
        "last_name": "Васин",
        "phone": "8-916-678-85-17",
        "email": "ossminoga88@gmail.com",
    }
    context = {
        'author': author,
    }
    return render(request, "about.html", context)


def get_item(request, item_id: int):
    """По указанному id возвращает элемент из списка"""
    for item in items:
        if item["id"] == item_id:
            result = f"""
            <h2> Имя: {item["name"]} </h2>
            <p> Количество: {item["quantity"]} </p>
            <p> <a href='/items'> Назад к списку товаров </a></p>
            """
            return HttpResponse(result)
        
    return HttpResponseNotFound(f' Item with ad={item_id} not found')


def get_items(request):
    result = "<h1> Список товаров </h1><ol>"
    for item in items:
        result += f""" <li><a href='/item{item["id"]}'> {item["name"]} </a> </li> """
    result += "</ol>"
    return HttpResponse(result)


