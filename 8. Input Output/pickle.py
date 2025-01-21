import pickle

# pickle로 데이터를 파일에 저장하기
profile_file = open("profile.pickle", "wb") # pickle 사용을 위해선 반드시 binary 파일을 사용
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile 에 있는 정보를 profile_file에 저장
profile_file.close()

# pickle로 파일에서 데이터를 읽어오기
profile_file = open("profile.pickle", "rb") # pickle 사용을 위해선 반드시 binary 파일을 사용
profile_read = pickle.load(profile_file) # profile_file에 있는 정보를 profile_read에 저장
print(profile_read)
profile_file.close()