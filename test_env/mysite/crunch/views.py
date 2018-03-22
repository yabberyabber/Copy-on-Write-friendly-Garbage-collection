from django.http import HttpResponse

class LargeObject():
    def __init__(self):
        lists = []
        strs = []
        for i in range(1600):
            lists.append([])
            for j in range(40):
                strs.append(' ' * 8)
        self.lists = lists
        self.strs = strs

glob_a = None
glob_b = None
glob_c = None

def index(request):
    global glob_a
    global glob_b
    global glob_c
    glob_a, glob_b, glob_c = LargeObject(), glob_a, glob_b

    return HttpResponse("Hello, world.")
