from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (CreateView, UpdateView, TemplateView, DetailView)
# Create your views here.
from django.http import HttpResponse
from django.template import loader

from cart.forms import CartAddSettingForm

from .models import Setting
from .forms import SettingForm


class ListSettingView(TemplateView):

    model = Setting
    template_name = "robos/list_setting.html"

    def get_queryset(self):
        queryset = self.model.objects.all().order_by('id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListSettingView, self).get_context_data(**kwargs)
        context["settings_list"] = self.get_queryset()
        context["per_page"] = self.request.POST.get('per_page')
        return context

def SettingDetailView(request, setting_id):
    print("**********************")
    print(setting_id)
    product = get_object_or_404(Setting, id=setting_id)
    cart_product_form = CartAddSettingForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'robos/detail_setting.html', context)