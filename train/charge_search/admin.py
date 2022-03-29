from django.contrib import admin
from .models import JobanStationModel,BasicChargeModel,BasicFareModel,TokaidoStationModel # models.pyで指定したクラス名

admin.site.register(BasicChargeModel) 
admin.site.register(BasicFareModel)


admin.site.register(JobanStationModel) 
admin.site.register(TokaidoStationModel) 