"""
파이썬에서 리스트는 전부 같은 타입일 필요 없음
순서대로 저장, 0 인덱스 시작
mutable type- 값 변경 가능
배열 없음 , 리스트만 존재
음의 인덱스로 접근 가능
"""

primes =[2,3,5,7]

for p in primes:
    print(p)

print(len(primes))

print(primes[0])
print(primes[-1])
print(primes[1]+primes[3])


list1=[1,2,3,4,5]

copy=list1
copy.append(6)

print(copy)
print(list1)
# 두 리스트가 동일
# 리스트만 넘겨 주는 것이라서

copy2=list1[:]
copy2.append(7)

print(copy2)
print(list1)
#list1[:]는 리스트의 모든 요소를 선택하여 자르는 구문
#제대로 복사됨
print("다음")

list3=[1,2,3]
list4=list((4,5,6))

print(list3+list4)
print(list3*3)

list3.extend(list4)
print(list3)

print("다음2")
list5 =[5,6,7,8,9]
list5.append(0)
print(list5)

list5.remove(7)
print(list5)

list5.remove(5)
print(list5)

list5.insert(5,2)
print(list5)
#원하는 인덱스, 넣을 요소
#존재하는 인덱스 넘어가면 그냥 그 다음 인덱스에 채워짐

list5.pop(1) #인덱스
print(list5)

print("순서 변환")
list5.reverse()
print(list5)

list5.sort()  #sorted는 원래의 리스트는 변경하지 않고, 정렬한 값을 보여줌
print(list5)

print("2차원")
matrix=[[1,2,3], ["하나","둘","셋"]]    
print(matrix[0])
print(matrix[0][0])
print(matrix[1][2])








