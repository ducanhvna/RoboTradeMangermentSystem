from django import forms
from .models import Account


class AccountForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {"class": "form-control"}
        # self.fields['description'].widget.attrs.update({'rows': '8'})
        # self.fields['assigned_to'].queryset = assigned_users
        # self.fields['assigned_to'].required = False
        # self.fields['teams'].required = False
        # label là giá trị khi định nghĩa model  file.
        for key, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model = Account
        fields = ('name', 'deposit', 'description')
    