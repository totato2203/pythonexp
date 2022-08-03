'''
Created on 2022. 8. 3.

@author: SIST
# 생성자
1. 객체를 생성하면 무조건 호출되는 메소드를 의미한다.
2. 객체를 생성하면서 변수의 값을 초기화하는 메소드를 말한다.
3. 생성자로 초기화를 하면 코드가 간결해진다.
# 생성자의 형태
1. 생성자를 클래스 안에서 __init__()라는 이름으로 지정되어 있다.
2. 기본형식
    class 클래스이름:
        def __init__(self, name):
            self.name = name  # 자바와 달리  self.를 접두어로 두면 필드로 선언된다.
    
    참조명1 = 클래스이름("할당데이터")            
'''
class Person:
    def __init__(self, name, age, loc):
        self.name = name
        self.age = age
        self.loc = loc
    def showInfo(self):
        self.chac = "온화한 성격" 
        print("# Person의 정보 #")
        print("이름:",self.name)
        print("나이:",self.age)
        print("사는곳:",self.loc)
p01 = Person("홍길동",25,"서울")        
p02 = Person("김길동",27,"부산")        
p03 = Person("신길동",28,"광주")
p01.showInfo()
p02.showInfo()
p03.showInfo()
print("메서드에의해 추가된 필드:",p01.chac)
# ex) 좋아하는 운동선수의 팀명, 이름, 성적을 클래스로 선언하고 생성자를 통해 초기값
#     처리, showRecords()를 통해 필드값을 출력하세요.
class Player:
    def __init__(self, tname, name, record):
        self.tname = tname
        self.name = name
        self.record = record
    def showRecords(self):
        print("# 선수의 정보 #")
        print("소속팀:", self.tname)    
        print("이름:", self.name)    
        print("성적:", self.record)    
pl01 = Player("토드넘", "손흥민", 23)
pl01.showRecords()

        
        
        
        




