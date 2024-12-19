from django import forms
from .models import Membership, Package

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['name', 'phone', 'start_date', 'package']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['package'].queryset = Package.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        package = cleaned_data.get('package')
        if package:
            cleaned_data['price'] = package.price
        return cleaned_data