from django.contrib import admin

from .models import *

admin.site.register(VehicleModel)
admin.site.register(EngineModel)
admin.site.register(TransmissionModel)
admin.site.register(DriveAxleModel)
admin.site.register(SteerableAxleModel)
admin.site.register(ServiceCompany)
admin.site.register(TypeService)
admin.site.register(NodeRejection)
admin.site.register(SpareParts)
admin.site.register(Car)
admin.site.register(Service)
admin.site.register(Claims)
