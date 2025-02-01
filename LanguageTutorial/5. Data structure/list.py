# Data structure 1: List

subway = [10, 20 ,30]
bus = ["Tom", "Andy", "Stacy"]

print(subway)
print(subway[0])
print(subway[1])
print(subway[2])

print(bus)
print(bus[0])
print(bus[1])
print(bus[2])

print(bus.index("Stacy"))
print(bus.index("Andy"))
print(bus.index("Tom"))

# 추가 함수 - append
bus.append("New person")
print(bus)

# 추가 함수 - insert
bus.insert(1, "New person2")
print(bus)

# 제거 함수 - pop
print(bus.pop())
print(bus)
# print(bus.pop())
# print(bus)
# print(bus.pop())
# print(bus)

# 요소 개수 세기 - count
bus.append("Andy")
print(bus)
print(bus.count("Andy"))

# 정렬 함수 - sort
num_list = [5, 2, 4, 3, 1]
print(num_list)

num_list.sort()
print(num_list)
 
num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)


# 다양한 자료형 함께 사용 가능
mix_list = ["Andy", 20, True]
print(mix_list)


# 리스트 병합 - extend
subway.extend(mix_list)
print(subway)