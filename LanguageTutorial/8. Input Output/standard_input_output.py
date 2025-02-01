# import sys

# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)


# print("Python", "Java", "JavaScript", sep=" vs ")


# print("Python", "Java", "JavaScript", sep=",", end="?")
# print("무엇이 더 재밌을까요?")

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")
print()


for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(4))


# 표준 입력 -> input 함수는 항상 문자열 형태로 입력됨
answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 {0} 입니다".format(answer))