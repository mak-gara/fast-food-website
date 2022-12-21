from django.forms import modelform_factory, ModelForm
from django.forms.widgets import Select

from .models import PickUpOrder


# PickUpOrderForm = modelform_factory(
#     PickUpOrder,
#     fields='__all__',
#     labels={
#         'customer_name': 'Ім\'я',
#         'phone_number': 'Номер телефону',
#         'email': 'Електронна адреса'
#     },
#     help_texts={
#         'email': 'Формат: youremail@gmail.com'
#     },
#     error_messages={
#         'email': {
#             'invalid': 'Ви ввели некоректний Email'
#         }
#     },
#     widgets={'store': Select(attrs={'size':8})})

class PickUpOrderForm(ModelForm):
    class Meta:
        model = PickUpOrder
        fields = '__all__'
        labels={
            'customer_name': 'Ім\'я',
            'phone_number': 'Номер телефону',
            'email': 'Електронна адреса'
            }
        help_texts={
            'email': 'Формат: youremail@gmail.com'
        }
        
