from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Portfolio, PortfolioItem
from .forms import PortfolioForm, PortfolioItemForm

@login_required
def portfolio_list(request):
    portfolios = Portfolio.objects.filter(user=request.user)
    return render(request, 'portfolio/portfolio_list.html', {'portfolios': portfolios})

@login_required
def create_portfolio(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()
            return redirect('portfolio_list')  # Перенаправлення на сторінку зі списком портфоліо
    else:
        form = PortfolioForm()
    return render(request, 'portfolio/portfolio_form.html', {'form': form})

@login_required
def edit_portfolio(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    if portfolio.user != request.user:
        return HttpResponseForbidden("Ви не можете редагувати цей проект.")

    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('portfolio_list')
    else:
        form = PortfolioForm(instance=portfolio)
    return render(request, 'portfolio/portfolio_form.html', {'form': form})

@login_required
def add_portfolio_item(request, portfolio_pk):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_pk)
    if portfolio.user != request.user:
        return HttpResponseForbidden("Ви не можете додавати елементи до цього портфоліо.")

    if request.method == 'POST':
        form = PortfolioItemForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio_item = form.save(commit=False)
            portfolio_item.portfolio = portfolio
            portfolio_item.save()
            return redirect('portfolio_detail', pk=portfolio.pk)
    else:
        form = PortfolioItemForm()
    return render(request, 'portfolio/portfolio_item_form.html', {'form': form, 'portfolio': portfolio})

def portfolio_detail(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    items = PortfolioItem.objects.filter(portfolio=portfolio)
    return render(request, 'portfolio/portfolio_detail.html', {'portfolio': portfolio, 'items': items})
