from django.shortcuts import render
from django.views.generic import TemplateView, View

class DashboardView(View):
    template_name = 'dashboard/base.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})