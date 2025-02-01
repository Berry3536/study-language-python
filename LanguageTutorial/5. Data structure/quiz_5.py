from random import *

id_list = [1, 2, 3, 4, 5, 6, 7, 8 ,9 ,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

shuffle(id_list)

winner_chicken = sample(id_list, 1)
id_list.remove(winner_chicken[0])

winner_coffee = sample(id_list, 3)

print("-- 당첨자 발표 --")
print("치킨 당첨자: ", winner_chicken[0])
print("커피 당첨자: ", winner_coffee)
print("-- 축하합니다 --")

# users = range(1, 21)
# print(users, type(users))

# users = list(users)
# print(users, type(users))