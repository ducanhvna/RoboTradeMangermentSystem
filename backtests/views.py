"""
Thong tin cac view
CreateBackTestView: t?o testitem view
EditBackTestView: s?a testitem view
ListBackTestView: list test item view
"""


from django.shortcuts import render, redirect
from django.views.generic import (CreateView, UpdateView, TemplateView, DetailView)
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from django import forms

from formtools.wizard.views import SessionWizardView

from .models import BackTest, TestSetting
from .forms import BackTestForm
from robos.models import Setting
from robos.forms import SettingForm, SelectSettingForm, SetValueSettingForm
from cart.cart import Cart

class BackTestDetailView(DetailView):
    model = BackTest
    context_object_name = "testitem_record"
    template_name = "backtests/view.html"

    def get_context_data(self, **kwargs):
        context = super(BackTestDetailView, self).get_context_data(**kwargs)
        return context

class ListBackTestView(TemplateView):
    # template = loader.get_template('testitems_list.html')
    # context = {}
    # return HttpResponse(template.render(context, request))

    model = BackTest
    template_name = "backtests/list.html"

    def get_queryset(self):
        print("**************************************")
        print(self.request.user.id)
        queryset = self.model.objects.filter(created_by=self.request.user.id).order_by('id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListBackTestView, self).get_context_data(**kwargs)
        context["backtests_list"] = self.get_queryset()
        context["per_page"] = self.request.POST.get('per_page')
        return context

class CreateBackTestView(CreateView):

    model = BackTest
    form_class = BackTestForm
    template_name = "backtests/create.html"
    
    def get_context_data(self, **kwargs):
        context = super(CreateBackTestView, self).get_context_data(**kwargs)
        context["backtest_obj"] = self.object
        context["backtest_form"] = context["form"]
        return context

    def post(self, request, *args, **kwargs):
        # t?o view m?i n�n object = None
        self.object = None
        form = self.get_form()
        if form.is_valid(): 
            
            return self.form_valid(request, form)
        else:

            return self.form_invalid(form)

    def form_valid(self, request, form):
        # Save item to session

        test_object = form.save(commit=False)
        test_object.created_by = self.request.user
        # test_object.save()
        # create cart
        cart = Cart(request)
        cart.add_backtest(backtestSetting = test_object)


        return redirect("robos:list_setting")

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form))
        
class EditBackTestView(UpdateView):
    model = BackTest
    form_class = BackTestForm
    template_name = "backtests/create.html"
    
    def get_context_data(self, **kwargs):
        context = super(EditBackTestView, self).get_context_data(**kwargs)
        context["backtest_obj"] = self.object
        context["backtest_form"] = context["form"]
        return context

    def post(self, request, *args, **kwargs):
        
        self.object = self.get_object()
        # l?y d? li?u t? form
        form = self.get_form()
        if form.is_valid(): 
            
            return self.form_valid(form)
        else:

            return self.form_invalid(form)

    def form_valid(self, form):
        # Save item
        test_object = form.save(commit=False)
        test_object.created_by = self.request.user
        test_object.save()
        return redirect("backtests:add_setting")

    def form_invalid(self, form):
        print(form.errors)
        # for field, errors in form.errors.items:
        #     for error in errors:
        #         print(field, error)
        return self.render_to_response(
            self.get_context_data(form=form))

def order_backtest(request):
    # cart = Cart(request)
    # if request.method == 'POST' :
    # get back test infor
    cart = request.session.get(settings.CART_SESSION_ID, None)
    if cart is None:
        return redirect("backtests:list")
    selectedBackTestObject = cart['backtest']
    backtest = BackTest()
    backtest.name= selectedBackTestObject['name']
    backtest.time_start = selectedBackTestObject['time_start']
    backtest.time_end = selectedBackTestObject['time_end']
    backtest.status = selectedBackTestObject['status']
    backtest.created_by = request.user
    backtest.overview = selectedBackTestObject['overview']
    backtest.note = selectedBackTestObject['note']
    backtest.save()
    # get backtest setting
    cart.pop('backtest', None)
    product_ids = cart.keys()

    print("*******************")
    print((product_ids))
    products = Setting.objects.filter(id__in=product_ids)
    for product in products:
        #tao testsetting
        testSetting = TestSetting()
        testSetting.backtest = backtest
        testSetting.setting = product
        testSetting.settingvalue = cart[str(product.id)]['setting_value']
        testSetting.save()

    cart = Cart(request)
    cart.clear()
    return redirect("backtests:list")

FORMS = [("create_backtest", BackTestForm),
         ("select_setting", SelectSettingForm),
         ("edit_setting", SetValueSettingForm)]

TEMPLATES = {"create_backtest": "backtests/create.html",
             "select_setting": "backtests/create_setting.html",
             "edit_setting": "backtests/edit_setting.html"
            }



class CreateBackTestWizardView(SessionWizardView):
    form_list = FORMS
    #custome template name for each form
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

# customer context data
    def get_context_data(self, form, **kwargs):
        context = super(CreateBackTestWizardView, self).get_context_data(form=form, **kwargs)
        if self.steps.current == 'select_setting' or self.steps.current =='edit_setting':
            settings_list = Setting.objects.all()
            context.update({'settings_list': settings_list})
        return context

    def done(self, form_list, **kwargs):
        # do_something_with_the_form_data(form_list)
        # create backtest and save to database

        
        i = 0
        for form in form_list:
            if i == 0:
                #backtest form

                backtest_object = form.save(commit=False)
                backtest_object.created_by = self.request.user
                backtest_object.save()

            if i == 1:
                selectSetting = form.cleaned_data
            
            if i == 2:
                valueSetting = form.cleaned_data

            i = i + 1
        # tao testsetting
        setting_List = Setting.objects.all()
        print(type(setting_List))
        i = 0
        for key, value in selectSetting.items():
            if  value == True:
                testSetting = TestSetting()
                testSetting.backtest = backtest_object
                testSetting.setting = setting_List[i]
                testSetting.settingvalue = valueSetting[key]
                testSetting.save()
            
            i = i + 1


        return redirect("backtests:list")

    def get_form(self, step=None, data=None, files=None):
        form = super().get_form(step, data, files)

        if step is None:
            step = self.steps.current


        if step == 'edit_setting':
            step1_data = self.get_cleaned_data_for_step('select_setting')
            for key , value in step1_data.items():
                # if is check then display
                if value == True:
                    form.fields[key].required = True
                
        return form