#문자열의 이해(string)
# 활용 예: 데이터 분석, 자연어 처리 응용
#         사용자로부터 값 입력받을 때 처리용도
#
# 1.문자열 인덱스(index)
# - 문자열은 각 문자마다 순서(인덱스)가 있음
# - 첫번째 문자부터 마지막 문자까지 순차적으로 인덱스
# -인덱스 시작은 0
# -인덱스는 공백 포함
print("="*100)
print("Python")

# 2.문자 추출
# - 인덱스를 통해서 문자 추출
# - 인덱스 범위 벗어난 경우 오류)
#   (Error: index out of range)
lang = "Python"
print(lang[0])
print(lang[2])
#print(lang[9]) #Error

# -1 인덱스(Reverse Index)
# - 우측에서 좌측으로 인덱스
# - 시작값 -1

#3. 문자열 슬라이싱
# - lang[3]: 문자 1개만 추출
# - 부분 문자열 추출하고 싶은 경우
# - 시작인덱스, 끝인덱스 필요
msg = "Python is all you need"
print(msg[0:6])  #끝인덱스 +1
print(msg[:6])   # 시작 인덱스 생략 -> 자동 0입력
print(msg[3:])   # 끝 인덱스 생략 -> 자동 -1 입력
print(msg[:])    # 처음부터 끝까지

# 프로그래밍 언어 프로그래밍 언어 1개는 마스터
#   - 여러분들이 아이디어가 떠올랐을 때
#      바로 구현은 못하지만 구글링해서 어떻게
#      어떻게하면 만들 수 있겠네라는 생각이 들 정도

#개발자: 웹 개발자(프론트엔드, 백엔드)
#-앱 개발자(Android, ios)
#-웹 퍼블리셔
#-웹 디자이너
#-인공지능 개발자
#-....
# 서버 엔지니어

#quiz
print(msg[18:])
print(msg[:])
print(msg[-4:])

#주혁이가 쏘아올린 공

# 4.문자열 함수
str = "Hello World"
print("="*100)
# 4-1. len() : 문자열 길이 계산
print(len(str))

#4-2. upper() and lower() : 대소문자 변경
# -ID = "ChoLong02" -> "cholong02".lower()
# - epdlxj wjscjfl -> 1A, 1a-> upper() 1A 통일
print(str.upper())
print(str.lower())

# 4-3 replace() : 문자열 내의 특정 문자 치환
print(str.replace("H", "J"))

# 4-4 split() : 구분자를 기준으로 문자열 분할(Default: 공백)
b="Hello world what a nice weather"
print(b.split())
print(b.split("w"))

# 4-5 strip() : 문자열의 좌우공백 제거
id= "                                               python1004          "
print(id)
print(id.strip())

#id="        cholong1004       "
#id.lower() "     cholong1004    "
print(id.lower().strip())   #"cholong1004

# 4-6. find() and rfind() : 문자열 내부의 특정 문자 위치 인덱스 출력
print(str.find("o"))  #hell^o^ world
print(str.rfind("o")) #Hello W^o^rld
print(str.find("world"))  # 못 찾으면 -1 출력
print(str.find("World"))  # 단어의 첫 글자 인덱스
print(str.rfind("World")) # 단어의 첫 글자 인덱스

#4-7. in() : 특정 문자열 포함하는지 확인(True, False 출력)
print("Hi" in "Hi Python")

#문제
#    "abc123@gmail.com"
#    "ter@naver.com

id = "cherry1004@gmail.com"
val = id[:10]
print(val) #cherry1004

a = "abc123@gmail.com"
ax=a.find("@")
val=a[:ax]
print()

#  "www.googole.com"
#  "www.naver.com"
url= "www. naver.com"
start = url.find(".")+1
end = url.rfind(".")
val = url[start:end]
print(val)

