personal_code = "990120-1234567"

print("sex : ", personal_code[7])            # 1
print("birth year : ", personal_code[0:2])   # 99
print("birth month : ", personal_code[2:4])  # 01
print("birth date : ", personal_code[4:6])   # 20

print("first section: ", personal_code[0:6])    # 990120
print("first section: ", personal_code[:6])     # 990120
print("second section: ", personal_code[7:])    # 1234567
print("second section: ", personal_code[-7:])   # 1234567