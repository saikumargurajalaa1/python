cus_id=int(input("enter customer id"))
prev_unit=int(input("enter previous unit"))
curr_unit=int(input("enter current unit"))
usage_unit=curr_unit-prev_unit

if (usage_unit >= 0 and usage_unit <= 50):
    print("POWER BILL")
    print("customer id=",cus_id)
    print("previous unit=",prev_unit)
    print("current unit=",curr_unit)
    print("amount=free")
elif (usage_unit >= 51 and usage_unit <= 100):
    amt=usage_unit*2
    print("POWER BILL")
    print("customer id=", cus_id)
    print("previous unit=", prev_unit)
    print("current unit=", curr_unit)
    print("amount=",amt)
elif (usage_unit >= 101 and usage_unit <= 200):
    amt=usage_unit*3
    print("POWER BILL")
    print("customer id=", cus_id)
    print("previous unit=", prev_unit)
    print("current unit=", curr_unit)
    print("amount=",amt)
elif (usage_unit >= 201 and usage_unit <= 500):
    amt=usage_unit*4
    print("POWER BILL")
    print("customer id=", cus_id)
    print("previous unit=", prev_unit)
    print("current unit=", curr_unit)
    print("amount=",amt)