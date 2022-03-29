from .classification import *
from .calculation import *
from .forms import SearchForm
from .getdata import *
from .models import (
    JobanStationModel,
    TokaidoStationModel,
    BasicChargeModel,
    BasicFareModel,
)


def main(request, line):
    # (0)フォームから取得 ＆ バリデーション#########################################################
    form = SearchForm(request.POST)
    if not form.is_valid():
        raise

    # ①モデルから駅オブジェクトを取得##############################################################
    request_data = request.POST
    input_dep = request_data["input_dep"]
    input_arr = request_data["input_arr"]
    model_name = eval(line + "StationModel")
    dep_sta = model_name.objects.filter(sta_name=input_dep)[0]
    arr_sta = model_name.objects.filter(sta_name=input_arr)[0]

    # ②検索対象の距離を算出######################################################################
    dep_dis = dep_sta.distance
    arr_dis = arr_sta.distance
    real_distance = float(dep_dis) - float(arr_dis)
    real_distance = round(real_distance, 1)
    real_distance = natural_numbering(real_distance)

    # ③特定都区市内の判定########################################################################
    dep_city = ""
    arr_city = ""
    count_distance = real_distance
    city_key = [
        "[札]札幌市内",
        "[仙]仙台市内",
        "[浜]横浜市内",
        "[名]名古屋市内",
        "[京]京都市内",
        "[阪]大阪市内",
        "[神]神戸市内",
        "[広]広島市内",
        "[九]北九州市内",
        "[福]福岡市内",
    ]
    city_sta = ["札幌", "仙台", "横浜", "名古屋", "京都", "大阪", "神戸", "広島", "小倉", "博多"]
    i = 0

    if (
        dep_sta.city == "[区]東京都区内" or dep_sta.city == "[山]東京山手線内"
    ) and real_distance > 200:
        count_distance = (
            eval(line + "StationModel").objects.filter(sta_name="東京")[0].distance
        )
        count_distance = float(count_distance) - float(arr_sta.distance)
        dep_city = "[区]東京都区内"
    elif (
        arr_sta.city == "[区]東京都区内" or arr_sta.city == "[山]東京山手線内"
    ) and real_distance > 200:
        count_distance = (
            eval(line + "StationModel").objects.filter(sta_name="東京")[0].distance
        )
        count_distance = float(dep_sta.distance) - float(count_distance)
        arr_city = "[区]東京都区内"
    elif dep_sta.city == "[山]東京山手線内" and real_distance > 100:
        count_distance = (
            eval(line + "StationModel").objects.filter(sta_name="東京")[0].distance
        )
        count_distance = float(count_distance) - float(arr_sta.distance)
        dep_city = "[山]東京山手線内"
    elif arr_sta.city == "[山]東京山手線内" and real_distance > 100:
        count_distance = (
            eval(line + "StationModel").objects.filter(sta_name="東京")[0].distance
        )
        count_distance = float(dep_sta.distance) - float(count_distance)
        arr_city = "[山]東京山手線内"

    while i < len(city_key):
        if dep_sta.city == city_key[i] and real_distance > 200:
            count_distance = (
                eval(line + "StationModel")
                .objects.filter(sta_name=city_sta[i])[0]
                .distance
            )
            count_distance = float(count_distance) - float(arr_sta.distance)
            dep_city = dep_sta.city
            break
        elif arr_sta.city == city_key[i] and real_distance > 200:
            count_distance = (
                eval(line + "StationModel")
                .objects.filter(sta_name=city_sta[i])[0]
                .distance
            )
            count_distance = float(dep_sta.distance) - float(count_distance)
            arr_city = arr_sta.city
            break
        else:
            i += 1
    count_distance = natural_numbering(count_distance)
    count_distance = round(count_distance, 1)

    # ④運賃区分判定##############################################################################
    if dep_sta.specific_section == "山手線" and arr_sta.specific_section == "山手線":
        fare_obj = BasicFareModel.objects.filter(fare_type="電車特定区間(山手線)")
    elif (
        dep_sta.specific_section
        and arr_sta.specific_section == "東京"
        or dep_sta.specific_section
        and arr_sta.specific_section == "山手線"
    ):
        fare_obj = BasicFareModel.objects.filter(fare_type="電車特定区間(東京)")
    else:
        fare_obj = BasicFareModel.objects.filter(fare_type="幹線")

    # ⑤運賃算出#################################################################################
    fare = fare_classification(count_distance, fare_obj)
    # ⑥特急料金算出##############################################################################
    charge_data = get_charge(real_distance)
    charge_nr = charge_data[0]
    charge_gr = charge_data[1]

    # ⑦割引運賃の算出#############################################################################
    if count_distance > 100:
        student_fare = "{:,d}".format(price_rounding(fare, 0.8))
    else:
        student_fare = "―"
    shareholder_fare = price_rounding(fare, 0.6)
    shareholder_charge_nr = price_rounding(charge_nr, 0.6)
    shareholder_charge_gr = price_rounding(charge_gr, 0.6)

    # ⑧レスポンス生成#############################################################################

    response = {
        "dep_sta": dep_sta,
        "arr_sta": arr_sta,
        "real_distance": real_distance,
        "charge_nr": "{:,d}".format(charge_nr),
        "charge_gr": "{:,d}".format(charge_gr),
        "shareholder_charge_nr": "{:,d}".format(shareholder_charge_nr),
        "shareholder_charge_gr": "{:,d}".format(shareholder_charge_gr),
        "fare": "{:,d}".format(fare),
        "student_fare": (student_fare),
        "shareholder_fare": "{:,d}".format(shareholder_fare),
        "fare_type": fare_obj[0].fare_type,
        "dep_city": dep_city,
        "arr_city": arr_city,
    }

    return response
