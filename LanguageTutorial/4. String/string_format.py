print("a" + "b")
print("a", "b")

print("나는 %d살입니다" % 20)               # %d : 정수
print("나는 %s을 좋아해요" % "python")      # %s : 문자열
print("Apple은 %c로 시작해요" % "A")        # %c : 문자

print("나는 %s색과 %s색을 좋아해요" %("파란", "빨간"))

print("나는 {}살입니다" .format(20))
print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아해요" .format(age = 20, color = "빨간"))