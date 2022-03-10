from django.http import HttpResponse


def index(request):
    return HttpResponse("<p>Hello, world. You're at the polls index.<p>")