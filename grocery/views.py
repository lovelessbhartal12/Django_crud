from django.shortcuts import render
from .models import GroceryItem
    

# Create your views here.
def index(request):

    items=GroceryItem.objects.all()
    context={
        'items':items
    }
    return render(request, 'grocery/index.html')
