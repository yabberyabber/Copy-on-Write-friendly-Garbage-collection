from django.http import HttpResponse

def index(request):
    lists = []
    strs = []
    for i in range(16000):
        lists.append([])
        for j in range(40):
            strs.append(' ' * 8)

    return HttpResponse("Hello, world.")
