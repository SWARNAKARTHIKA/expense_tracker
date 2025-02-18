# forms.py
from django import forms
from .models import Et

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Et
        fields = ['exp_name', 'exp_category', 'amount', 'exp_date']
        widgets = {
            'exp_category': forms.Select(choices=[
                ('Food', 'Food'),
                ('Transportation', 'Transportation'),
                ('Housing', 'Housing'),
                ('Healthcare', 'Healthcare'),

            ]),
            'exp_date': forms.DateInput(attrs={'type': 'date'})
        }
