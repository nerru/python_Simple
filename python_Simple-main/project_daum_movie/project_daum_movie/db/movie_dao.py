from db.common.connection import connection


# 리뷰 저장
def add_review(data):
    # 1.Connection
    conn = connection()

    try:
        # 2. 일꾼 생성
        curs = conn.cursor()
        # 3. JoB 생성(SQL) -> INSERT, DELETE, UPDATE, SELECT
        sql = """
                INSERT INTO tbl_review(title, review, score, writer, reg_date)
                VALUES(%(title)s, %(review)s, %(score)s, %(writer)s, %(reg_date)s)
              """
        # 4. 작업 시작
        curs.execute(sql, data)
    except Exception as e:
        print(e)
    finally:
        # 5. 자원 해제
        conn.close()

def get_last_review():
    conn = connection()

    try:
        curs = conn.cursor()
        sql = """
               SELECT *
                FROM (
                    SELECT DATE_FORMAT(STR_TO_DATE(reg_date, '%Y. %m. %d. %H:%i'), '%Y%m%d%H%i') AS int_regdate FROM tbl_review
                    ORDER BY reg_date
                ) EX1
                ORDER BY int_regdate DESC LIMIT 1;
             """
        curs.execute(sql)
        # INSERT, DELETE, UPDATE -> 동작(Check)
        # SELECT -> DB로부터 데이터 받기(dict type)
        #  - 단건: fetchone()
        #  - 복수건: fetchall()
        result = curs.fetchone()
        return result
    except Exception as e:
        print(e)
    finally:
        conn.close()

def get_reviews():
    conn = connection()

    try:
        curs = conn.cursor()
        sql = """
                 SELECT * FROM tbl_review
              """
        curs.execute(sql)
        return curs.fetchall()
    except Exception as e:
        print(e)
    finally:
        conn.close()