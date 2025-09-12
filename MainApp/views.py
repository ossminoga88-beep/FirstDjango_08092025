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
        if item['id'] == item_id:
            context = {
                "item": item
            }
            return render(request, "item_page.html", context)
    return render(request, "errors.html", {'errors': [f'Item with id={item+id} not found']})
        

def get_items(request):
    context = {"items": items }
    return render(request, "items_list.html", context)


