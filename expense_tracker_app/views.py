# views.py

from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Et
from .forms import ExpenseForm

def index(request):
    return render(request, "index.html")

def main(request):
    category = request.GET.get('category')
    month_year = request.GET.get('month_year')
    expenses = Et.objects.all()

    if category:
        expenses = expenses.filter(exp_category=category)

    if month_year:

        year, month = month_year.split('-')
        expenses = expenses.filter(exp_date__year=year, exp_date__month=month)

    if request.method == "POST":
        if 'id' in request.POST:
            exp = Et.objects.get(id=request.POST['id'])
            form = ExpenseForm(request.POST, instance=exp)
        else:
            form = ExpenseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/main")
    else:
        form = ExpenseForm()

    return render(request, "main.html", {'exp': expenses, 'form': form})


def maindel(request, id):
    exp = Et.objects.get(id=id)
    exp.delete()
    return redirect("/main")
