'''
Created on 2022. 8. 3.

@author: SIST
# 리스트형 객체 처리
1. 기존의 [](리스트)유형에서 class를 선언하고, 객체를 추가하여 처리하는 형태를
    말한다.
2. 주로 데이터를 여러가지 유형의 리스트를 처리할 때, 활용할 수 있다.
'''
class Product:
    def __init__(self, name, price, cnt):
        self.name = name
        self.price = price
        self.cnt = cnt
    def buy(self):
        print(self.name, end="\t")
        print(self.price, end="\t")
        print(self.cnt, end="\n")
        return self.price*self.cnt
pList = []
pList.append( Product("사과",3000,2))
pList.append( Product("바나나",4000,3))
pList.append( Product("딸기",12000,5))
print("list객체",pList)
tot = 0
print("물건명\t가격\t갯수")
for prod in pList:
    tot += prod.buy()
print("총비용:",tot)
# ex) list형 객체 처리하기 위하여 도서명과 도서가격, 출판사를 속성으로 이를 출력하는 메서드를
#     class로 선언하고, 객체 3개를 생성 list에 담고, 반복문으로 출력하세요.
class Book:
    def __init__(self, title, price, publisher):
        self.title = title
        self.price = price
        self.publisher = publisher
    def showInfo(self):
        print(self.title, end = "\t")    
        print(self.price, end = "\t")    
        print(self.publisher, end = "\n")    
blist = []
blist.append(Book("자바기초",27000,"it기술"))
blist.append(Book("jsp중급",30000,"혜영사"))
blist.append(Book("스프링고급",33000,"오라클"))
for book in blist:
    book.showInfo()
    
# install numpy    
# install pandas
# install matplotlib
# install tensorflow
# 설치.
# 하단에 apply (시간 꽤 걸림)
# 설치된 내용 확인    
import numpy as np
ar = np.array([1,2,3])
print(ar)  
from pandas import DataFrame
data = DataFrame
print(data)  












        