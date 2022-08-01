'''
Created on 2022. 8. 1.

@author: SIST
# 리스트 활용하기
1. 기능 메서드를 이용해서 추가와 삭제를 하면 구조가 변경이 된다.
    ex) 입력이  있으면 기본 위치는 뒤로 밀리고, 삭제하면
        해당 위치로 데이터가 다시 재조정이 된다. - 배열과 차이
2. 리스트는 지금까지 index로 접근할 뿐만 아니라, 여러가지 기능 메서드를 통해서
    동적으로 효과적인 기능 처리를 지원하고 있다.
3. 리스트 삽입
    리스트명.insert(위치, 값) : 정해진 위치에 값을 삽입하기
'''
numList = [10,20,30]
numList.insert(1,123) # 두번째 위치에 123데이터를 삽입 처리
print("현재 리스트 내용:",numList)
# ex) 회원 3명의 아이디 리스트로 선언하고, 3번째 위치에 회원아이디를 추가 삽입하세요
memberIds = ["himan","goodMan","whiteMan"]
memberIds.insert(2,"higirl")
print(memberIds)
'''
3. 리스트 값을 삭제
    1) 기본 형식
         del(리스트명[index번호]) : 해당 위치의 데이터가 삭제가 되고 다시 
             재조합이 된다.
    ps) 전체 메모리에서 삭제
        del(리스트명) : 변수나 객체의 이름을 선언했을 때, 전체 메모리에서 삭제가
        처리된다.
    2) 해당 값을 찾아서 삭제 처리..
        리스트명.remove(삭제할 데이터) : 리스트로 설정된 특정값을 삭제 처리..
        중복된 값이 있으면, 첫번째 값만 일단 삭제가 된다..
'''
del(numList[1]) # 두번째 위치에 있는 numList 삭제
print(numList)
del(numList) # numList 전체 메모리 삭제
# print(numList) # 해당 numList가 삭제되어 메모리에 사라진다.(에러발생)
memberIds.remove("goodMan") # 해당 값을 30데이터 삭제 처리
print("삭제 후 데이터:", memberIds)
'''
ex) 장바구니에 물건 3개를 list(사과, 바나나, 딸기)에 담고
    1) 마지막에 위치에 있는 물건을 삭제
    2) 바나나 데이터를 삭제
'''
cartList = []
cartList.append("사과")
cartList.append("바나나")
cartList.append("딸기")
print("카트에 담기 물건:",cartList)
del(cartList[-1]) # 리스트의 마지막 데이터 index : -1
cartList.remove("바나나") # 바나나 데이터 삭제
print("삭제 후 데이터 :", cartList) 
'''
# 리스트값 추출 갯수 세기
1. 리스트값 마지막 값 추출 및 삭제 처리
    pop() : 제일 뒤의 값을 뽑아내서 값을 특정한 변수에 할당할 수 있고,
        마지막값을 구조에서 삭제 처리된다.
2. 갯수 세기
    count(찾을값) :찾을 값이 몇 개인지 갯수를 세서 알려준다.
'''
numList = [10,20,30,10,20,10]

print("10 데이터의 건수:", numList.count(10))
print("삭제할 마지막 데이터:", numList.pop())
print("삭제할 마지막 데이터:", numList.pop())
print("삭제할 마지막 데이터:", numList.pop())
print("삭제 후 현재 리스트:", numList)
# ex) 장바구니에 초기에 물건 5개를 담고, 마지막 물건을 메서드를 통해서
#     제외 시키고, 제외된 리스트를 따로 출력하고,
#     현재 담은 물건 중에 중복된 것의 갯수를 출력하세요.
cartList = ["사과","사과","딸기","오렌지","수박"]
delList = []
delList.append(cartList.pop()) 
# 기능 메서드 pop()을 통해 삭제되면서 해당 내용을 리턴하기 때문에 다른 변수나 객체에
# 활용할 수 있다.
delList.append(cartList.pop())
print("현재 장바구니 내용:",cartList)
print("삭제된 리스트 내용:",delList)
print("현재 사과의 갯수:", cartList.count("사과"))
'''
# 리스트의 정렬 처리
1. sort() : 리스트의 값을 정렬처리한다.
    1) 숫자형태는 오름차순으로 정렬된다.
    2) 문자열의 경우는 알파벳, ㄱ,ㄴ,ㄷ... 순위로 정렬된다.
2. sort(reverse=True)
    1) 내림 차순 정렬
        가장 많은 데이터로 ranking 처리할 때 주로 활용된다.
'''
points = [80,90,75,88,100,70,50]
# 오름차순으로 정렬
points.sort()
print("정렬된 후 데이터:", points)
# 내림차순으로 정렬
points.sort(reverse=True)
print("내림 차순 데이터 :", points)
# 상위 1~3위 데이터
print("상위 1~3위:", points[:3])
# ex) 구매한 물건의 가격 5개를 리스트 하고, 오름차순/내림차순 정렬 후 출력하고
#    가장 가격이 높은 물건 3개를 출력하세요.
buyList = [3000,2000,4000,7000,1000]
buyList.sort(); print("오름 차순 정렬:",buyList)
buyList.sort(reverse=True); print("내림 차순 정렬:",buyList)
print("가장 가격이 높은 물건의 가격3:", buyList[:3])
'''
# 리스트의 복사처리 메서드 copy()
1. 일반 변수와 객체는 메모리할당 형식이 차이가 난다.
    1) 일반 변수 : 변수 선언 위치와 할당 메모리 위치가 동일
        대입 연산을 사용하더라도 각 다른 메모리를 활용
        num01 = 15
        num02 = num01
        num02 = 30
        num01(15), num02(30)
    2) 객체형 변수 : list를 비롯한 객체형 변수는 변수의 선언 위치와
        할당 메모리 위치가 다르다.
        대입연산자를 쓰면 객체의 메모리 위치로 할당하기 때문에 동일한 데이터가
        된다.
        list01 = [10,20,30]
        list02 = list01
        list02[1] = 40
        list01([10,40,30]),  list02([10,40,30])
2. 이와같이 객체를 사용하고, 대입연산자를 사용하면 메모리 위치가 복사하기에
    변경을 하면 이전 객체도 동일하게 변경이 되는 것을 볼 수 있다.
3. 이 때, 따로 메모리를 선언하여 사용하고자 한다면 copy()를 이용하여 처리하여야
    이런 메모리사용을 동일하게 하는 것에서 벗어날 수 있다.
        list01 = [10,20,30]
        list02 = list01.copy()
        list02[1] = 40
        list01([10,20,30]),  list02([10,40,30])
'''
num01 = 15
num02 = num01
num02 = 50
print("num01:",num01)
print("num02:",num02)
list01 = [10,20,30]
list02 = list01
list02[1] = 40
print("list01:",list01)
print("list02:",list02)
list03 = list01.copy()
list03[1] = 50
print("# copy 메서드 처리 후 #")
print("list01:",list01)
print("list03:",list03)
# ex) 학생 3명의 점수를 list04로 선언하고 대입연산자와 copy()를
#    사용한 경우의 변경시 차이점을 확인하세요
list04 = [80,90,100]
list05 = list04
list05[1]=100
print("#대입연산자 처리시#")
print("list04:", list04)
print("list05:", list05)
list06 = list04.copy()
list06[1]=80
print("#copy() 처리시#")
print("list04:", list04)
print("list06:", list06)
































