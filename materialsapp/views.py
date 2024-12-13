from django.shortcuts import render, get_object_or_404, redirect
from .models import Material
from .forms import MaterialForm

# Список матеріалів
def material_list(request):
    materials = Material.objects.all()
    return render(request, 'materialsapp/material_list.html', {'materials': materials})

# Створення матеріалу
def material_create(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('material-list')
    else:
        form = MaterialForm()
    return render(request, 'materialsapp/material_form.html', {'form': form})

# Редагування матеріалу
def material_edit(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('material-list')
    else:
        form = MaterialForm(instance=material)
    return render(request, 'materialsapp/material_form.html', {'form': form})

# Видалення матеріалу
def material_delete(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        material.delete()
        return redirect('material-list')
    return render(request, 'materialsapp/material_confirm_delete.html', {'material': material})
