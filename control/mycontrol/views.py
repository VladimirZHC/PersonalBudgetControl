from django.shortcuts import render, redirect
from .forms import BudgetForm
from django.contrib import messages
from .models import Budget


def home(request):
    if request.method == 'POST':
        sendForm = BudgetForm(request.POST)
        if sendForm.is_valid():
            sendForm.save()
            # messages.success(request, f'Бюджет {sendForm.cleaned_data.get("title")} было успешно отправлено')
            return redirect('home')   
    else:
        sendForm = BudgetForm()
    
    data = {
        'history': Budget.objects.all(),
        'sendForm': sendForm
    }
           
    return render(request, 'mycontrol/home.html', data)