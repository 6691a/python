# 비동기 I/O Coroutine

# Blocking I/O: 호출된 함수가 작업이 완료 될 떄까지 제어권을 갖고 있음
# NonBlocking I/O: 함수(서브루틴)가 return(yield) 후 호출 함수(메인 루틴)에 제어권을 전달 
import asyncio
import timeit
# urlopen = BlockingIO
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading

start = timeit.default_timer()
urls = ['https://daum.net', 'https://naver.com', 'https://tistory.com', 'https://wemakeprice.com/']

async def fetch(url, executor):
    # 쓰레드 디버깅
    print(f"Thread Start: {threading.current_thread().getName()}", url)
    # 실행
    response = await loop.run_in_executor(executor, urlopen, url)
    print(f"Thread Done: {threading.current_thread().getName()}", url)

    # 결과 반환
    return response.read()[:5]

async def main():
    # 쓰레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=len(urls))
    
    # future 객체를 모아 gather에서 실행
    futures = [
        # url 하나에 한개의 쓰레드 할당
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]

    # 결과 취합
    result = await asyncio.gather(*futures)

    print(f"Result: {result}")

if __name__ == '__main__':
    # 루프 초기화
    loop = asyncio.get_event_loop()
    # 작업 완료까지 대기
    loop.run_until_complete(main())
    print(f"total run time: {timeit.default_timer() - start}")
