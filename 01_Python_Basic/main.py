a = 10
b = 20
c = a + b
print(c)

# New -> terminal
# 명령프롬프트(터미널)에서 python main.py를 실행하라고 알려주면 명령프롬프트에서 이 파일이 실행된다.
# 하지만 그 결과는 나오지 않는다. 여기서는 jupyter notebook의 REPL과는 다르게 실행된다.
# 자동으로 결과를 출력해주지 않는다. 그래서 print() 명령어를 꼭 사용해야 한다.
# REPL(Read-Evaluate-Print Loop)

# 이 파일에서 greeting 함수를 사용하고 싶지만 실행되지 않는다.
# 이때 필요한 것이 import 이다.
# greeting 함수는 my_module module에 있다.
# 그래서 이 module을 import하면 module에 있는 함수를 사용할 수 있다.

import my_module

r = my_module.greeting("홍길동")
print(r)

p = my_module.Person("홍길동", 30)
print(p)


# 이때 주의해야 할 점은 단순히 함수 이름만을 사용하면 지금 파일 즉, 지금 module에서 찾는다.
# 하지만 지금 module에는 greeting 함수와 Person class가 없다. 그래서 앞에 해당 함수와 class가 있는 module 명을 붙여야 한다.

# 현재 directory에 없는 module인 calculator을 사용할 때는 다음과 같이 해야 한다.
# my_package라는 package에서 calculator module을 import 하는 것이다.
# 그런데 아래와 같이 import 하면 calculator module의 함수를 사용할 때
# my_package.calculator.plus()와 같이 함수 이름을 적어야 한다.
import my_package.calculator
result = my_package.calculator.plus(a, b)
print(f"덧셈 결과: {result}")

# 위와 같은 방법은 효율적이지 못하다.
# 이를 효율적으로 해결할 수 있는 방법은 두 가지이다.
# 1번
# from my_package import calulator
# calculator.plus()
# 2번
# import my_package.calculator as calc
# calc.plus()












