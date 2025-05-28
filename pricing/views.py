from django.shortcuts import render
from .models import Service, PortfolioItem

def portfolio(request):
    items = PortfolioItem.objects.all().order_by('-created_at')
    return render(request, 'pricing/portfolio.html', {'items': items})

def service_list(request):
    services = Service.objects.all()
    return render(request, 'pricing/services.html', {'services': services})

def calculator_view(request):
    result = None
    context = {
        'selected_service': '',
        'selected_material': '',
        'width': '',
        'height': '',
    }

    if request.method == 'POST':
        service = request.POST['service_type']
        material = request.POST['material']
        width = request.POST['width']
        height = request.POST['height']

        context.update({
            'selected_service': service,
            'selected_material': material,
            'width': width,
            'height': height,
        })

        try:
            area = float(width) * float(height)
            base_price = {
                'banner_fabric': 500,
                'mesh': 450,
                'lightbox_film': 700,
                'pvc': 300,
                'plastic': 350,
                'composite': 600,
                'vinyl': 400,
                'perforated_vinyl': 450,
                'uv_acrylic': 800,
                'vinyl_gloss': 700,
                'vinyl_matte': 750,
                'vinyl_special': 900,
                'reinforced_banner': 600,
                'blockout': 650,
                'acrylic': 900,
                'metal': 1100,
                'composite_led': 1200,
            }
            price_per_m2 = base_price.get(material, 500)
            result = round(area * price_per_m2, 2)
        except:
            result = None

    context['result'] = result
    return render(request, 'pricing/calculator.html', context)



