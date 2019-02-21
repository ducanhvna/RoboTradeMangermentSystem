
from django import forms
from .models import Setting

class SettingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SettingForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {"class": "form-control"}
        # self.fields['description'].widget.attrs.update({'rows': '8'})
        # self.fields['assigned_to'].queryset = assigned_users
        # self.fields['assigned_to'].required = False
        # self.fields['teams'].required = False
        for key, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
        
    class Meta:
        model = Setting
        fields = ('note', )
        # widgets =  {'note': forms.HiddenInput(), }
    

class SelectSettingForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(SelectSettingForm, self).__init__(*args, **kwargs)
        setting_list = Setting.objects.all()
        for i, setting in enumerate(setting_list):
            self.fields['setting_%s' % setting.id] = forms.BooleanField(initial=False, required=False)
        # for field in self.fields.values():
        #     field.widget.attrs = {"class": "form-control"}
        # self.fields['description'].widget.attrs.update({'rows': '8'})
        # self.fields['assigned_to'].queryset = assigned_users
        # self.fields['assigned_to'].required = False
        # self.fields['teams'].required = False
        # for key, value in self.fields.items():
        #     value.widget.attrs['placeholder'] = value.label
        
    # class Meta:
    #     model = Setting
    #     fields = ('note', )
    #     widgets =  {'note': forms.HiddenInput(), }

    def get_setting_fields(self):
        for field_name in self.fields:
            if field_name.startswith('setting_'):
                yield self[field_name]

class SetValueSettingForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(SetValueSettingForm, self).__init__(*args, **kwargs)
        setting_list = Setting.objects.all()
        for i, setting in enumerate(setting_list):
            self.fields['setting_%s' % setting.id] = forms.CharField(max_length=100, required = False)
            # self.initial['setting_%s' % setting.id] = '0'
        for field in self.fields.values():
            field.widget.attrs = {"class": "form-control"}
        # self.fields['description'].widget.attrs.update({'rows': '8'})
        # self.fields['assigned_to'].queryset = assigned_users
        # self.fields['assigned_to'].required = False
        # self.fields['teams'].required = False
        for key, value in self.fields.items():
            value.widget.attrs['placeholder'] = 'Setting Value'
        
    # class Meta:
    #     model = Setting
    #     fields = ('note', )
    #     widgets =  {'note': forms.HiddenInput(), }
    def get_setting_fields(self):
        for field_name in self.fields:
            if field_name.startswith('setting_'):
                yield self[field_name]