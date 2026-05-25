units = int(input("please enter numbver of units consumed"))

if (units<50):
   amount = units*2.60
   surcharge = 35

elif (units<=100):
   amount= 130+ ((units-50))*3.25
   surcharge = 45

elif (units<=200):
   amount= 130+162.5+((units-100))*5.26
   surcharge = 35
total = amount+surcharge
print("\nElectricity Bill")