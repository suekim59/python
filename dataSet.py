"""
세트는 중괄호{}로 감싸서 선언
쉼표로 구분
"""

set1={1,2,3}
set2=set("Python")
set3=set("Hello")

print(set1)
print(set2) #순서 상관없이 무작위로 출력/ 문자열 하나하나 출력
print(set3) #중복되는 건 삭제됨.

"""
빈 세트를 나타날 때는,
set4={} 이거 말고
set5=set()
"""

set10={1,2,3}

set10.add(4)
print(set10)

set10.update((5,6))
print(set10)

set10.remove(2)
print(set10)

print("집합의 연산")
sett1={1,2,3,4,5}
sett2=set((1,3,5,7,9))

print(sett1)
print(sett2)

print(sett1 | sett2) #합집합
print(sett1 & sett2) # 교집합
print(sett1 - sett2) # 차집합 
print(sett1 ^ sett2)  # 여집합 = 합집합 - 교집합





