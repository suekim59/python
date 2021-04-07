#initialize method
class Dog:
    sound="멍멍" #클래스 변수 선언
    def __init__(self, name) :
    #인스턴스가 생성될 때 자동으로 호출되어 변수를 초기화
        self.name = name #인스턴스 변수 선언

    def bark(self):
        print(self.name+"가 멍멍하고 짓는다.")

my_dog=Dog("삼식이") #인스턴스 생성
my_dog.bark()

"""
class variable : 해당 클래스에서 생성된 모든 인스턴스가 값을 공유
instance variable : __init__() 메소드 내에서 선언된 변수
                    인스턴스가 생성될 때마다 새로운 값이 할당되는 변수
                    
"""