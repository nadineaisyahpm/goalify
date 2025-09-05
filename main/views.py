from django.shortcuts import render
from .models import Product

def show_main(request):
    context = {
        'app_name': 'Goalify',
        'name': 'Nadine Aisyah',
        'class': 'PBP C',
        'products': Product.objects.all(),  # ambil semua produk
    }
    return render(request, "main/main.html", context)