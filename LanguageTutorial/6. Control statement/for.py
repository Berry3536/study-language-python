
for count in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(count))
print()
    
for count in range(5):  # 0, 1, 2, 3, 4
    print("대기번호 : {0}".format(count))
print()

for count in range(1, 6):  # 1, 2, 3, 4, 5
    print("대기번호 : {0}".format(count))
print()


starbucks = ["iron man", "thor", "captain america"]

for customer in starbucks:
    print("Customer name [{0}]. Your menu is ready.".format(customer))