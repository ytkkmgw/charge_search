from .models import JobanStationModel,TokaidoStationModel,BasicChargeModel,BasicFareModel
from .classification import *


def get_charge(real_distance):
    charge_nra = BasicChargeModel.objects.filter(charge_type = "スワロー料金")
    charge_gra = BasicChargeModel.objects.filter(charge_type = "グリーン料金(東日本)")
    charge_nr = charge_classification(real_distance,charge_nra)
    charge_gr = charge_classification(real_distance,charge_gra)
    charge_gr += charge_nr-530
    return charge_nr,charge_gr
        
