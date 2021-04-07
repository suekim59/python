#C언어, 자바와 달리 변수에 타입 없음
#변수를 선언할 때, 별도로 타입을 명시해줄 필요 없음

var = 7
print(type(var))

var = "문자열"
print(type(var))

#int
#str
#float
# + - * / 연산 사용
# / 나누기 사용 시, 실수로 반환

#bool : 자바에서 boolean
#비어 있으면,거짓으로 인식

#논리 연산자
# or, and, not
# ||, &&, ! (자바에서는 이러한 기능들)


i="김보형 "
j="아름다워"

print(i + j)
print(i * 3)
#위처럼 문자열을 숫자연산으로 사용 가능

py= "김보형의 아름다워"
print(py[0])
print(py[6])
print(py[-1])
print(len(py))
#배열처럼 하나씩 인식 가능
#-1은 뒤에서 첫 번째
#띄어쓰기도 하나로 인식

py2="우리집 강아지 이름은 멍멍이입니다."
print(py2[4])
print(py2[4:7])
print(py2[:4])
print(py2[4:])


py3="python programming"

print(py3.count('p'))

print(py3.find('o'))
print(py3.index('o'))

print(py3.find('z'))
#index는 문자열에 포함되어 있지 않으면, error를 반환
#무조건 있는지 확인하고 사용해야함


word="python"
print(word.upper())
word2="PYTHON"
print(word2.lower())

sen="파이썬 공부는 너무 재밌어요!"
print(sen.replace("파이썬","자바"))
print(sen)

print(sen.split(' '))
print(sen.split())
print(sen)