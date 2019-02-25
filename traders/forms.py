from django import forms


from bootstrap_datepicker_plus import   DateTimePickerInput
from .models import Trader
from robos.models import Setting

class TraderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TraderForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {"class": "form-control"}
        # self.fields['description'].widget.attrs.update({'rows': '8'})
        # self.fields['assigned_to'].queryset = assigned_users
        # self.fields['assigned_to'].required = False
        # self.fields['account'].widget.attrs['readonly'] = True
        self.fields['account'].widget.attrs['disabled'] = True
        for key, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label

        # assign account

        # self.fields['account']. = a

    # account = forms.CharField(max_length=100, disabled=True)
        
    class Meta:
        model = Trader
        fields = ('name', 'time_start', 'time_end', 
                    'overview', 'note', 'account')
      
        widgets = {
            'time_start': DateTimePickerInput(),
            'time_end': DateTimePickerInput(),
        }
   



