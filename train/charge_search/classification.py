from .models import *

def charge_classification(count_distance,charge):
    if count_distance <= 25:
        charge = charge[0].charge_25 
    elif count_distance > 25 and count_distance <= 50:
        charge = charge[0].charge_50
    elif count_distance > 50 and count_distance <= 75:
        charge = charge[0].charge_75 
    elif count_distance > 50 and count_distance <= 100:
        charge = charge[0].charge_100
    elif count_distance > 100 and count_distance <= 150:
        charge = charge[0].charge_150
    elif count_distance > 150 and count_distance <= 200:
        charge = charge[0].charge_200
    elif count_distance > 200 and count_distance <= 300:
        charge = charge[0].charge_300
    elif count_distance > 300 and count_distance <= 400:
        charge = charge[0].charge_400
    elif count_distance > 400 and count_distance <= 600:
        charge = charge[0].charge_600
    elif count_distance > 600 and count_distance <= 700:
        charge = charge[0].charge_700
    elif count_distance > 700 and count_distance <= 800:
        charge = charge[0].charge_800
    elif count_distance > 800:
        charge = charge[0].charge_over801
    return charge


def fare_classification(count_distance,fare):
    if count_distance <= 3:
        fare = fare[0].fare_3
    elif count_distance > 3 and count_distance <= 6:
        fare = fare[0].fare_6
    else:
        j=10
        while j<=3000:
            while j<=45:
                order = "fare[0].fare_"+str(j)
                if count_distance <= j:
                    fare = eval(order)
                    return fare
                j += 5

            while j<=90:
                order = "fare[0].fare_"+str(j)
                if count_distance <= j:
                    fare = eval(order)
                    return fare
                j += 10

            while j<=580:
                order = "fare[0].fare_"+str(j)
                if count_distance <= j:
                    fare = eval(order)
                    return fare
                j += 20

            while j<=3000:
                order = "fare[0].fare_"+str(j)
                if count_distance <= j:
                    fare = eval(order)
                    return fare
                j += 40
    return fare



