# import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))
# with문을 탈출하면서 자동으로 종료되기 때문에 close()가 필요없다

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("Python")
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())