# DAO: Database Access Object
#  - 데이터 작업(CRUD)을 하는 객체

# 예시)
# 회원 -> member_dao
#              ㄴ 회원 가입, 회원 수정, 회원 조회, 회원 검색, 회원 삭제

# 로그인 -> login_dao
#           ㄴ 로그인, 로그아웃, ID 찾기, PW 찾기

from db.common.connection import conn_mongodb

# 뉴스 (제목, 본문, 날짜) 저장
def add_news(data):
    conn = conn_mongodb()  # 1. Connctrion
    conn.insert_one(data) # 2. DB에 저장