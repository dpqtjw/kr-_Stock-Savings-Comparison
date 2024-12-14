from datetime import datetime, timedelta
from pykrx import stock

class 기준금리:
    def __init__(self):
        self.금리_구간 = []  
        # (금리, 시작날짜, 종료날짜) 저장 리스트

        self.금리_구간.extend([
            (0.03, datetime.strptime('20241128', '%Y%m%d'), datetime.strptime('99991231', '%Y%m%d')),
            (0.0325, datetime.strptime('20241011', '%Y%m%d'), datetime.strptime('20241128', '%Y%m%d')),
            (0.035, datetime.strptime('20230113', '%Y%m%d'), datetime.strptime('20241011', '%Y%m%d')),
            (0.0325, datetime.strptime('20221124', '%Y%m%d'), datetime.strptime('20230113', '%Y%m%d')),
            (0.03, datetime.strptime('20221012', '%Y%m%d'), datetime.strptime('20221124', '%Y%m%d')),
            (0.025, datetime.strptime('20220825', '%Y%m%d'), datetime.strptime('20221012', '%Y%m%d')),
            (0.0225, datetime.strptime('20220713', '%Y%m%d'), datetime.strptime('20220825', '%Y%m%d')),
            (0.0175, datetime.strptime('20220526', '%Y%m%d'), datetime.strptime('20220713', '%Y%m%d')),
            (0.015, datetime.strptime('20220414', '%Y%m%d'), datetime.strptime('20220526', '%Y%m%d')),
            (0.0125, datetime.strptime('20220114', '%Y%m%d'), datetime.strptime('20220414', '%Y%m%d')),
            (0.01, datetime.strptime('20211125', '%Y%m%d'), datetime.strptime('20220114', '%Y%m%d')),
            (0.0075, datetime.strptime('20210826', '%Y%m%d'), datetime.strptime('20211125', '%Y%m%d')),
            (0.005, datetime.strptime('20200528', '%Y%m%d'), datetime.strptime('20210826', '%Y%m%d')),
            (0.0075, datetime.strptime('20200317', '%Y%m%d'), datetime.strptime('20200528', '%Y%m%d')),
            (0.0125, datetime.strptime('20191016', '%Y%m%d'), datetime.strptime('20200317', '%Y%m%d')),
            (0.015, datetime.strptime('20190718', '%Y%m%d'), datetime.strptime('20191016', '%Y%m%d')),
            (0.0175, datetime.strptime('20181130', '%Y%m%d'), datetime.strptime('20190718', '%Y%m%d')),
            (0.015, datetime.strptime('20171130', '%Y%m%d'), datetime.strptime('20181130', '%Y%m%d')),
            (0.0125, datetime.strptime('20160609', '%Y%m%d'), datetime.strptime('20171130', '%Y%m%d')),
            (0.015, datetime.strptime('20150611', '%Y%m%d'), datetime.strptime('20160609', '%Y%m%d')),
            (0.0175, datetime.strptime('20150312', '%Y%m%d'), datetime.strptime('20150611', '%Y%m%d')),
            (0.02, datetime.strptime('20141015', '%Y%m%d'), datetime.strptime('20150312', '%Y%m%d')),
            (0.0225, datetime.strptime('20140814', '%Y%m%d'), datetime.strptime('20141015', '%Y%m%d')),
            (0.025, datetime.strptime('20130509', '%Y%m%d'), datetime.strptime('20140814', '%Y%m%d')),
            (0.0275, datetime.strptime('20121011', '%Y%m%d'), datetime.strptime('20130509', '%Y%m%d')),
            (0.03, datetime.strptime('20120712', '%Y%m%d'), datetime.strptime('20121011', '%Y%m%d')),
            (0.0325, datetime.strptime('20110610', '%Y%m%d'), datetime.strptime('20110610', '%Y%m%d')),
            (0.03, datetime.strptime('20110310', '%Y%m%d'), datetime.strptime('20110610', '%Y%m%d')),
            (0.0275, datetime.strptime('20110113', '%Y%m%d'), datetime.strptime('20110310', '%Y%m%d')),
            (0.025, datetime.strptime('20101116', '%Y%m%d'), datetime.strptime('20110113', '%Y%m%d')),
            (0.0225, datetime.strptime('20100709', '%Y%m%d'), datetime.strptime('20101116', '%Y%m%d')),
            (0.02, datetime.strptime('20090212', '%Y%m%d'), datetime.strptime('20100709', '%Y%m%d')),
            (0.025, datetime.strptime('20090109', '%Y%m%d'), datetime.strptime('20090212', '%Y%m%d')),
            (0.03, datetime.strptime('20081211', '%Y%m%d'), datetime.strptime('20090109', '%Y%m%d')),
            (0.04, datetime.strptime('20081107', '%Y%m%d'), datetime.strptime('20081211', '%Y%m%d')),
            (0.0425, datetime.strptime('20081027', '%Y%m%d'), datetime.strptime('20081107', '%Y%m%d')),
            (0.05, datetime.strptime('20081009', '%Y%m%d'), datetime.strptime('20081027', '%Y%m%d')),
            (0.0525, datetime.strptime('20080807', '%Y%m%d'), datetime.strptime('20081009', '%Y%m%d')),
            (0.05, datetime.strptime('20070809', '%Y%m%d'), datetime.strptime('20080807', '%Y%m%d')),
            (0.0475, datetime.strptime('20070712', '%Y%m%d'), datetime.strptime('20070809', '%Y%m%d')),
            (0.045, datetime.strptime('20060810', '%Y%m%d'), datetime.strptime('20070712', '%Y%m%d')),
            (0.0425, datetime.strptime('20060608', '%Y%m%d'), datetime.strptime('20060810', '%Y%m%d')),
            (0.04, datetime.strptime('20060209', '%Y%m%d'), datetime.strptime('20060608', '%Y%m%d')),
            (0.0375, datetime.strptime('20051208', '%Y%m%d'), datetime.strptime('20060209', '%Y%m%d')),
            (0.035, datetime.strptime('20051011', '%Y%m%d'), datetime.strptime('20051208', '%Y%m%d')),
            (0.0325, datetime.strptime('20041111', '%Y%m%d'), datetime.strptime('20051011', '%Y%m%d')),
            (0.035, datetime.strptime('20040812', '%Y%m%d'), datetime.strptime('20041111', '%Y%m%d')),
            (0.0375, datetime.strptime('20030710', '%Y%m%d'), datetime.strptime('20040812', '%Y%m%d')),
            (0.04, datetime.strptime('20030513', '%Y%m%d'), datetime.strptime('20030710', '%Y%m%d')),
            (0.0425, datetime.strptime('20020507', '%Y%m%d'), datetime.strptime('20030513', '%Y%m%d')),
            (0.04, datetime.strptime('20010919', '%Y%m%d'), datetime.strptime('20020507', '%Y%m%d')),
            (0.045, datetime.strptime('20010809', '%Y%m%d'), datetime.strptime('20010919', '%Y%m%d')),
            (0.0475, datetime.strptime('20010705', '%Y%m%d'), datetime.strptime('20010809', '%Y%m%d')),
            (0.05, datetime.strptime('20010208', '%Y%m%d'), datetime.strptime('20010705', '%Y%m%d')),
            (0.0525, datetime.strptime('20001005', '%Y%m%d'), datetime.strptime('20010208', '%Y%m%d')),
            (0.05, datetime.strptime('20000210', '%Y%m%d'), datetime.strptime('20001005', '%Y%m%d')),
            (0.0475, datetime.strptime('19990506', '%Y%m%d'), datetime.strptime('19990506', '%Y%m%d')),
        ])
        #한국은행 기준 금리리
    
    def 금리_조회(self, 기준날짜):
        기준날짜 = datetime.strptime(기준날짜, '%Y%m%d')
        적용금리 = [
            (금리, 시작날짜, 종료날짜) for 금리, 시작날짜, 종료날짜 in self.금리_구간
            if 시작날짜 <= 기준날짜 <= 종료날짜
        ]
        return 적용금리
    #적용금리 계산


