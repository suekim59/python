"""
여러 개의 데이터를 하나로 묶는데 사용
리스트와 비슷하지만 immutable type
리스트보다 실행 속도가 빠름
튜플명=(요소1,요소2,요소3)
튜플명=요소1,요소2,요소3
"""
tuple1=(1,2,3)
tuple2=1,2,3
tuple3=(1,) #하나의 요소만을 가진 튜플은 꼭 쉼표를 붙여주어야 함!
tuple4=(1)

print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)

#선택, 자르기, 연산은 가능하지만
#추가,삭제,삽입,추출하는 동작 불가능


#패킹과 언패킹
tuple11=10,"열",True

a,b,c=tuple11     #튜플에 들어있는 요소와 동일한 갯수가 있지 않으면 오류

print(a)
print(b)
print(c)

#튜플 속 포함여부 확인
print("포함여부")
print(10 in tuple11)
print("아홉" not in tuple11)

