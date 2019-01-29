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

from .models import BackTest, TestSetting
from .forms import BackTestForm, SettingTestForm
from robos.models import Setting

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
        queryset = self.model.objects.all().order_by('id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListBackTestView, self).get_context_data(**kwargs)
        context["backtests_list"] = self.get_queryset()
        context["per_page"] = self.request.POST.get('per_page')
        return context

class CreateBackTestView(CreateView):
    # template = loader.get_template('create_testitems.html')
    # context ={}
    # return HttpResponse(template.render(context, request))
    #model = BackTest
    # content = {}
    #template_name = "create_testitems.html"
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
            
            return self.form_valid(form)
        else:

            return self.form_invalid(form)

    def form_valid(self, form):
        # Save item
        print ("*************************************valid")
        test_object = form.save(commit=False)
        test_object.created_by = self.request.user
        test_object.save()
        return redirect("backtests:add_setting")

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

class CreateBackTestSettingView(CreateView):
    # template = loader.get_template('create_testitems.html')
    # context ={}
    # return HttpResponse(template.render(context, request))
    #model = BackTest
    # content = {}
    #template_name = "create_testitems.html"
    model = TestSetting
    form_class = SettingTestForm
    template_name = "backtests/create_setting.html"
    
    def get_context_data(self, **kwargs):
        context = super(CreateBackTestSettingView, self).get_context_data(**kwargs)
        context["backtest_obj"] = self.object
        context["backtest_form"] = context["form"]
        return context

    def post(self, request, *args, **kwargs):
        # t?o view m?i n�n object = None
        self.object = None
        form = self.get_form()
        if form.is_valid(): 
            
            return self.form_valid(form)
        else:

            return self.form_invalid(form)

    def form_valid(self, form):
        # Save item
        test_object = form.save(commit=False)
        test_object.created_by = self.request.user
        print ("*************************************valid")
        request_post = self.request.POST
      
        if request_post.get('next_btn'):

            return redirect("backtests:add_setting")
        
        if request_post.get('save_btn'):
            print ("*************************************save")
            test_object.save()
            return redirect("backtests:list")

    def form_invalid(self, form):
        print ("*************************************invalid")
        return self.render_to_response(
            self.get_context_data(form=form))


