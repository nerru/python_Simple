# TODO: 1. 스케줄링
#       3. DB에 저장 된 데이터 Excel 다운로드
#       4. DB에 저장 된 데이터  -> 텍스트 분석
#       5. DB에 저장 된 데이터  -> WorldCloud 시각화

from collect.collect_daum_movie_review import review_collector
from apscheduler.schedulers.blocking import BlockingScheduler
def main():
    print("="*100)
    print("== 영화 리뷰 수집기 ==")
    print("="*100)
    movie_code = input("영화 코드>>")  # 169328
    print("MSG: 매일 12시간에 수집")

    # 중복 리뷰 체크
    # 1. 리뷰수(x)
    #  - DB에 저장 된 리뷰 수(17)
    #  - 현재 수집 할 리뷰 수(20)
    #  20 - 17 = 3  리뷰 삭제 고려 X!
    # 2. 날짜 비교
    #  -last_date = DB에 저장 된 리뷰 중 가장 최신 날짜 get
    #  수집 리뷰_date 비교 last_date
    #  ex)last_date = 2023.11.27 02:25       202311270225
    #  ex)수집 리뷰_date = 2023.11.28. 02:25   202311280225



    scheduler = BlockingScheduler()
    scheduler.add_job(review_collector,
                      args=[movie_code],
                      trigger="cron",
                      hour="12",
                      minute="0")
    scheduler.start()
    

if __name__ =="__main__":
    main()