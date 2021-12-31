# Unpacking
x, _, y = (1, 2, 3)

a, *_, c = (1, 2, 3, 4, 5)

print(x, y, a, c)
# > 1, 3, 1, 5

for _ in range(10):
    pass

for _, v in enumerate(range(10)):
    pass


# 접근 지정자
# name: public
# _name: protected
# __name: private
# private 모두 외부에서 강제 수정이 가능
class Sample():
    def __init__(self) -> None:
        self.x = 0
        self._y = 1
        self.__z = 2

cls = Sample()

print(cls.x)
print(cls._y)
# AttributeError: 'Sample' object has no attribute '__z'
# print(cls.__z)
cls._Sample__z = 10
print(cls._Sample__z)
#> 10

    