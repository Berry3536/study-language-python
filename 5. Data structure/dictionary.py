# Data structure 2: Dictionary

cabinet = {3:"Andy", 100:"Tom"}    # key:value
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(100))
print()

# print(cabinet[5])                   # Key error

print(cabinet.get(5))               # get: Key value X -> None
print(cabinet.get(5, "usable"))
print()

print(3 in cabinet)

str_cabinet = {"A-3":"Alpha", "B-2":"Beta"}
print(str_cabinet)
print(str_cabinet["A-3"])
print(str_cabinet["B-2"])
print()

del str_cabinet["A-3"]
print(str_cabinet)
print()

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())
print()

cabinet.clear()
print(cabinet)