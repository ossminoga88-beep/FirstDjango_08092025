from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


author = {
    "name": "Владимир",
    "middle_name": "Сергеевич",
    "last_name": "Васин",
    "phone": "8-916-678-85-17",
    "email": "ossminoga88@gmail.com",
}


# items = [
#     {"id": 1, "name": "Кроссовки adidas", "quantity":5},
#     {"id": 2, "name": "Куртка кожаная", "quantity":2},
#     {"id": 5, "name": "Coca-cola 1 литр", "quantity":12},
#     {"id": 7, "name": "Картофель фри", "quantity":0},
#     {"id": 8, "name": "Кепка", "quantity":124},
# ]


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
    context = {'author': author}
    return render(request, "about.html", context)


def get_item(request, item_id: int):
    """Get item by id from db."""
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return render(request, "errors.html", {'errors': [f'Item with id={item+id} not found']})
    else:
        context = {"item": item}
        return render(request, "item_page.html", context)
    

def get_items(request):
    """Get all items from db."""
    context = {"items": Item.objects.all()}
    return render(request, "items_list.html", context)


