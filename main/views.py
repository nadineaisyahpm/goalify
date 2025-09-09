from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'Goalify',
        'name': 'Nadine Aisyah',
        'class': 'PBP C',
    }
    return render(request, "main/main.html", context)
