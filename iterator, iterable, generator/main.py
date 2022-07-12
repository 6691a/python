from random import randint
from collections.abc import Iterable, Iterator
class RendomIntIterator():
    def __init__(self, min: int, max: int, count: int):
        self.current: int = 0
        self.max: int = max
        self.min: int = min
        self.count: int = count

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.count > self.current:
            self.current += 1
            return randint(self.min, self.max)
        else:
            raise StopIteration


class RandomIntIterable():
    def __init__(self, min: int,  max: int, count: int):
        self.min: int = min
        if min > max:
            raise ValueError("max must be greater than min")
        self.max: int = max
        self.count: int = count

    def __iter__(self):
        # 주의 iterator를 반환 해야함
        return RendomIntIterator(self.min, self.max, self.count)


random = RandomIntIterable(1, 10, 3)
iter1 = iter(random)
iter2 = iter(random)

# iter함수로 생성된 iterator는 모두 다름
assert iter1 != iter2

# iterator를 iter 함수를 통해 iterator로 만들어도 같은 값이 출력
assert iter1 is iter(iter1)

print(next(iter1))
print(next(iter1))
print(next(iter1))
# StopIteration
# print(next(iter1))

print("====")

for i in iter2:
    print(i)

print("====")

for i in RandomIntIterable(20, 30, 2):
    print(i)


# Iterator는 Iterable을 상속한다
assert True == issubclass(Iterator, Iterable)
assert False == issubclass(Iterable, Iterator)
