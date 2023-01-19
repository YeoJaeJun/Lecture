# module을 만들 때 module version을 저장하는 변수를 만든다.
# 관례적으로 __version__을 변수명으로 사용한다.
__version__ = 1.0

def greeting(name):
    return f"{name} 님, 안녕하세요!"


class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"이름: {self.name}, 나이: {self.age}"


if __name__ == "__main__":
    print(__name__)
    g = greeting("김영수")
    p = Person("이순신", 20)
    print(g)
    print(p)
