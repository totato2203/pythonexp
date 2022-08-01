'''
Created on 2022. 7. 29.

@author: SIST

# 리스트(list)
1. 하나씩 사용하던 변수를 붙여서 한 줄로 나타내는 개념의 객체
2. 리스트는 종이상자를 한 줄로 붙인 후에 박스 전체의 이름을 지정하여 사용한다.
3. 각각의 데이터에는 번호(첨자)를 붙여서 접근한다.
    리스트명[index번호] :  index번호는 0부터 시작한다.
    ex) numlist[0] numlist[1] numlist[2]
4. len(리스트명) : 리스트의 크기

# 리스트의 생성
1. 대괄호를 선언
    list01 = []
2. 대괄호 안에 값을 선언
    list02 = [3000,4000,5000]

'''
numList = [1000,2000,3000]
print(numList[0])
print(numList[1])
print(numList[2])
# ex) 리스트를 초기화하고 입력된 데이터로 리스트 처리하자.
'''
numlist2 = [0,0,0]
numlist2[0] = int(input("숫자 입력"))
numlist2[1] = int(input("숫자 입력"))
numlist2[2] = int(input("숫자 입력"))
for num in numlist2:
    print(num)
tot =  numlist2[0]+numlist2[0]+numlist2[0]

print("합산:",tot)
'''
# ex) 학생의 3가지 국어, 영어, 수학 점수를 할당하고 총점/평균출력하세요.
'''
subjects =['국어','영어','수학']
points =[0,0,0]
for idx in range(3): # 0,1,2
    points[idx] = int(input(subjects[idx]+"점수:")) # index별로 데이터 할당
tot = points[0]+points[1]+points[2] 
print("총점:",tot)   
print("평균:",tot//3)  # 소숫점 이하 절삭 
'''
'''
# 리스트의 다양한 형태
1. 비어있는 리스트 생성
    numlist=[]
2. 정수형 데이터 리스트 생성
    intlist = [10,20,30]
3. 문자열 데이터 리스트 생성
    strlist = ['안녕','반갑습니다','어서오세요']
4. 다양한 데이터유형 리스트 생성 ;
    mxlist = [400,True, 25.7,'운수 좋은 날']
# 리스트 추가 하는 메서드 : append(추가할데이터)
1. 리스트는 배열과 달리 고정적인 크기로 사용하지 않고, 동적으로
    크기가 변경이 될 수 있는 데이터 유형이다. - 동적 배열
2. 리스트를 하나씩 추가하여 하기하기
    리스트는 동적인 배열로 append라는 메서드를 통해서 하나씩
    추가하여 크기가 변경될 수 있다.
    리스트의 구조체에 가장 마지막 부분에 추가하여 처리한다.
3. 기본 형식
    리스트 변수 =[]
    리스트변수.append(데이터1)
    리스트변수.append(데이터2)
    리스트변수.append(데이터3)
'''
fruits=[]
fruits.append('사과')
fruits.append('바나나')
fruits.append('딸기')
print("과일 리스트:", fruits)
print("과일 리스트크기:", len(fruits)) # list의 크기 len
# ex) 도서 목록 3가지를 list의 초기[]로 선언하고 append로 할당한 후,
#     반복문을 통해 @@ - @@@ 형태로 출력하세요.
books = []
books.append("자바")
books.append("파이썬")
books.append("C++")
for idx in range(len(books)):
    print(idx+1, "- "+books[idx])
'''
# 리스트 데이터의 접근
1. 리스트형 데이터의 접근 속성
    1) index : 리스트는 리스트명[index번호]로 0부터 시작해서 접근할 수 있다.
        리스트명[-1] : 제일 마지막 데이터
        리스트명[-2] : 뒤에서 두번째 데이터
    2) 첨자(콜론:)을 활용하여 리스트의 데이터를 부분적으로 추출해서 사용할 수 있다.
        리스트명[0부터시작index:1부터시작순서index]
        리스트명[시작index:] : 시작 index부터 끝까지
        리스트명[:1부터 순서index]: 0부터 해당하는 순서 index번호까지 추출
'''
print("마지막 도서명:", books[-1])
fruits.append("수박")
fruits.append("오렌지")
fruits.append("키위")
fruits.append("참외")
print("전체데이터:", fruits[:])
print("두번째부터 4번째까지 추출:", fruits[1:4])
print("4번째 이후 데이터 추출:", fruits[3:])
print("첫번째부터 3번째까지 추출:", fruits[:3])













