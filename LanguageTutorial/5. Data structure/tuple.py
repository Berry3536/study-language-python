# Data structure 3. tuple
# List, Dictionary와 다르게 변경 불가능

menu = ("bread", "soup")
print(menu[0])
print(menu[1])

name = "Andy"
age = 20
hobby = "coding"
print(name, age, hobby)

(name, age, hobby) = ("andy", 15, "running")
print(name, age, hobby)