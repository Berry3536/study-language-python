# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
print("{0:A>10}".format(500))

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))

# 3자리마다 콤마 찍기
print("{0:+,}".format(1000000000000))
print("{0:+,}".format(-1000000000000))

# 3자리마다 콤마를 찍고, 부호를 붙이고, 자릿수 확보, 빈자리는 ^로 채우기
print("{0:^<+30,}".format(1000000000000))

# 소수점 출력, 소수점 셋째 자리에서 반올림
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))