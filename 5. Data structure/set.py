# Data structure 4: set
# 중복 불가능, 순서 없음

my_set = {1, 2, 3, 3 ,3}
print(my_set)
print()

a_team = {"a-1", "a-2", "a-3"}
b_team = {"a-1", "b-2", "b-3"}

# 교집합
print(a_team & b_team)
print(a_team.intersection(b_team))
print()

# 합집합
print(a_team | b_team)
print(a_team.union(b_team))
print()

# 차집합
print(a_team - b_team)
print(a_team.difference(b_team))
print()

# 추가, 삭제
a_team.add("a-99")
b_team.remove("b-2")
print(a_team)
print(b_team)