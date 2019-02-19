from decimal import Decimal
from django.conf import settings
from robos.models import Setting


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'setting_value': 0, }
        if update_quantity:
            self.cart[product_id]['setting_value'] = quantity
        else:
            self.cart[product_id]['setting_value'] = quantity
        self.save()

    def add_backtest(self, backtestSetting):
        name = str(backtestSetting.name)
        time_start = str(backtestSetting.time_start)
        time_end = str(backtestSetting.time_end)
        status = str(backtestSetting.status)
        created_by = str(backtestSetting.created_by)
        overview = str(backtestSetting.overview)
        note = str(backtestSetting.note)
        created_by = str(backtestSetting.created_by)
        self.cart['backtest'] = {'name' : name, 'time_start': time_start, 'time_end' : time_end, 'status' : status,
        'created_by' : created_by, 'overview' : overview, 'note' : note , 'created_by' : created_by}
        self.save()

    def add_backtest_setting(self, setting):
        self.cart['backtest'] = setting
        self.save()
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    # def __iter__(self):
    #     product_ids = self.cart.keys()
    #     products = Setting.objects.filter(id__in=product_ids)
    #     for product in products:
    #         self.cart[str(product.id)]['product'] = product


    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
