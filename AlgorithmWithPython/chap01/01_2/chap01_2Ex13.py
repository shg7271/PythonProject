# 파이썬 변수 알아보기
# 함수 내부-외부에서 정의한 변수와 객체의 식별 번호를 출력하기

n = 1           # 전역 변수(함수 내부-외부에서 사용)
def put_id():
    x = 1       # 지역 변수(함수 내부에서 사용)
    # x = 1을 x = n으로 바꿔도 같은 int형 객체 1을 가리키기 때문에 x의 id값이 동일하다.
    print(f'id(x) = {id(x)}')
print(f'id(1) = {id(1)}')
print(f'id(n) = {id(n)}')
put_id()

'''
id(1) = 140723127465760
id(n) = 140723127465760
id(x) = 140723127465760
'''

# 1부터 100까지 반복하여 출력하기
for i in range(1, 101):
    print(f'id({i}) = {id(i)}')
'''
id(1) = 140723127465760
id(2) = 140723127465792
id(3) = 140723127465824
id(4) = 140723127465856
id(5) = 140723127465888
...
'''