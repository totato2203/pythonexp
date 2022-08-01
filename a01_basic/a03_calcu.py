'''
Created on 2022. 7. 5.

@author: 전장호

# 파이썬 특징 연산자
1. / : 소수점 이하까지 표현
2. // : 소수점 이하 절삭
3. ** : 변수의 제곱처리

'''

num01 = 10
num02 = 3
print(num01/num02)
print(num01//num02)
print(num01**num02)

# ex) 곰돌이 3마리가 빵 20개를 동일하게 배분하여 먹은 빵의 개수와
#    남은 빵의 개수를 변수와 연산자를 통해서 출력하세요.
bread = 20
bear = 3
print("동일 배분 빵 개수 :", bread//bear)
print("남은 빵 개수 :", bread%bear)

'''
# 비교 연산자
1. 어떤 것이 큰지, 작은지, 같은지를 비교하는 연산자
    ==, !=, <, >, ...
# 논리 연산자
1. 비교 연산자가 여러 번 필요할 때 사용
2 . and, or, not(비교 또는 논리 연산)
    ex) 나이가 10 이상 18 미만 청소년 요금제 적용
'''

# ex) 구매가격과 개수를 입력받아 1000000 이사이면 MVP 고객이다.
#    MVP 고객 (True/False) 여부를 출력하세요.
buyPrice = int(input("구매가격 :"))
buyCnt = int(input("구매가격 :"))
tot = buyPrice*buyCnt
print("총비용 :", tot)
print("MVP 여부 :", tot>=1000000)