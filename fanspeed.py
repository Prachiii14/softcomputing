def fan_speed(temp):
    if temp < 20:
	   return "slow"
	elif temp>=20 and temp <= 30:
	   return "medium"
	else:
	   return "fast"
	   
temp=float(input("enter temperature"))
print("fan speed:" fan_speed(temp))