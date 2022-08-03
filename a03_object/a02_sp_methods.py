'''
Created on 2022. 8. 3.

@author: SIST

# 특별한 메서드
1. __del__() 메소드
    1) __init__()메소드가 생성자라면 __del__()메소드는 소멸자라고 부른다.
    2) __del__()는 객체가 제거될 때, 자동으로 호출된다.
        메모리에서 제거할 때, del로 지우는데, 이때 호출 된다.
'''
class Rabbit:
    def __init__(self):
        print("객체가 생성된다")
    def __del__(self):
        print("객체를 소멸한다.~~")
print("프로세스1")        
r1 = Rabbit() 
del(r1) # 명시적으로 객체의 메모리를 소멸 처리
print("프로세스2")        
r2 = Rabbit()        
print("프로세스3")        
# 프로그램이 끝나면 자동으로 소멸되고..
# ex) Fruit를 통해서 객체의 이름을 필드로 지정하고, 
#     생성자와 소멸자를 선언하면 해당 객체가 생성/소멸되게 처리하되, 명시적 소멸과
#     자동 소멸 되는 내용을 참조객체 3개를 통해 처리하세요.
class Fruit:
    def __init__(self, name):
        self.name = name
        print("과일:" +self.name+" 객체가 생성된다.")
    def __del__(self):
        print("과일:" +self.name+" 객체가 소멸된다.")
f1 = Fruit("사과")
print("#명시적 삭제#"); del(f1)
f2 = Fruit("바나나")
f3 = Fruit("딸기")
print("#자연적 삭제#")












