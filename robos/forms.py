
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
        fields = ('name','kieu','source', 'plugin', 'note', 'overview','triger',
        'defaultvalue')
    
    