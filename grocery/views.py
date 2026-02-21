from django.shortcuts import render , redirect , get_object_or_404
from .models import GroceryItem
    

# Create your views here.
def index(request):

    items=GroceryItem.objects.all()
    context={
        'items':items
    }
    return render(request, 'grocery/index.html',context)

def toggle_item(request, item_id):
    if request.method=='POST':
     item = get_object_or_404(GroceryItem, id=item_id)
    item.completed = not item.completed
    item.save()
    
    return redirect('grocery:index')


def delete_item(request , item_id):
   if request.method=='POST':
    item=get_object_or_404(GroceryItem, id=item_id)
    item.delete()

    return redirect('grocery:index')
   

def add_item(request):
   if request.method=='POST':
      name=request.POST.get('name')
      if name:
         GroceryItem.objects.create(name=name)


      return redirect('grocery:index')
