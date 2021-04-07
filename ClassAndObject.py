"""
1. Class :
함수를 포함한 프로그램 코드의 일부를 재사용하기 위해서는 
해당 함수뿐만 아니라 데이터가 저장되는 변수까지도 한꺼번에 관리하는 것이 편함
2. Object :
클래스로 생성되는 것
-> 이런 객체를 사용하여 데이터를 표현하는 프로그래밍 기법 OOP(객체 지향 프로그래밍)
3. Attribute:
클래스에 포함되는 변수
4. Method :
클래스에 포함되는 함수
5. Class member : Attribute + Method
"""

class Dog:
    name="삼식이"
    age=3
    breed="골든 리트리버"

    def bark(self):
        print(self.name+"가 멍멍하고 짓는다.") 
        #self는 자바의 this와 같은 역할
        #객체가 자기 자신을 참조하는데 사용하는 매개 변수
        #즉, self매개변수를 사용하면 메소드에서 클래스에 정의된
        #모든 속성 및 다른 메소드에 접근 가능  
    """
    파이썬에서는 메소드를 선언 시, 첫번째 매개변수로 반드시 self를 명시해야 함
    """

#instance란 클래스를 기반으로 생성된 object
my_dog=Dog() 
print(my_dog.breed) #인스턴스의 속성 접근
my_dog.bark() #인스턴스의 메소드 호출


 
