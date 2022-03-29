import math

# 割引計算・端数処理関数
# **%引の計算を行う関数
# 端数は10円未満を切り捨てで処理する。
def price_rounding(num,percentage):
    price = int(math.floor(num /10 * percentage)*10)
    return price

# 負→正変換関数
# 営業キロ算出する際に負の値になった場合は正の値に変換する
def natural_numbering(num_bef):
    if num_bef < 0:
        num_aft = num_bef *- 1
        return num_aft
    else:
        return num_bef
        