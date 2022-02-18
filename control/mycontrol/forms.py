from django import forms
from .models import Budget


class BudgetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BudgetForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Название транзакции'
        self.fields['value'].label = 'Бюджет'
        self.fields['revenue'].label = 'Доход'
        self.fields['consumption'].label = 'Расход'
        self.fields['pub_date'].label = 'Дата транзакции'
    
    
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название транзакции'})
    )
        
    class Meta:
        model = Budget
        
        fields = [
            'title',
            'value',
            'revenue',
            'consumption',
            'pub_date'
        ]
        