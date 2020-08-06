from django.shortcuts import render


def index_view(request):
    data = 'Hello World'
    return render(request, 'index.html', {'data': data})