class 복리계산기:
    def __init__(self, 초기원금, 기준금리_객체, 회전수=1.0):
        self.초기원금 = 초기원금
        self.기준금리_객체 = 기준금리_객체
        self.회전수 = 회전수
    
    def 총액_계산(self, 시작날짜, 종료날짜):
        총액 = self.초기원금
        시작날짜 = datetime.strptime(시작날짜, '%Y%m%d')
        종료날짜 = datetime.strptime(종료날짜, '%Y%m%d')

        현재날짜 = 시작날짜
        while 현재날짜 <= 종료날짜:
            적용금리 = self.기준금리_객체.금리_조회(현재날짜.strftime('%Y%m%d'))
            if 적용금리:
                금리, 구간시작, 구간종료 = 적용금리[0]
                구간종료 = min(구간종료, 종료날짜)
                구간기간 = (구간종료 - 현재날짜).days / 365.0 
                총액 *= (1 + 금리 / self.회전수) ** (self.회전수 * 구간기간)
                현재날짜 = 구간종료 + timedelta(days=1) 
            else:
                raise ValueError("해당 날짜에 적용 가능한 금리가 없습니다.")
        return 총액
    
class 주가계산:
#pykrx를 이용한 주가 계산
    def __init__(self, 시작날짜, 종료날짜, 종목코드):
        시작날짜 = datetime.strptime(시작날짜, '%Y%m%d')
        종료날짜 = datetime.strptime(종료날짜, '%Y%m%d')

        시작날짜계산 = 시작날짜 + timedelta(days=1)
        종료날짜계산 = 종료날짜 + timedelta(days=1)
        # 시작 날짜와 종료 날짜의 다음 날을 계산
    
        dfStart = stock.get_market_ohlcv(시작날짜, 시작날짜계산, 종목코드)
        dfEnd = stock.get_market_ohlcv(종료날짜, 종료날짜계산, 종목코드)
        # 주가 데이터 가져오기

        self.시작날짜종가 = dfStart.iloc[0]['종가'] if not dfStart.empty else 0
        self.종료날짜종가 = dfEnd.iloc[0]['종가'] if not dfEnd.empty else 0
        # 종가 가져오기

    def 종가차이계산(self, 초기원금):
        기준 = self.시작날짜종가
        if 기준 == 0:
            raise ValueError("시작 날짜의 종가가 0입니다. 유효한 종목 코드를 입력하세요.")
        보유주식 = 초기원금 / 기준
        주식결산 = 보유주식 * self.종료날짜종가

        return 주식결산
    


