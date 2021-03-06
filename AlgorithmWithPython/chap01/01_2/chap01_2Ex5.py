# 반복 과정에서 조건 판단하기 2
# +와 -를 번갈아 출력하기 1
print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for i in range(n):
    if i % 2:   # i가 짝수라면 거짓 홀수라면 참
        print('-', end='')  # 홀수
    else:
        print('+', end='')  # 짝수
print()

''' 위 프로그램은 두가지 문제가 존재한다.
1. for문을 반복할때마다 if문을 수행한다. 즉, n이 50,000번 이라면 if문이 50,000번 수행된다.
2. 이 프로그램은 상황에 따라 유연하게 수정하기 어렵다.
'''

# +와 -를 번갈아 출력하기 1(for문 수정)
print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for i in range(1, n+1):
    if i % 2:   # i가 짝수라면 거짓 홀수라면 참
        print('+', end='')  # 홀수
    else:
        print('-', end='')  # 짝수
print()

# +와 -를 번갈아 출력하기 2
print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for _ in range(n // 2): # 파이썬에서 무시하고 싶은 값은 언더스코어로 표현할 수 있다.
    print('+-', end='')
# n이 홀수인 경우 마지막 +를 출력하기 위한 코드
if n % 2:  # if n % 2 == 1:과 같은 의미
    print('+', end='')
print()

# 위 코드는 문제점 1, 2를 모두 해결한 코드이다.