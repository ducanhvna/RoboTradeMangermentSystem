from django import forms
from .models import BackTest, TestSetting
from bootstrap_datepicker_plus import   DateTimePickerInput


class BackTestForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BackTestForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {"class": "form-control"}
        # self.fields['description'].widget.attrs.update({'rows': '8'})
        # self.fields['assigned_to'].queryset = assigned_users
        # self.fields['assigned_to'].required = False
        # self.fields['teams'].required = False
        for key, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label


        
    class Meta:
        model = BackTest
        fields = ('name', 'time_start', 'time_end', 'status',
                    'overview', 'note')
      
        widgets = {
            'time_start': DateTimePickerInput(),
            'time_end': DateTimePickerInput(),
        }
   



class SettingTestForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SettingTestForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {"class": "form-control"}
        # self.fields['description'].widget.attrs.update({'rows': '8'})
        # self.fields['assigned_to'].queryset = assigned_users
        # self.fields['assigned_to'].required = False
        # self.fields['teams'].required = False
        for key, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label


        
    class Meta:
        model = TestSetting
        fields = ('setting','settingvalue')
    
    