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

from .models import BackTest, TestSetting, SelectedBackTest
from .forms import BackTestForm
from robos.models import Setting
from robos.forms import SettingForm

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
        test_object = form.save(commit=False)
        test_object.created_by = self.request.user
        selectedBackTestList = SelectedBackTest.objects.filter(created_by=self.request.user.id, is_setting=True)
        if selectedBackTestList.count() > 0:
            selectedBackTest = selectedBackTestList[0]
        else:
            selectedBackTest = SelectedBackTest()


        print(selectedBackTest)
        selectedBackTest.name = test_object.name
        selectedBackTest.time_start = test_object.time_start
        selectedBackTest.time_end = test_object.time_end
        selectedBackTest.status = test_object.status
        selectedBackTest.created_by = test_object.created_by
        selectedBackTest.overview = test_object.overview
        selectedBackTest.note = test_object.note
        selectedBackTest.is_setting = True
        #save 
        selectedBackTest.save()
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
    model = Setting
    form_class = SettingForm
    template_name = "backtests/create_setting.html"
    
    def get_context_data(self, **kwargs):
        context = super(CreateBackTestSettingView, self).get_context_data(**kwargs)
        context["setting_obj"] = self.object
        context["setting_form"] = context["form"]
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
        test_object.save()
        # test_object.created_by = self.request.user
        request_post = self.request.POST
            #get selecteBacktest
        selectedBackTest = SelectedBackTest.objects.filter(created_by=self.request.user.id, is_setting=True)
        if (selectedBackTest.count() > 0):
            selectedBackTest[0].settings.add(test_object)
            if request_post.get('next_btn'):
                return redirect("backtests:add_setting")
            else:
                return redirect("backtests:edit_setting")
        return redirect("backtests:list")
      
    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form))


class EditBackTestSettingView(TemplateView):
    """
    setting value

    """
    model = Setting
    context_object_name = "setting_list"
    template_name = "backtests/edit_setting.html"
    
    def get_queryset(self):
        selectedBackTest = SelectedBackTest.objects.filter(created_by=self.request.user.id, is_setting=True)
        if (selectedBackTest.count() > 0):
            queryset = selectedBackTest[0].settings.all()

            return queryset

    def get_context_data(self, **kwargs):
        context = super(EditBackTestSettingView, self).get_context_data(**kwargs)
        context["setting_list"] = self.get_queryset()
        return context

    def post(self, request, *args, **kwargs):
        request_post = self.request.POST
        selectedBackTest = SelectedBackTest.objects.filter(created_by=self.request.user.id, is_setting=True)
        if (selectedBackTest.count() > 0):
            #check if data is valid
            setting_list = selectedBackTest[0].settings.all()
            for index, setting in enumerate(setting_list):
                textSetting = "text-input" + str(index + 1)
                if not request_post.get(textSetting):
                    return redirect("backtests:edit_setting")
            # save data
            # create backtest object
            selectedBackTestObject = selectedBackTest[0]
            backtest = BackTest()
            backtest.name= selectedBackTestObject.name
            backtest.time_start = selectedBackTestObject.time_start
            backtest.time_end = selectedBackTestObject.time_end
            backtest.status = selectedBackTestObject.status
            backtest.created_by = selectedBackTestObject.created_by
            backtest.created_on = selectedBackTestObject.created_on
            backtest.completed_on = selectedBackTestObject.completed_on
            backtest.overview = selectedBackTestObject.overview
            backtest.note = selectedBackTestObject.note
            backtest.save()

            for index, setting in enumerate(setting_list):
                textSetting = "text-input" + str(index + 1)

                #tao testsetting

                testSetting = TestSetting()
                testSetting.backtest = backtest
                testSetting.setting = selectedBackTestObject.settings.all()[index]
                testSetting.settingvalue = request_post.get(textSetting)
                testSetting.save()

        return redirect("backtests:list")