"""
리스트와 튜플은 인덱스로 순차적으로 요소에 접근 가능
딕셔너리는 사전이라는 말 그대로 키(key)를 통해 각 요소에 접근 가능 -> 맵 in 자바
선언방법
키:값
"""

dict1={'하나':1, '둘':2, '셋':3}
dict2=dict({'하나':1, '둘':2, '셋':3})
dict3=dict ([('하나', 1), ('둘', 2), ('셋',3)])
dict4=dict(하나=1, 둘='two', 셋=3)

print(dict1)
print(dict2)
print(dict3)
print(dict4)

"""
dict4처럼 =을 사용하려면
key가 문자열이어야 함
그렇기 때문에 굳이 ''넣을 필요 없는 것일까?
"""
dict5={'하나':1,2:'two', 3.14:'pi'}
dict6={('ten',10):['열',10.0]}

print(dict5)
print(dict6)

dict11=dict({'자바':80, 'PHP':90, 'HTML':70})

print(dict11['자바'])
print(dict11.get('자바'))

print(dict11.get('파이썬')) #None 이라고 나옴 => 값이 없음

dict11['파이썬']=100 #딕셔너리에서 요소 추가 
print(dict11)

del dict11['PHP']   #딕셔너리에서 요소 제거
print(dict11)

dict11['자바'] = 100 #간단하게 딕셔너리 요소 수정
print(dict11)

#dict11.clear()  딕셔너리에서 값 모두 삭제

print(dict11.keys())
print(dict11.values())
print(dict11.items())

print('HTML' in dict11)
print('PHP' in dict11)








