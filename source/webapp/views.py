from django.shortcuts import render

from django.shortcuts import render


def calculator_view(request):
    if request.method == "GET":
        return render(request, "calculator.html")

    elif request.method == "POST":
        context = {
            'first': request.POST.get('first'),
            'second': request.POST.get('second'),
            'method': request.POST.get('method'),
            'result': 0,
        }
        context['first'] = int(context['first'])
        context['second'] = int(context['second'])

        if context['method'] == '+':
            context['result'] += (context['first'] + context['second'])

        elif context['method'] == '-':
            context['result'] += (context['first'] - context['second'])

        elif context['method'] == '*':
            context['result'] += (context['first'] * context['second'])

        elif context['method'] == '/':
            context['result'] += (context['first'] / context['second'])

        return render(request, 'calculator.html', context)