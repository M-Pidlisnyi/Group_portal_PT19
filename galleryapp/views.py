from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import GalleryItem
from .forms import GalleryItemForm

# Відображення галереї
def gallery_list(request):
    items = GalleryItem.objects.all()
    return render(request, 'galleryapp/gallery_list.html', {'items': items})

# Додавання нового матеріалу
@login_required
def gallery_add(request):
    if request.method == 'POST':
        form = GalleryItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.uploaded_by = request.user
            item.save()
            return redirect('gallery-list')
    else:
        form = GalleryItemForm()
    return render(request, 'galleryapp/gallery_add.html', {'form': form})

# Модерація (для адміністратора/модератора)
@login_required
def gallery_moderate(request):
    if not request.user.is_staff:
        return redirect('gallery-list')
    items = GalleryItem.objects.filter(is_approved=False)
    return render(request, 'galleryapp/gallery_moderate.html', {'items': items})

@login_required
def approve_item(request, pk):
    if not request.user.is_staff:
        return redirect('gallery-list')
    item = get_object_or_404(GalleryItem, pk=pk)
    item.is_approved = True
    item.save()
    return redirect('gallery-moderate')
