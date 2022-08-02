'''
Created on 2022. 8. 2.

@author: 전장호

# 지역변수와 전역변수의 이해
1. 유효범위
    자신이 활동할 수 있는 범위
    함수1 - 지연변수1, 지역변수2
    함수2 - 지역변수3, 지역변수4
    전역변수1
2. 지역변수 : 한정된 지역(local)에서만 사용되는 변수
    생존 범위 : 위의 예시로 지역변수1, 지역변수2는
        함수1에서 사용되고 함수2에서는 사용되지 못한다.
3. 전역변수 : 프로그램 전체(global)에서 사용되는 변수
    생존 범위 : 위의 예시로 전역변수1은 함수1과 함수2에서
        모두 사용할 수 있다.
4. 지역변수와 전역변수의 이름이 같은 경우
    1) 지역변수가 우선됨
    2) 위 유효범위내용 함수1은 전역변수와 지역변수로 동일변수1이 있을 때,
        지역변수에 있는 동일변수1을 호출하여 사용한다.
    3) 함수2는 해당 함수 내에 동일변수1이 없기 때문에
        전역변수에 있는 동일변수 1을 호출하여 사용한다.
'''
gloVar01 = 10
commVar02 = 20
def fun01() : 
    locVar03 = 30
    locVar04 = 40
    print("지역변수03 호출 : ", locVar03)
    print("전역변수01 호출 : ", gloVar01)
    # print("외부함수 지역변수 호출 : ", locVar05)
    print("공통변수02 호출 : ", commVar02)
def fun02() : 
    locVar05 = 50
    commVar02 = 60
    print("지역변수05 호출 : ", locVar05)
    print("공통변수02 호출 : ", commVar02)
fun01()
fun02()
print("전역변수 호출 : ", gloVar01)
# print("지역변수 호출 : ", locVar03)

# ex) 회사이름과 공통부서명을 전역변수로 선언하고,
#    part01(), part02()에서 각각의 부서명을 선언하여 회사이름과 부서명을 호출하되
#    part02()에서는 공통부서명과 동일한 변수로 부서명을 다르게 선언했으 때 처리되는 데이터를 출력하세요.
corpName = "A회사"
dept01 = "영업부"
def part01() :
    dept02 = "기획부"
    dept03 = "홍보부"
    print("부서02 : ", dept02)
    print("부서03 : ", dept03)
def part02() :
    dept04 = "재정부"
    dept01 = "인사부"
    print("부서04 : ", dept04)
    print("부서01 : ", dept01)
part01()
part02()
print("전역변수 호출 : ", corpName)

'''
# global 예약어
1. 함수 안에서 사용되는 변수로 지역변수 대신에 무조건 전역변수로
    사용하고 싶은 경우에 사용하는 예약어
2. global 예약어와 함께 나오는 변수명은 무조건 전역변수이다.
'''
def func01() : 
    global num01
    num01 = 10
    print("함수01의 num01 : ", num01)
def func02()  :
    print("함수02의 num02 : ", num01)
num01 = 20
func01()
func02()
print(num01)
num01 = 20
print(num01)

# ex) buy01(), buy02()를 통해 price01, price02를 물건값으로 구매했을 때,
#        해당 물건의 구매가격을 출력하고 buy01()에서 global 키워드를 이용해서
#        전역변수를 선언하고, 총비용을 누적해서 buy02()로 출력하세요.
def buy01() : 
    global price01
    price01 = 1000
def buy02() : 
    price02 = 2000
    sum = price01 + price02
    print("두 물건의 총비용 : ", sum)
buy01()
buy02()