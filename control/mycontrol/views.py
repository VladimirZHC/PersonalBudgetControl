
from django.shortcuts import render, redirect
from .forms import BudgetForm
from django.db.models import Sum
from .models import Budget
# from django.views.generic import CreateView


def home(request):
    if request.method == 'POST':
        sendForm = BudgetForm(request.POST)
        if sendForm.is_valid():
            sendForm.save()
            return redirect('home')   
    else:
        sendForm = BudgetForm()
    
    # summary = list(Budget.objects.values())
    # for sum in range(len(summary)):
    #     consum =  summary[sum]['value'] - summary[sum]['consumption']
    #     main_res = summary[sum]['value']
    
    main_res = Budget.objects.all().aggregate(Sum('value'))
    print(main_res)
    revenue = Budget.objects.all().aggregate(Sum('consumption'))
    print(revenue)
    consum = main_res['value__sum'] - revenue['consumption__sum']
    print(consum)
        
        
    data = {
        'main_res': main_res['value__sum'],
        'consum': consum,
        'history': Budget.objects.all(),
        'sendForm': sendForm
    }
           
    return render(request, 'mycontrol/home.html', data)
