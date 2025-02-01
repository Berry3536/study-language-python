def profile(name, age, language1, language2, language3, language4, language5):
    print("name : {0}\tage : {1}\t".format(name, age), end = " " )
    print(language1, language2, language3, language4, language5)


profile("Thor", 20, "Python", "Java", "C", "C++", "C#")
profile("Loki", 20, "Kotlin", "Swift", "", "", "")


def profile(name, age, *language):  # 가변인자 사용
    print("name : {0}\tage : {1}\t".format(name, age), end = " " )
    for lang in language:
        print(lang, end = " ")
    print()

profile("Thor", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("Loki", 20, "Kotlin", "Swift")