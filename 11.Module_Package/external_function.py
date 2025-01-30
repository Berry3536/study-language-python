# glob : 경로 내의 폴더 / 파일 목록 조회
# import glob
# print(glob.glob("*.py"))

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd())  # 현재 디렉토리 표시

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다")
    
# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))