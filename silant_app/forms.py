from django import forms
from .models import *


class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['machine_serial_number',
                  'vehicle_model',
                  'engine_model',
                  'engine_serial_number',
                  'transmission_model',
                  'transmission_serial_number',
                  'drive_axle_model',
                  'drive_axle_serial_number',
                  'steerable_axle_model',
                  'steerable_axle_serial_number',
                  'delivery_contract',
                  'shipping_date',
                  'consignee',
                  'delivery_address',
                  'equipment',
                  'client',
                  'service_company',]
        

class AddServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['type_service',
                  'date_service',
                  'operating_time',
                  'work_order_number',
                  'work_order_date',
                  'organization',
                  'car',
                  'service_company',]
        

class AddClaimsForm(forms.ModelForm):
    class Meta:
        model = Claims
        fields = ['date_rejection',
                  'operating_time',
                  'node_rejection',
                  'description_rejection',
                  'recovery_method',
                  'spare_parts',
                  'date_recovery',
                  'machine_downtime',
                  'car',
                  'service_company',]
