'''
Created on 2022. 8. 2.

@author: SIST
# 파일 쓰기
1. 결과를 파일에 쓰게 되면 모니터에는 나오지 않고, 파일로 직접 저장된다.
2. 기능메서드 : writelines("저장할 문자열")
# 파일 쓰기 3단계
1. 파일 객체 생성
    1) 파일을 쓰기 위해서도 open()함수에서 파일명을 지정하고, 파일 쓰기 모드(w)를
        선언하여야 한다.
    2) 이 때 파일 경로에 같은 이름의 파일이 있다면 기존 파일을 덮어 쓴다.
        - 같은 이름의 파일이 없다면 파일을 새로 생성한다.
    3) 쓰기용 open()함수의 매개변수로 "w"를 사용한다.
    ex)
    변수명 = open("경로명/파일명","w", encoding="utf-8")
2. 파일 쓰기
    변수명.writelines("저장할 문자열\n") : 해당 문자열을 줄단위로 저장처리한다.
3. 파일 닫기
    변수명.close() 자원을 해제 처리..
'''
outFile = open("z04_outText.txt","w", encoding="utf-8")
outFile.writelines("# 출력 파일 내용입니다1 #\n")
outFile.writelines("# 출력 파일 내용입니다2 #\n")
outFile.writelines("# 출력 파일 내용입니다3 #\n")
outFile.writelines("# 출력 파일 내용입니다4 #\n")
outFile.writelines("# 출력 파일 내용입니다5 #\n")
outFile.close()
# ex) z05_empList.txt  사원 정보를 input()으로 입력해서 해당 파일에 출력하게 하세요
empFile = open("z05_empList.txt","w", encoding="utf-8")
while True:
    empno = input("사원번호를 입력하세요:")
    ename = input("사원명를 입력하세요:")
    job = input("직책를 입력하세요:")
    empFile.writelines(empno+"\t"+ename+'\t'+job+'\n')
    isContinue = input("입력을 종료하실려면 Q:")
    if isContinue =="Q":
        break
print("사원정보 등록 완료!")
empFile.close()
    




