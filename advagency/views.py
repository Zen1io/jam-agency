
from django.views.generic import TemplateView
from pricing.models import Service

class AboutView(TemplateView):
    template_name = "about.html"

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = Service.objects.first()  # ✅ или фильтрация по коду
        return context