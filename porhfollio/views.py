from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Portfolio
from .forms import PortfolioForm  
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

class PortfolioUpdateView(LoginRequiredMixin, UpdateView):
    model = Portfolio
    fields = ['title', 'description', 'screenshot', 'link', 'file']
  
@login_required
def edit_portfolio(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    if portfolio.user != request.user:
        return HttpResponseForbidden("Ви не можете редагувати цей проект.")
    
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('portfolio_detail', pk=portfolio.pk)  
    else:
        form = PortfolioForm(instance=portfolio)
    
    return render(request, 'portfolio/edit_portfolio.html', {'form': form})
