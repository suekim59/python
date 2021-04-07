"""
variable scope
: local variable, global variable
local variable: 함수 내에서 선언된 변수
                함수의 호출이 끝남과 동시에 소멸
global variable: 함수 외부에서 선언된 변수

"""

#global variable
def fun():
    global global_var  #함수 내부에서 전역 변수 사용하려면 global로 재선언 해야 함
    local_var="지역 변수"
    print(local_var)
    print(global_var)

global_var="전역 변수"
fun()
print(global_var)


print("두번째 예시------")
def func(): 
    var="지역 변수"  #globe 키워드 사용하지 않아 전혀 별개로 취급됨
    print(var)

var="전역 변수"
func()
print(var)

print("세번째 예시-----")
def func3():
    global var1
    var1="지역 변수"
    print(var1)

var1="전역 변수"
print(var1)
func3()
print(var1)

