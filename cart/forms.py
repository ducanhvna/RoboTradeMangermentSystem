from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


class CartAddSettingForm(forms.Form):
    settingvalue = forms.CharField(max_length=100)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super(CartAddSettingForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {"class": "form-control"}
        # self.fields['description'].widget.attrs.update({'rows': '8'})
        # self.fields['assigned_to'].queryset = assigned_users
        # self.fields['assigned_to'].required = False
        # self.fields['teams'].required = False
        # label là giá trị khi định nghĩa model  file.
