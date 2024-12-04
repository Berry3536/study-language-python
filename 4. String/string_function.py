string = "Python is Amazing"

print(string.lower())
print(string.upper())
print(string[0].isupper())
print(len(string))
print(string.replace("Python", "Java"))
print(string)

index = string.index("n")
print(index)
index = string.index("n", index + 1)
print(index)

print(string.find("Java"))  # 찾고자 하는 문자열이 탐색 문자열에 없을 경우, -1을 리턴

print(string.count("n"))