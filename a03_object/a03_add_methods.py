'''
Created on 2022. 8. 3.

@author: SIST
# __add__()메소드
1. 객체끼리 참조변수로 덧셈을 할 경우에 실행되는 메소드
2. 일반적으로 덧셈(+) 연산은 숫자나 문자열 등에만 작동하지만,
    __add__() 메소드를 작성해 놓으면 객체 사이의 덧셈 작업도 가능하다.

'''
class Rabbit:
    def __init__(self,shape):
        self.shape = shape
    def __add__(self, other):
        print("객체",self.shape+"와",other.shape+"가 친구가 되었습니다")
r1 = Rabbit("동글한 토끼")
r2 = Rabbit("새하얀 토끼")
r1 + r2 # +연산자를 통해서 __add__에서 처리하는 메소드를 호출하게 처리한다.
print()
# ex) Product클래스를 통해서 물건명과 가격을 설정하고, 물건1+물건2를 할 때,
##    물건 @@(가격), @@(가격)을 구매하여 총비용이 @@@원입니다. 출력되게 하세요.
class Product:
    def __init__(self,name, price):
        self.name = name
        self.price = price
    def __add__(self, other):
        print("물건", self.name,"(",self.price,"원)",other.name,
              "(",other.price,"원)을 구매하여", end="")
        print("총비용이", self.price+other.price,"원 입니다")        
p01 = Product("사과",1200)        
p02 = Product("바나나",4000)        
p01 + p02        
        
        
         








