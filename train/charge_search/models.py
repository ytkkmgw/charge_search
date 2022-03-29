from django.db import models


class JobanStationModel(models.Model):
    sta_name = models.CharField(null=True, blank=True, max_length=20)
    sta_name_hr = models.CharField(null=True, blank=True, max_length=30)
    distance = models.FloatField()
    city = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        choices=(
            ("[札]札幌市内", "札幌市内"),
            ("[仙]仙台市内", "仙台市内"),
            ("[区]東京都区内", "東京都区内"),
            ("[山]東京山手線内", "東京山手線内"),
            ("[浜]横浜市内", "横浜市内"),
            ("[名]名古屋市内", "名古屋市内"),
            ("[京]京都市内", "京都市内"),
            ("[阪]大阪市内", "大阪市内"),
            ("[神]神戸市内", "神戸市内"),
            ("[広]広島市内", "広島市内"),
            ("[九]北九州市内", "北九州市内"),
            ("[福]福岡市内", "福岡市内"),
        ),
    )
    specific_section = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        choices=(("東京", "東京"), ("山手線", "山手線"), ("大阪", "大阪"), ("大阪環状線", "大阪環状線")),
    )
    branch = models.CharField(null=True, blank=True, max_length=30)

    def __str__(self):
        return self.sta_name


class TokaidoStationModel(models.Model):
    sta_name = models.CharField(null=True, blank=True, max_length=20)
    sta_name_hr = models.CharField(null=True, blank=True, max_length=30)
    distance = models.FloatField()
    city = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        choices=(
            ("[札]札幌市内", "札幌市内"),
            ("[仙]仙台市内", "仙台市内"),
            ("[区]東京都区内", "東京都区内"),
            ("[山]東京山手線内", "東京山手線内"),
            ("[浜]横浜市内", "横浜市内"),
            ("[名]名古屋市内", "名古屋市内"),
            ("[京]京都市内", "京都市内"),
            ("[阪]大阪市内", "大阪市内"),
            ("[神]神戸市内", "神戸市内"),
            ("[広]広島市内", "広島市内"),
            ("[九]北九州市内", "北九州市内"),
            ("[福]福岡市内", "福岡市内"),
        ),
    )
    specific_section = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        choices=(("東京", "東京"), ("山手線", "山手線"), ("大阪", "大阪"), ("大阪環状線", "大阪環状線")),
    )
    branch = models.CharField(null=True, blank=True, max_length=30)

    def __str__(self):
        return self.sta_name


class BasicChargeModel(models.Model):
    charge_type = models.CharField(primary_key=True, max_length=20)
    charge_25 = models.IntegerField()
    charge_50 = models.IntegerField()
    charge_75 = models.IntegerField()
    charge_100 = models.IntegerField()
    charge_150 = models.IntegerField()
    charge_200 = models.IntegerField()
    charge_300 = models.IntegerField()
    charge_400 = models.IntegerField()
    charge_600 = models.IntegerField()
    charge_700 = models.IntegerField()
    charge_800 = models.IntegerField()
    charge_over801 = models.IntegerField()

    def __str__(self):
        return self.charge_type


