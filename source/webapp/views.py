from django.shortcuts import render


# Create your views here.

def index_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        context = {
            "first_number": request.POST.get("first_number"),
            "second_number": request.POST.get("second_number"),
            "action": request.POST.get("action"),
            "result": "",
            "sign": ""
        }
        print(context)
        if context['action'] == 'add':
            context['sign'] = '+'
            context['result'] = int(context['first_number']) + int(context['second_number'])
        elif context['action'] == 'subtract':
            context['sign'] = '-'
            context['result'] = int(context['first_number']) - int(context['second_number'])
        elif context['action'] == 'multiply':
            context['sign'] = '*'
            context['result'] = int(context['first_number']) * int(context['second_number'])
        else:
            context['sign'] = '/'
            context['result'] = int(context['first_number']) / int(context['second_number'])
        return render(request, 'index.html', context)
