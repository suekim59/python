i=1

while i<11: #조건문
    print("파이썬" + str(i))
    i=i+1 #탈출조건

#탈출조건이 필요함
#while True:
#위는 무한루프 반복문

"""
for 변수 in 문자열(or 튜플 or 리스트):
    반복적으로 실행하고자 하는  명령문
"""

str="파이썬 프로그래밍"

for ch in str:
    print(ch)   #ch는 그냥 변수명으로 아무거로 바꿔줘도 됨

"""
range(마지막 정수)
range(시작정수, 마지막 정수)
"""

range(5) # 0,1,2,3,4
range(10) # 0,1,2,3,4,5,6,7,8,9
range(-3) # 아무런 정수도 반환 안됨

range(2,5) #2,3,4
range(-3,5) # -3,-2,-1,0,1,2,3,4

#break 사용
for col in range(2,10):
    if col >5:
        break
    for row in range(1,10):
        print(col, "x", row, "=", col*row)

#continue 사용
#처음으로 되돌아가게 함
for n in range(1,11):
    if n%2==0:
        continue
    print(n,"은 홀수입니다.")