class BasicFareModel(models.Model):
    fare_type = models.CharField(primary_key=True, max_length=20)
    fare_3 = models.IntegerField(null=True, blank=True)
    fare_6 = models.IntegerField(null=True, blank=True)
    fare_10 = models.IntegerField(null=True, blank=True)
    fare_15 = models.IntegerField(null=True, blank=True)
    fare_20 = models.IntegerField(null=True, blank=True)
    fare_25 = models.IntegerField(null=True, blank=True)
    fare_30 = models.IntegerField(null=True, blank=True)
    fare_35 = models.IntegerField(null=True, blank=True)
    fare_40 = models.IntegerField(null=True, blank=True)
    fare_45 = models.IntegerField(null=True, blank=True)
    fare_50 = models.IntegerField(null=True, blank=True)
    fare_60 = models.IntegerField(null=True, blank=True)
    fare_70 = models.IntegerField(null=True, blank=True)
    fare_80 = models.IntegerField(null=True, blank=True)
    fare_90 = models.IntegerField(null=True, blank=True)
    fare_100 = models.IntegerField(null=True, blank=True)
    fare_120 = models.IntegerField(null=True, blank=True)
    fare_140 = models.IntegerField(null=True, blank=True)
    fare_160 = models.IntegerField(null=True, blank=True)
    fare_180 = models.IntegerField(null=True, blank=True)
    fare_200 = models.IntegerField(null=True, blank=True)
    fare_220 = models.IntegerField(null=True, blank=True)
    fare_240 = models.IntegerField(null=True, blank=True)
    fare_260 = models.IntegerField(null=True, blank=True)
    fare_280 = models.IntegerField(null=True, blank=True)
    fare_300 = models.IntegerField(null=True, blank=True)
    fare_320 = models.IntegerField(null=True, blank=True)
    fare_340 = models.IntegerField(null=True, blank=True)
    fare_360 = models.IntegerField(null=True, blank=True)
    fare_380 = models.IntegerField(null=True, blank=True)
    fare_400 = models.IntegerField(null=True, blank=True)
    fare_420 = models.IntegerField(null=True, blank=True)
    fare_440 = models.IntegerField(null=True, blank=True)
    fare_460 = models.IntegerField(null=True, blank=True)
    fare_480 = models.IntegerField(null=True, blank=True)
    fare_500 = models.IntegerField(null=True, blank=True)
    fare_520 = models.IntegerField(null=True, blank=True)
    fare_540 = models.IntegerField(null=True, blank=True)
    fare_560 = models.IntegerField(null=True, blank=True)
    fare_580 = models.IntegerField(null=True, blank=True)
    fare_600 = models.IntegerField(null=True, blank=True)
    fare_640 = models.IntegerField(null=True, blank=True)
    fare_680 = models.IntegerField(null=True, blank=True)
    fare_720 = models.IntegerField(null=True, blank=True)
    fare_760 = models.IntegerField(null=True, blank=True)
    fare_800 = models.IntegerField(null=True, blank=True)
    fare_840 = models.IntegerField(null=True, blank=True)
    fare_880 = models.IntegerField(null=True, blank=True)
    fare_920 = models.IntegerField(null=True, blank=True)
    fare_960 = models.IntegerField(null=True, blank=True)
    fare_1000 = models.IntegerField(null=True, blank=True)
    fare_1040 = models.IntegerField(null=True, blank=True)
    fare_1080 = models.IntegerField(null=True, blank=True)
    fare_1120 = models.IntegerField(null=True, blank=True)
    fare_1160 = models.IntegerField(null=True, blank=True)
    fare_1200 = models.IntegerField(null=True, blank=True)
    fare_1240 = models.IntegerField(null=True, blank=True)
    fare_1280 = models.IntegerField(null=True, blank=True)
    fare_1320 = models.IntegerField(null=True, blank=True)
    fare_1360 = models.IntegerField(null=True, blank=True)
    fare_1400 = models.IntegerField(null=True, blank=True)
    fare_1440 = models.IntegerField(null=True, blank=True)
    fare_1480 = models.IntegerField(null=True, blank=True)
    fare_1520 = models.IntegerField(null=True, blank=True)
    fare_1560 = models.IntegerField(null=True, blank=True)
    fare_1600 = models.IntegerField(null=True, blank=True)
    fare_1640 = models.IntegerField(null=True, blank=True)
    fare_1680 = models.IntegerField(null=True, blank=True)
    fare_1720 = models.IntegerField(null=True, blank=True)
    fare_1760 = models.IntegerField(null=True, blank=True)
    fare_1800 = models.IntegerField(null=True, blank=True)
    fare_1840 = models.IntegerField(null=True, blank=True)
    fare_1880 = models.IntegerField(null=True, blank=True)
    fare_1920 = models.IntegerField(null=True, blank=True)
    fare_1960 = models.IntegerField(null=True, blank=True)
    fare_2000 = models.IntegerField(null=True, blank=True)
    fare_2040 = models.IntegerField(null=True, blank=True)
    fare_2080 = models.IntegerField(null=True, blank=True)
    fare_2120 = models.IntegerField(null=True, blank=True)
    fare_2160 = models.IntegerField(null=True, blank=True)
    fare_2200 = models.IntegerField(null=True, blank=True)
    fare_2240 = models.IntegerField(null=True, blank=True)
    fare_2280 = models.IntegerField(null=True, blank=True)
    fare_2320 = models.IntegerField(null=True, blank=True)
    fare_2360 = models.IntegerField(null=True, blank=True)
    fare_2400 = models.IntegerField(null=True, blank=True)
    fare_2440 = models.IntegerField(null=True, blank=True)
    fare_2480 = models.IntegerField(null=True, blank=True)
    fare_2520 = models.IntegerField(null=True, blank=True)
    fare_2560 = models.IntegerField(null=True, blank=True)
    fare_2600 = models.IntegerField(null=True, blank=True)
    fare_2640 = models.IntegerField(null=True, blank=True)
    fare_2680 = models.IntegerField(null=True, blank=True)
    fare_2720 = models.IntegerField(null=True, blank=True)
    fare_2760 = models.IntegerField(null=True, blank=True)
    fare_2800 = models.IntegerField(null=True, blank=True)
    fare_2840 = models.IntegerField(null=True, blank=True)
    fare_2880 = models.IntegerField(null=True, blank=True)
    fare_2920 = models.IntegerField(null=True, blank=True)
    fare_2960 = models.IntegerField(null=True, blank=True)
    fare_3000 = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.fare_type
