con="sweet"

if(con=="sweet") :
    print("삼키다")
else:
    print("뱉는다")

#여러가지 경우로 조건문 짜기 -> elif
season="summer"

if season=="spring" :
    print("봄이 왔네요")
elif season =="summer":
    print("여름에는 더워요")
elif season=="fall":
    print("가을은 독서의 계절!")
elif season=="winter":
    print("겨울에는 눈이 와요")


temp=18

if temp<26:
    pass
else :
    print("에어컨을 켠다.")

#pass는 아무 동작을 취하지 않는 것
#일반적으로 자바에서는 따로 명령문이 명시되어 있지 않으면, 아무 것도 하지 않으나
#파이썬에서는 필요함
#아니면 단순하게 아래와 같이 적어도 됨
if temp<26:
    print("에어컨을 켭니다.")




