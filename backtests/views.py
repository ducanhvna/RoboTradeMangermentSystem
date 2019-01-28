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

from .models import BackTest
from .forms import BackTestForm

class BackTestDetailView(DetailView):
    model = BackTest
    context_object_name = "testitem_record"
    template_name = "view.html"

    def get_context_data(self, **kwargs):
        context = super(BackTestDetailView, self).get_context_data(**kwargs)
        return context

class ListBackTestView(TemplateView):
    # template = loader.get_template('testitems_list.html')
    # context = {}
    # return HttpResponse(template.render(context, request))

    model = BackTest
    template_name = "list.html"

    def get_queryset(self):
        queryset = self.model.objects.all().order_by('id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListBackTestView, self).get_context_data(**kwargs)
        context["testitems_list"] = self.get_queryset()
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
    template_name = "create.html"
    
    def get_context_data(self, **kwargs):
        context = super(CreateBackTestView, self).get_context_data(**kwargs)
        context["testitem_obj"] = self.object
        context["testitem_form"] = context["form"]
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
        test_object.save()
        return redirect("testitems:list")

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form))
        


class EditBackTestView(UpdateView):
    model = BackTest
    form_class = BackTestForm
    template_name = "create.html"
    
    def get_context_data(self, **kwargs):
        context = super(EditBackTestView, self).get_context_data(**kwargs)
        context["testitem_obj"] = self.object
        context["testitem_form"] = context["form"]
        return context

    def post(self, request, *args, **kwargs):
        # update view m?i n�n object l� object hi?n t?i
        self.object = request.object
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
        return redirect("testitems:list")

    def form_invalid(self, form):
        print(form.errors)
        # for field, errors in form.errors.items:
        #     for error in errors:
        #         print(field, error)
        return self.render_to_response(
            self.get_context_data(form=form))
            
        


