from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from robos.models import Setting
from .cart import Cart
from .forms import CartAddSettingForm


@require_POST
def cart_add(request, setting_id):
    cart = Cart(request)  # create a new cart object passing it the request object 
    setting = get_object_or_404(Setting, id=setting_id) 
    form = CartAddSettingForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=setting, quantity=cd['settingvalue'], update_quantity=cd['update'])
    return redirect('robos:list_setting')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Setting, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


# def cart_detail(request):
#     cart = Cart(request)
#     for item in cart:
#         item['update_quantity_form'] = CartAddSettingForm(initial={'quantity': item['quantity'], 'update': True})
#     return render(request, 'cart/detail.html', {'cart': cart})
