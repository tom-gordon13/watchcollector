from django.forms import ModelForm
from .models import Servicing, Component

class ServicingForm(ModelForm):
    class Meta:
        model = Servicing
        fields = ['date', 'type', 'cost']

class ComponentForm(ModelForm):
    class Meta:
        model = Component
        fields = ['type_comp', 'subtype_comp']