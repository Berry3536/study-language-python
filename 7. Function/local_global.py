gun = 10

def checkpoint(soilders):
    global gun # use global variable : gun
    gun = gun - soilders
    print("[in function]Left gun : {0}".format(gun))

def checkpoint_return(gun, soilders):
    gun = gun - soilders
    return gun

print("Total gun : {0}".format(gun))
# checkpoint(2)
gun = checkpoint_return(gun, 2)
print("Left gun : {0}".format(gun))