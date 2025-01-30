def std_weight(height, gender):
    if gender == "man":
        return height * height * 22
    elif gender == "woman":
        return height * height * 21
    
height = 175
gender = "man"
weight = round(std_weight(height / 100, gender), 2)

print("키 {0}cm {1}의 표준 체중은 {2} 입니다".format(height, gender, weight))