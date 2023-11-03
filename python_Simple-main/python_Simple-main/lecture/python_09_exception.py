# 예외 처리
# ** 예외(exception)
#  - 프로그램을 개발하면서 예상하지 못한 상황
#    ex) 사용자 입력 오류
#  - 예외처리를 사용하면 ;프로그램이 종료x
#    입력 오류 -> 프로그램 종료(Error)
#    입력 오류 -> 예외 처리 -> 프로그램 종료 x
#  - 데이터베이스 또는 파일 시스템 사용할 때는 반드시 예외 처리!!

# ** 예외 종류
# 1. 예측 가능한 예외
#   - 발생 여부를 개발자가 사전에 인지
# 2. 예측 불가능한 예외
#   - 서버에서 데이터 받기(서버 화재 발생으로 서버 종류)

# ** 예외 기본 문법
#  try:
#    예외가 발생할 수도 있는 코드
#  except 예외 타입:
#  elxe:
#     예외가 발생하지 않는 경우 실행되는 코드
#  finally:
#     무조건 실행되는 코드(예외 발생 여부 상관 없음)
#     (대부분 자원 해제에 사용)
# 자원 해제: Connect 끊기!
# 가정: 종합 정보 시스템(동시 접속 2000명)
#     - 학생1 <-> 종합 정보 시스템(Connected)
#     - 학생 2 <-> 종합 정보 시스템(Connected)
#


# 정상: try -> else -> finally
# 예외: try -> except -> finally
# try~except 한 쌍
# else, finally 생략 가능

from urllib.request import urlopen, HTTPError

try:
    html = urlopen("http://www.javer.com")
except HTTPError as e:
    print(e)
else:    #잘 안씀
    print("No Error")
finally:
    print("자원해제")