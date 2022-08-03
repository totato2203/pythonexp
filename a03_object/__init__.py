'''
# 객체지향 프로그래밍
1. 클래스와 객체
    1) 클래스의 생성
    2) 객체의 생성
2. 생성자와 특별 메소드
    1) 생성자 
        __init__()
    2) 특별메소드
        __del__()
        __add__()
3. 클래스와 상속
    1) 상속의 개념
    2) 상속의 구현
    
# 객체의 개념
1. 수많은 사물을 프로그래밍 관점에서 객체라고 부른다.
    자동차, 건물, 고양이, 물고기 등
2. 객체의 정의
    객체란 어떤 속성과 행동을 가지고 있는 데이터를 말한다.

# 클래스와 객체의 관계
1. 클래스
    1) 파이썬에서 제공하는 객체 외에 필요한 객체를 만들어서 사용할 수 있는데,
        객체를 만들기 위해서는 클래스가 필요하다.
    2) 객체를 만들기 위한 설계도 또는 찍어내는 틀을 의미한다.
2. 파이썬이 제공하지 않는 토끼 클래스 만들기
    1) 토끼 객체를 만들려면 먼저 또끼 클래스가 필요로 한다.
    2) 하지만 토끼 클래슨는 파이썬에서 제공하지 않는다.
        - 따라서 토끼 객체를 만들기 위해서는 우선 토끼 클래스를 만들어야 한다.
# 클래스를 만들기 위한 형식
1. class 클래스 이름:
    # 클래스 생성 코드 구현
2. 토끼 클래스에 필요한 속성과 행동
    1) 속성 : 토끼의 모양, x,y의 위치 ==> 변수로 생성
    2) 기능 : 이동하기() ==> 함수 (메소드)로 구현한다.
'''
class Rabbit:
    #토끼의 속성(변수)
    shape =""
    xPos = 0
    yPos = 0
    def go(self,x,y):
        self.xPos = x # self : 파이썬에서 현재 객체의 속성(필드/메서드)을 접근할 때 사용
        self.yPos = y # 자바의 this와 동일한 역할
        print("#토끼가 이동#")
        print("X좌표:",self.xPos)
        print("X좌표:",self.yPos)
rabbit1 = Rabbit()        
rabbit2 = Rabbit()        
rabbit3 = Rabbit()        
rabbit1.go(10,20)        
rabbit2.go(30,40)        
rabbit3.go(50,60) 
# ex) Person 클래스를 선언하고 속성 이름, 나이, 사는 곳, 
#  메서드로 showInfo(속성할당 파라미터)를 통해 속성을 출력 처리하는 기능을 처리해보세요..
class Person:
    name = ""
    age = 0
    loc = ""
    def showInfo(self, name, age, loc):
        self.name = name
        self.age = age
        self.loc = loc
        print("이름 :", self.name)
        print("나이 :", self.age)
        print("사는곳 :", self.loc)
p01 = Person()
p02 = Person()
p03 = Person()
p01.showInfo("홍길동", 25, "서울")
p02.showInfo("김길동", 27, "대전")
p03.showInfo("신길동", 23, "대구")





       



