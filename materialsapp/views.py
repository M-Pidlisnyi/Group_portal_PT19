from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Material
from .forms import MaterialForm

@login_required
def material_list(request):
    materials = Material.objects.all()
    return render(request, 'materials/material_list.html', {'materials': materials})

@login_required
@permission_required('materials.add_material', raise_exception=True)
def material_create(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.created_by = request.user
            material.save()
            return redirect('material-list')
    else:
        form = MaterialForm()
    return render(request, 'materials/material_form.html', {'form': form})

@login_required
@permission_required('materials.change_material', raise_exception=True)
def material_edit(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            form.save()
            return redirect('material-list')
    else:
        form = MaterialForm(instance=material)
    return render(request, 'materials/material_form.html', {'form': form})

@login_required
@permission_required('materials.delete_material', raise_exception=True)
def material_delete(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        material.delete()
        return redirect('material-list')
    return render(request, 'materials/material_confirm_delete.html', {'material': material})
