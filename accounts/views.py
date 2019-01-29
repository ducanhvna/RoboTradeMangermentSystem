from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.generic import (CreateView, UpdateView, DetailView, ListView, DeleteView, TemplateView)

from django.contrib.auth.models import User
import openpyxl

from .models import Account
from .forms import AccountForm

# Create your views here.

class ListAccountView(TemplateView):
    model = Account
    #context_object_name = "accounts_list"
    template_name = "accounts/list_accounts.html"

    def get_queryset(self):
        queryset = self.model.objects.all().order_by('id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListAccountView, self).get_context_data(**kwargs)
        context["accounts_list"] = self.get_queryset()
        context["per_page"] = self.request.POST.get('per_page')
        return context

class DetailAccountView(DetailView):
    model = Account
    context_object_name ="account_record"
    template_name = "accounts/detail_account.html"

    def get_context_data(self, **kwargs):
        context = super(DetailAccountView, self).get_context_data(**kwargs)
        account_record = context["account_record"]
        return context


# def CreateView(request):
#     template = loader.get_template('create_accounts.html')
#     context = {}
#     return HttpResponse(template.render(context, request))

class CreateAccountView(CreateView):
    model = Account
    form_class = AccountForm
    template_name = "accounts/create_accounts.html"

  
    def get_context_data(self, **kwargs):
        context = super(CreateAccountView, self).get_context_data(**kwargs)
        context["account_form"] = context["form"]
        context["account_obj"] = self.object

        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid(): 
            
            return self.form_valid(form)
        else:

            return self.form_invalid(form)

    def form_valid(self, form):
        # Save Account
        account_object = form.save(commit=False)
        print("**************************************************************")
        print(self.request.user)
        account_object.created_by = self.request.user
        account_object.balance = account_object.deposit
        account_object.save()
        return redirect("accounts:list")

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form))
        

class EditAccountView(UpdateView):
    model = Account
    form_class = AccountForm
    template_name = "accounts/create_accounts.html"
    
    def get_context_data(self, **kwargs):
        context = super(EditAccountView, self).get_context_data(**kwargs)
        context["account_obj"] = self.object
        context["account_form"] = context["form"]
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid(): #and billing_form.is_valid() and shipping_form.is_valid():
            
            return self.form_valid(form)
        else:

            return self.form_invalid(form)

    def form_valid(self, form):
        # Save Account
        account_object = form.save(commit=False)
        account_object.created_by = self.request.user
        account_object.balance = account_object.deposit
        account_object.save()
        return redirect("accounts:list")

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form))
        