#int main(){}
if __name__ == "__main__":
    초기원금 = float(input("초기 원금을 입력하세요: "))
    시작날짜 = input("시작 날짜를 입력하세요 (형식: yyyymmdd): ")
    종료날짜 = input("종료 날짜를 입력하세요 (형식: yyyymmdd): ")
    종목코드 = input("종목 코드를 입력하세요: ")

    시작날짜_dt = datetime.strptime(시작날짜, '%Y%m%d')
    종료날짜_dt = datetime.strptime(종료날짜, '%Y%m%d')
    날짜차이 = 종료날짜_dt - 시작날짜_dt

    회전수 = int(날짜차이.days) / 365

    기준금리객체 = 기준금리()

    계산기 = 복리계산기(초기원금, 기준금리객체 , 회전수=회전수)

    정기예금최종금액 = 계산기.총액_계산(시작날짜, 종료날짜)

    print(f"최종 금액: {정기예금최종금액:.2f}원")

#정기예금계산

    주가계산기 = 주가계산(시작날짜, 종료날짜, 종목코드)

    # 계산
    주식최종금액 = 주가계산기.종가차이계산(초기원금)
    print(f"최종 금액: {주식최종금액:.2f}원")

    if(주식최종금액<정기예금최종금액):
        print("주식하지 말껄")

    else:
        print("라고할때 넣을껄")