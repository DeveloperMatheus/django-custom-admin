from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Isso é um teste para uma tarefa</h1>");