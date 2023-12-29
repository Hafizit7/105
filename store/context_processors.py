from .models import *

def category(request):
    cate = Category.objects.filter(parent_category=None)

    context = {
        'cate':cate
    }
    return context