"""
컨텍스트 매니저: 원하는 타이밍에 리소스 할당 및 제공, 반환을 해준다.
with
"""

file = open('./test1.txt', 'w')

# 구 버전 방식
try:
    file.write("Test1 Write")
finally:
    file.close()

# 최신 방식
with open('./test2.txt', 'w') as f:
    f.write("Test2 Write")


# Context Manager
class CustomFile():
    def __init__(slef, file_name, method):
        slef.file = open(file_name, method)
    
    # 진입 시
    def __enter__(self):
        return self.file
    # 나갈 시
    def __exit__(self, exc_type, exc_value, trace_back):
        if exc_type:
            print(f"error:{exc_value} / {trace_back}")
        self.file.close()

with CustomFile('./test3.txt', 'w') as f:
    f.write("CustomFile")