"""
function
프로그램 내에서 중복적인 코드의 작성을 최소화
코드의 재사용성을 높여줌
def 함수명(매개변수1):
    실행할 코드
"""
def hello() :
    print("함수 시작")
    print("안녕하세요!")
    print("함수 끝")

hello()

def sum(a,b):
    print(a+b)

sum(1,2)
sum(3,4)

"""
def 함수명(매개변수1,..):
    실행할코드
    return 결과값
"""

def sum2(a,b):
    print("함수 시작!")
    print("함수 끝!")
    return a+b

c=sum2(1,2)
print(c)    

print(sum2(3,4))

def sub(a,b):
    print(a-b)

sub(1,2)
sub(a=1, b=2)
sub(b=1, a=2)

def total(a, b=5, c=10):
    print(a+b+c)

total(1)
total(1,2)
total(1,2,3)
#함수선언 시 명시한 매개변수의 순서에 따라 언제나 순서대로 저장

#가변 매개변수(variable parameters)
#앞에 * 붙여주면 가변 매개변수가 됨
#사용자가 매개변수의 개수를 정할 수 있고
#이 매개변수는 튜플의 형태로 저장됨

def add(*paras):
    print(paras)
    total =0
    for para in paras:
        total +=para
    return total

print(add(100))
print(add(10,100))
print(add(10,100,1000))

#가변 매개변수로 딕셔너리를 사용할 경우 *가 아닌 ** 두 개 사용
def print_map(**dics):
    for item in dics.items():
        print(item)


print_map(하나=1)
print_map(one=1,two=2)
print_map(하나=1,둘=2,셋=3)

def arith(a,b):
    add=a+b
    sub=a-b
    return add, sub
#return 값은 하나이지만, 두 개 이상을 반환하고 싶으면 튜플을 사용

i,j=arith(0,1)

print(i)
print(j)


"""
람다(lambda)
간단한 함수의 선언과 호출을 하나의 식으로 간략히 표현한 것
map()이나 filter() 함수와 같이 함수 자체를 인수로 전달받는 함수에서 자주 사용
람다는 한번밖에 사용 못 함
"""

def add5(a,b):
    return a+b

print(add5(1,2))

#3줄을 아래와 같이 1줄로 바꿀 수 있다.
print((lambda a,b:a+b)(1,2))


