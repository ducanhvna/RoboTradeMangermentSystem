"""
Thong tin cac view
CreateTraderView: tạo trader view
EditTraderView: sửa trader view
ListTraderView: list test item view
"""


from django.shortcuts import render, redirect
from django.views.generic import (CreateView, UpdateView, TemplateView, DetailView)
# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Trader, TraderSetting

from robos.models import Setting
from robos.forms import SettingForm

# class TraderDetailView(DetailView):
#     model = Trader
#     context_object_name = "testitem_record"
#     template_name = "traders/view.html"

#     def get_context_data(self, **kwargs):
#         context = super(TraderDetailView, self).get_context_data(**kwargs)
#         return context
# 
class ListTraderView(TemplateView):

    model = Trader
    template_name = "traders/list.html"

    def get_queryset(self):
        queryset = self.model.objects.filter(created_by=self.request.user.id).order_by('id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListTraderView, self).get_context_data(**kwargs)
        context["traders_list"] = self.get_queryset()
        context["per_page"] = self.request.POST.get('per_page')
        return context
""" 
class CreateTraderView(CreateView):
    model = Trader
    form_class = TraderForm
    template_name = "traders/create.html"
    
    def get_context_data(self, **kwargs):
        context = super(CreateTraderView, self).get_context_data(**kwargs)
        context["trader_obj"] = self.object
        context["trader_form"] = context["form"]
        return context

    def post(self, request, *args, **kwargs):
        # tạo view mới với object = None
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
        selectedTraderList = SelectedTrader.objects.filter(created_by=self.request.user.id, is_setting=True)
        if selectedTraderList.count() > 0:
            selectedTrader = selectedTraderList[0]
        else:
            selectedTrader = SelectedTrader()


        print(selectedTrader)
        selectedTrader.name = test_object.name
        selectedTrader.time_start = test_object.time_start
        selectedTrader.time_end = test_object.time_end
        selectedTrader.status = test_object.status
        selectedTrader.created_by = test_object.created_by
        selectedTrader.overview = test_object.overview
        selectedTrader.note = test_object.note
        selectedTrader.is_setting = True
        #save 
        selectedTrader.save()
        return redirect("traders:add_setting")

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form)) """
        


# class EditTraderView(UpdateView):
#     model = Trader
#     form_class = TraderForm
#     template_name = "traders/create.html"
    
#     def get_context_data(self, **kwargs):
#         context = super(EditTraderView, self).get_context_data(**kwargs)
#         context["trader_obj"] = self.object
#         context["trader_form"] = context["form"]
#         return context

#     def post(self, request, *args, **kwargs):
        
#         self.object = self.get_object()
#         # l?y d? li?u t? form
#         form = self.get_form()
#         if form.is_valid(): 
            
#             return self.form_valid(form)
#         else:

#             return self.form_invalid(form)

#     def form_valid(self, form):
#         # Save item
#         test_object = form.save(commit=False)
#         test_object.created_by = self.request.user
#         test_object.save()
#         return redirect("traders:add_setting")

#     def form_invalid(self, form):
#         print(form.errors)
#         # for field, errors in form.errors.items:
#         #     for error in errors:
#         #         print(field, error)
#         return self.render_to_response(
#             self.get_context_data(form=form))

# class CreateTraderSettingView(CreateView):
#     model = Setting
#     form_class = SettingForm
#     template_name = "traders/create_setting.html"
    
#     def get_context_data(self, **kwargs):
#         context = super(CreateTraderSettingView, self).get_context_data(**kwargs)
#         context["setting_obj"] = self.object
#         context["setting_form"] = context["form"]
#         return context

#     def post(self, request, *args, **kwargs):
#         # t?o view m?i n�n object = None
#         self.object = None
#         form = self.get_form()
#         if form.is_valid(): 
            
#             return self.form_valid(form)
#         else:

#             return self.form_invalid(form)

#     def form_valid(self, form):
#         # Save item
#         test_object = form.save(commit=False)
#         test_object.save()
#         # test_object.created_by = self.request.user
#         request_post = self.request.POST
#             #get selecteBacktest
#         selectedTrader = SelectedTrader.objects.filter(created_by=self.request.user.id, is_setting=True)
#         if (selectedTrader.count() > 0):
#             selectedTrader[0].settings.add(test_object)
#             if request_post.get('next_btn'):
#                 return redirect("traders:add_setting")
#             else:
#                 return redirect("traders:edit_setting")
#         return redirect("traders:list")
      
#     def form_invalid(self, form):
#         return self.render_to_response(
#             self.get_context_data(form=form))


# class EditTraderSettingView(TemplateView):
    # """
    # setting value

    # """
    # model = Setting
    # context_object_name = "setting_list"
    # template_name = "traders/edit_setting.html"
    
    # def get_queryset(self):
    #     selectedTrader = SelectedTrader.objects.filter(created_by=self.request.user.id, is_setting=True)
    #     if (selectedTrader.count() > 0):
    #         queryset = selectedTrader[0].settings.all()

    #         return queryset

    # def get_context_data(self, **kwargs):
    #     context = super(EditTraderSettingView, self).get_context_data(**kwargs)
    #     context["setting_list"] = self.get_queryset()
    #     return context

    # def post(self, request, *args, **kwargs):
        # request_post = self.request.POST
        # selectedTrader = SelectedTrader.objects.filter(created_by=self.request.user.id, is_setting=True)
        # if (selectedTrader.count() > 0):
        #     #check if data is valid
        #     setting_list = selectedTrader[0].settings.all()
        #     for index, setting in enumerate(setting_list):
        #         textSetting = "text-input" + str(index + 1)
        #         if not request_post.get(textSetting):
        #             return redirect("traders:edit_setting")
        #     # save data
        #     # create trader object
        #     selectedTraderObject = selectedTrader[0]
        #     trader = Trader()
        #     trader.name= selectedTraderObject.name
        #     trader.time_start = selectedTraderObject.time_start
        #     trader.time_end = selectedTraderObject.time_end
        #     trader.status = selectedTraderObject.status
        #     trader.created_by = selectedTraderObject.created_by
        #     trader.created_on = selectedTraderObject.created_on
        #     trader.completed_on = selectedTraderObject.completed_on
        #     trader.overview = selectedTraderObject.overview
        #     trader.note = selectedTraderObject.note
        #     trader.save()
        #     selectedTraderObject.is_setting = False
        #     selectedTraderObject.save()
        #     for index, setting in enumerate(setting_list):
        #         textSetting = "text-input" + str(index + 1)

        #         #tao testsetting

        #         testSetting = TestSetting()
        #         testSetting.trader = trader
        #         testSetting.setting = selectedTraderObject.settings.all()[index]
        #         testSetting.settingvalue = request_post.get(textSetting)
        #         testSetting.save()

        # return redirect("traders:list")