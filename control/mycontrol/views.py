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
    
    summary = list(Budget.objects.values())
    for sum in range(len(summary)):
        consum =  summary[sum]['value'] - summary[sum]['consumption']
        main_res = summary[sum]['value']
        
        
    data = {
        'main_res': main_res,
        'consum': consum,
        'history': Budget.objects.all(),
        'sendForm': sendForm
    }
           
    return render(request, 'mycontrol/home.html', data)