customer = "thor"
index = 5

while index >= 1:
    print("{0}, coffee is ready. Your chance left is only {1} time".format(customer, index))
    index -= 1

    if index == 0:
        print("coffee has been discarded")