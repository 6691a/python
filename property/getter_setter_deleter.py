"""
Property 장점
1. 파이써닉한 코드
2. 변수에 제약을 설정 할 수 있다.
3. Getter, Setter
    - 캡슐화, 유효성 검사, 기능 추가에 용이하다.
    - 대체 표현 (속성 노출, 내부 표현 보호)
    - 속성의 수명 및 메모리관리 (class 내부에 속하기 때문에 메모리 해제 이점이 있다)
      
"""

class Sample():
    def __init__(self):
        self.x = 0
        self.__y = 0

    # getter
    @property
    def y(self):
        print("getter")
        return self.__y
    
    # setter
    @y.setter
    def y(self, value):
        print("setter")
        self.__y = value

    @y.deleter
    def y(self):
        print("deleter")
        del self.__y

a = Sample()

a.y = 2
print(a.y)

# _Sample__y 삭제
del a.y

print(dir(a))

# AttributeError: 'Sample' object has no attribute '_Sample__y'
print(a.y)