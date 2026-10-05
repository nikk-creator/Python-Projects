distance_mi=5
is_raining=False
has_bike=True
has_car=True
has_ride_share_app=False
if distance_mi==0:
    print("False")
elif distance_mi<=1:
    if is_raining==False:
        print("True")
    else:
        print("False")
elif distance_mi>1 and distance_mi<=6:
    if is_raining==True:
        if has_bike==False:
            print("False")
    elif is_raining==False:
        if has_bike==False:
            print("False")
        elif has_bike==True:
            print("True")
elif distance_mi>6:
    if has_car==True or has_ride_share_app==True:
            print("True")
    else:
        print("False")

