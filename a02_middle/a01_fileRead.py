'''
Created on 2022. 8. 2.

@author: SIST
# 파일 입출력
1. 파일의 필요성
2. 파일의 읽기
    1) 파일 읽기 3단계
    2) readline()
    3) readlines()
3. 파일의 쓰기
    1) 파일 쓰기 3단계
    2) 파일의 한 줄 쓰기
    3) 파일의 입력받아 쓰기
# 파일을 사용하는 이유
1. 파일은 왜 필요한가?
    1) 문서편집기의 경우를 예를 들어, 매번 입력된 내용을 파일에
        저장해서 사용할 때, 저장 피일이라는 물리적 파일 정보가
        있어야 한다.
    2) 저장된 파일은 시간이 지나더라도 다시 읽어와서 정보를 활용할 수 있다.
# 파일 읽기/쓰기
1. 파이썬은 파일 읽기와 쓰기를 지원하고 있다.
2. 처리 단계
    1) 파일 객체 만들기
        파일객체명 = open("경로/파일명","r/w", encoding="utf-8")
        파일을 쓰고/읽기 위해서 open()기능 메서드를 통해서
        매개변수1 : 경로/파일명 지정
        매개변수2 : r/w (read/writer) 옵션 설정
        매개변수3 : 저장된 파일 또는 저장할 파일의 한글 encoding방식 선언.
    2) 파일읽어/파일쓰기
        파일객체명.readline() : 파일에 저장된 내용 한줄씩 읽어 오기 
        파일객체명.readlines() : 파일에 저장된 내용 list형식으로 여러줄 내용
            읽어오기.
        파일객체명.writelines("저장할데이터") : 파일에 저장할 정보를 처리한다.
    3) 파일자원의 해제
        파일객체명.close() : 파일의 자원을 해제 처리한다.
# readline()함수
1. 파일에 담아둔 데이터를 읽기 위한 함수
    readline(), readlines()
2. 한 행씩 읽어 오는 처리를 한다.
3. 파일에 100행이 있다면, 100번을 반복해서 읽어야 한다.
    
'''
# 1. 파일 객체 선언
inFile = open("z01_myText.txt","r", encoding="utf-8")
# 2. 읽어온 내용 문자열로 할당.
inStr = inFile.readline()
print(inStr,end=",")
inStr = inFile.readline()
print(inStr,end=",")
inStr = inFile.readline()
print(inStr,end=",")
inStr = inFile.readline()
print(inStr,end=",")
inStr = inFile.readline()
print(inStr,end=",")
# 3. 자원을 해제하기
inFile.close()
# ex) z02_song.txt  노래 가사 정보를 복사해 넣고, 해당 파일을 호출해서
#     출력하세요..
inFile2 = open("z02_song.txt","r", encoding="utf-8")
print("#음악 가사 #")
inStr2 = inFile2.readline();print(inStr2,end="")
inStr2 = inFile2.readline();print(inStr2,end="")
inStr2 = inFile2.readline();print(inStr2,end="")
inFile2.close()
# 반복문을 통해서 파일 내용이 있을 때까지 출력하기..
print("# 반복문을 통한 파일 처리 #")
inFile3 = open("z02_song.txt","r", encoding="utf-8")
while True:
    inStr = inFile3.readline()
    if inStr=="": # 파일 내용이 읽어 올게 없을 때 중단 처리
        break;
    print(inStr, end="")
inFile3.close()
# readlines() 함수 예제
inFile4 = open("z02_song.txt","r", encoding="utf-8")
inList = inFile4.readlines() # 라인단위 리스트 데이터로 가져온다.
print(inList)
print("# 반복문을 활용한 파일 내용 리스트 데이터 #")
for line in inList:
    print(line, end="")
inFile4.close()    
# ex) z03_poem.txt 에 좋아하는 시를 등록하고 readline()를 통해서
#     출력하세요.
inFile5 = open("z03_poem.txt","r", encoding="utf-8")
inList2 = inFile5.readlines()
print()
print("# 좋아하는 시 #")
for line in inList2:
    print(line, end="")
inFile5.close()   

























