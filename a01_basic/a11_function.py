'''
Created on 2022. 8. 2.

@author: 전장호

# 함수
1. 무엇을 넣으면 그것이 처리되어 다시 어떤 것을 돌려주는 기능을
2. 파이썬 함수의 기본 형식
    def 함수명(매개변수1, 매개변수2) : 
        처리프로세스
        return 리턴할데이터
'''
def plus(num01, num02) :
    print("# 합산 기능 처리 함수 #")
    print("매개변수1 : ", num01)
    print("매개변수2 : ", num02)
    # 프로세스 처리
    sum = num01 + num02
    print("결과값(매개변수1 + 매개변수2) : ", sum)
    return sum
sum01 = plus(10, 20)
sum02 = plus(20, 30)
sum03 = plus(40, 50)

# ex) buyProduct를 통해 매개변수에 물건명, 가격, 개수를 입력받고
#        해당 정보를 출력하고, 총계를 리턴 처리하는 함수를 선언하고,
#        구매정보 3개를 입력하고 리턴한 결과를 출력하세요.
def buyProduct(pname, price, cnt) : 
    print("# 물건 구매 함수 #")
    print("물건명 :", pname)
    print("물건가격 :", price)
    print("물건개수 :", cnt)
    tot = price * cnt
    print(pname, "의 총계 : ", tot)
    return tot
tot01 = buyProduct("사과", 2000, 3)
tot02 = buyProduct("바나나", 3000, 5)
print("구매1 총계 : ", tot01)
print("구매2 총계 : ", tot02)
