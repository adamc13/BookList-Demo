from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Books

# Create your views here.
sort_count = {'title': 0, 'author': 0, 'isbn': 0}


def index(request):
    global sort_count
    template = 'index.html'
    sort_count = {'title': 0, 'author': 0, 'isbn': 0}
    return render(request, template,
                  {'bookSet': Books.objects.all()})


def create_book(request):
    if request.method == 'POST':
        data = request.POST
        title, author, isbn, url = data['title'], data['author'], data['isbn'], data['url']
        try:
            Books.objects.get(title=title, author=author, isbn=isbn, url=url)
            return HttpResponse('', status=401)
        except Books.DoesNotExist:
            Books.objects.create(title=title, author=author, isbn=isbn, url=url)
        return HttpResponse('')


def update_books(request):
    order_set = [(key, val) for key, val in sort_count.items() if val != 0]
    if order_set:
        key, val = order_set[0]
        order_set = Books.objects.order_by('-' * (1 - val % 2) + key)
    else:
        order_set = Books.objects.all()
    return render(request, 'book_list.html',
                  {'bookSet': order_set})


def delete_book(request):
    if request.method == 'POST':
        book = get_object_or_404(Books, pk=request.POST['book_id'])
        book.delete()
    return HttpResponse('')


def sort(request):
    global sort_count
    if request.method == 'POST':
        key = request.POST['sort_id'][2:]
        val = sort_count[key] + 1
        sort_count = {'title': 0, 'author': 0, 'isbn': 0}
        sort_count[key] = val
        return render(request, 'book_list.html', {'bookSet':
                      Books.objects.order_by('-' * (1 - val % 2) + key)})
