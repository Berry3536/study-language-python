weather = input("what is weather today?: ")

if weather == "rain" or weather == 'snow':
    print("get your umbrella")
elif weather =="dust":
    print("get your mask on")
else:
    print("go outside freely")



temp = int(input("what is temperature today?: "))

if temp >= 30:
    print("Too hot. Stay home")
elif 10 <= temp and temp < 30:
    print("Hot. get your water when go outside")
elif 0 <= temp < 10:
    print("temperature outside is good.")
else:
    print("Too Colda")