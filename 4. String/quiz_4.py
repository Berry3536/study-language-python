url = "http://naver.com"
url = url.replace("http://", "")
url = url.replace(".com", "")

password = url[0:3] + str(len(url)) + str(url.count("e")) + "!"

print(password)