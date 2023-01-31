from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name': 'Kevin',
        'age': 30,
        'nationality': 'Filipino',
    }
    return render(request, 'index.html', context)

def counter(request):
    words = request.POST['text']
    num_words = len(words.split())
    return render(request, 'counter.html', {'num_words': num_words})

def todolist(request):
    return HttpResponse("<h1>This is the todolist page</h1>")