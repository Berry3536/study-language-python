# 자료구조의 변경

menu = {"coffee", "milk", "juice"}

print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))