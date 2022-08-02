'''
Created on 2022. 8. 1.

@author: SIST
# 딕션너리
1. 단어 의미 그대로 '영어사전'과 같은 구조를 가진다.
2. 2개의 쌍이 하나로 묶이는 자료구조를 의미한다.
3. 딕션너리는 중괄호({})로 묶여 있다.
4. 키(key)와 값(value)의 쌍으로 이루어진다.
    키:단어, 값: 뜻
    ps) 키데이터 :일반적으로 다른 데이터와 구분하여 중복적인 처리를 하지 않게 할 때,
    주로 활용된다. 동일한 키 데이터를 입력하면 해당 데이터를 크기가 변경이 되지 않는다.
5. 기본 예제
    딕션너리변수 = {키1:값1,키2:값2,키3:값3....}
'''
myDict = {1:'a',2:'b',3:'c'}
print(myDict)
# 추가할 때는 새로운 key로 데이터 할당.
# 딕션너리변수[키] = 데이터
myDict[4] = 'd'
print(myDict)
# 기본에 있는 키로 데이터를 할당시는 해당 키의 데이터가 변경만 일어난다.
myDict[1] = 'o'
print(myDict) 
# ex) 사원번호와 사원명으로 딕션너리 데이터를 만들고, 사원번호의 추가와 변경을 처리하세요.
empDict = {1000:"홍길동",1001:"김길동",1003:"신길동"}
print("초기 사원정보:", empDict)
empDict[1004]="마길동"
print("사원정보의 추가:",empDict )
empDict[1000]="오길동"
print("사원정보의 수정:",empDict)
'''
6. 딕션너리 데이터의 삭제
    1) del(딕션너리명[키])
        해당 딕션너리명안에 있는 키를 기준으로 키/값이 삭제 처리 된다.
'''
del(empDict[1000])
print("삭제후 사원정보:", empDict)
'''
# 딕션너리데이터 반복문과 함께 활용
1. 다음과 같은 기능메서드를 통해서 for문과 함께 사용할 수 있다.
    1) 딕션너리명.keys() : 키 데이터만 가져올 수 있다.
    2) list(딕션너리명.keys()) : 형변환을 list변환 처리
    3) for 키 in list딕션너리명:
         키, 딕션너리명[키]
'''
empnosDic = empDict.keys()
print("emplist의 키:",empnosDic)
empnos = list(empnosDic) # list형태로 형변환
print("emplist의 키 리스트:", empnos)
print("사원번호\t사원명")

for empno in empnos:
    print(empno,end="\t")
    print(empDict[empno])
# ex) 학생번호와 학생이름을 dictionary데이터로 선언하고 반복문으로 출력하세요.
students = {1:"홍길동",2:"김길동",3:"신길동"}
studNos = list(students.keys())
for no in studNos:
    print(no, end = "\t")
    print(students[no])
'''
# 딕션너리 관련 유용한 함수
1. 딕션너리명.values() : 딕션너리의 모든 값을 리스트로 만들어 반환한다.
    list()로 형변환하여 list 형태로 사용할 수 있다.
2. 딕션너리이름.items() : 2차원의 튜플 형태로 변환해서 데이터를 가져온다.
'''
print("values() : ", empDict.values())
enames = list(empDict.values())
print("# 사원명(value) #")
for ename in enames : 
    print(ename)
print("empDict.items() : ", empDict.items())

# ex) 학생 dictionary 데이터 기준으로 값과 tuple 2차원 데이터를 출력하세요.
print("학생(딕션너리) : ", students)
print("학생values(이름) : ", students.values())
studentnames = list(students.values())
print("학생 목록 : ")
for student in studentnames : 
    print(student)
print("학생 튜플(2차원) : ", students.items())






