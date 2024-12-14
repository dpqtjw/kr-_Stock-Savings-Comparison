#pykrx test
from datetime import datetime
from pykrx import stock
from pykrx import bond



class 주가계산:
    def __init__(self, 시작날짜, 종료날짜,종목코드):
        시작날짜 = datetime.strptime(시작날짜, '%Y%m%d')
        시작날짜계산 = datetime.strptime(시작날짜계산, '%Y%m%d')
        종료날짜 = datetime.strptime(종료날짜, '%Y%m%d')
        종료날짜계산 = datetime.strptime(종료날짜계산, '%Y%m%d')
        
        시작날짜계산 = 시작날짜 + datetime.timedelta(days=1)

        if(종료날짜 == datetime.datetime.now()):
            종료날짜계산 = 종료날짜 + datetime.timedelta(days=1)
        else
            종료날짜계산 = 종료날짜
            종료날짜 = 종료날짜계산 - datetime.timedelta(days=1)
        dfStart = stock.get_market_ohlcv(시작날짜, 시작날짜계산, 종목코드)
        dfEnd = stock.get_market_ohlcv(종료날짜, 종료날짜계산, 종목코드)

    def 종가차이계산(self,시작날짜종가,종료날짜종가):
        
        





초기원금 = 0
시작날짜 = datetime.datetime
종료날짜 = datetime.datetime
종목코드 =0

초기원금 = input("초기 원금을 입력하세요")
시작날짜, 종료날짜 = input("기간을 입력하세요(형식은 yyyymmdd)")
종목코드 = input("종목코드를 입력하세요")

주가계산기 = 주가계산(초기원금,시작날짜,종료날짜)  # 분기 복리

# 계산
최종금액 = 계산기.총액_계산(시작날짜, 종료날짜)
print(f"최종 금액: {최종금액:.2f}원")