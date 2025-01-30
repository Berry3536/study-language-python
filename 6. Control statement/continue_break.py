
absent = [2, 5]
no_book = [7]

for student in range(1, 11):
    if student in absent:
        continue    # skip student 2 and 5
    elif student in no_book:
        print("Get out {0}. no class today!!".format(student))
        break

    print("{0}, read the sentence please".format(student))