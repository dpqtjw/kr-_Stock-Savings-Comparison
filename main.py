#주식과 저축 금리의 차이
#날자와 기간은 yyyymmdd로 설정

from datetime import datetime
from pykrx import stock
from pykrx import bond
#한국 주식 크롤링 하는 모듈

class 기준금리:
    def __init__(self):
        self.금리_구간 = []  
        # (금리, 시작날짜, 종료날짜) 저장 리스트

        self.금리_구간.append((0.03, datetime.strptime('20230101', '%Y%m%d'), datetime.strptime('20231231', '%Y%m%d')))
        self.금리_구간.append((0.035, datetime.strptime('20240101', '%Y%m%d'), datetime.strptime('20251231', '%Y%m%d')))
    
    def 금리_조회(self, 기준날짜):
        기준날짜 = datetime.strptime(기준날짜, '%Y%m%d')
        적용금리 = [
            (금리, 시작날짜, 종료날짜) for 금리, 시작날짜, 종료날짜 in self.금리_구간
            if 시작날짜 <= 기준날짜 <= 종료날짜
        ]
        return 적용금리


class 복리계산기:
    def __init__(self, 초기원금, 기준금리_객체, 회전수=1.0):
        self.초기원금 = 초기원금
        self.기준금리_객체 = 기준금리_객체
        self.회전수 = 회전수
    
    def 총액_계산(self, 시작날짜, 종료날짜):
        총액 = self.초기원금
        시작날짜 = datetime.strptime(시작날짜, '%Y%m%d')
        종료날짜 = datetime.strptime(종료날짜, '%Y%m%d')

        # 금리 구간을 순회하며 적용
        현재날짜 = 시작날짜
        while 현재날짜 <= 종료날짜:
            적용금리 = self.기준금리_객체.금리_조회(현재날짜.strftime('%Y%m%d'))
            if 적용금리:
                금리, 구간시작, 구간종료 = 적용금리[0]
                구간종료 = min(구간종료, 종료날짜)
                구간기간 = (구간종료 - 현재날짜).days / 365.0  # 구간 기간(연 단위)
                총액 *= (1 + 금리 / self.회전수) ** (self.회전수 * 구간기간)
                현재날짜 = 구간종료 + datetime.timedelta(days=1)  # 다음 날로 이동
            else:
                raise ValueError("해당 날짜에 적용 가능한 금리가 없습니다.")
        return 총액

        
    
#int main(){}
초기원금 = 0
시작날짜 = datetime.datetime
종료날짜 = datetime.datetime
종목코드 =0

초기원금 = input("초기 원금을 입력하세요")
시작날짜, 종료날짜 = input("기간을 입력하세요(형식은 yyyymmdd)")
종목코드 = input("종목코드를 입력하세요")

날짜차이 = 종료날짜 - 시작날짜

회전수 = 날짜차이.days / 365

기준금리_객체 = 기준금리().금리_구간

계산기 = 복리계산기(초기원금, 기준금리_객체=기준금리_객체, 회전수)  # 분기 복리

# 계산
최종금액 = 계산기.총액_계산(시작날짜, 종료날짜)
print(f"최종 금액: {최종금액:.2f}원")