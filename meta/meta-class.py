# 커스텀 메타 클래스 생성 (Type 상속 X)

def mul(self, data):
    # self는 개체 생성 시 초기화 된 값
    for i in range(len(self)):
        self[i] = self[i] * data

def replace(self, old, new):
    while old in self:
        self[self.index(old)] = new

# list를 상속, 메소드 2개 추가
CoustomList = type('CustomList', (list,), 
    {
        'desc': '커스텀 리스트', 
        'mul': mul,
        'replace': replace
    }
)

c = CoustomList([1, 2])

c.mul(10)

# [10, 20]
print(c)




# 커스텀 메타 클래스 생성 (Type 상속 O)

class MetaClassName(type):
    def __new__(meta_cls, name, base, dict):
        # 코드
        pass

from typing import Any, Union
# 호출 순서 new -> init -> call
class CustomeListMeta(type):
    # 인스턴스 생성 (메모리 초기화)
    def __new__(meta_cls, name: str, bases: tuple[type, ...], namespace: dict[str, Any]):
        print("Call __new__")
        print(meta_cls, name, bases, namespace)
        namespace['mul'] = mul
        namespace['replace'] = replace
        return super().__new__(meta_cls, name, bases, namespace)

    # 생성된 인스턴스를 초기화
    def __init__(self, object_or_name: Union[object, str], base: tuple[type, ...], dict: dict[str, Any]):
        print("Call __init__")
        print(self, object_or_name, base, dict)
        super().__init__(object_or_name, base, dict)
    
    # 인스턴스 실행
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("Call __Call__")
        print(self, args, kwds)
        return super().__call__(*args, **kwds)    

custome_list = CustomeListMeta('CustomeMeta', (list, ), {})

cl = custome_list([1, 2, 3])
cl.mul(100)
# [100, 200, 300]
print(cl)
