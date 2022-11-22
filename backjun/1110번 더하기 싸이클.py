"""
ex)26
1.각 자리의 숫자를 더한다. 2+6 = 8
2.주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 

주어진 수의 가장 오른쪽 자리 수 6
앞에서 구한 합 8
이어붙이면 68

1사이클

68

1.각 자리의 숫자를 더한다. 6+8 = 14
2.주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 

주어진 수의 가장 오른쪽 자리 수 8
앞에서 구한 합의 가장 오른쪽 자리 수 4
이어붙이면 84

2사이클

84

1.각 자리의 숫자를 더한다. 8+4 = 12
2.주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 

주어진 수의 가장 오른쪽 자리 수 4
앞에서 구한 합의 가장 오른쪽 자리 수 2
이어붙이면 42

3사이클

42

1.각 자리의 숫자를 더한다. 4+2= 6
2.주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 

주어진 수의 가장 오른쪽 자리 수 2
앞에서 구한 합의 가장 오른쪽 자리 수 6
이어붙이면 26

4사이클

26  
"""

n = int(input()) #26
num = n
count = 0

while 1: #while True랑 같음 
    a = num // 10 # 주어진수 26를 10으로 나눈 몫 2
    b = num % 10 # 주어진수 26을 10으로 나눈 나머지 6
    c = (a+b) % 10 # 1.각 자리의 숫자를 더한다 2+6=8 두자리 수면 가장오른쪽 자리 수를 구해야하기 때문에 % 10을 해줌
    num =(b*10)+c #주어진수의 오른쪽 자리 6 합의 오른쪽 자리 8 붙인 값 68을 만들자

    count = count + 1 # 위 과정을 반복할 때마다 사이클을 +1씩 해준다 

    if num == n:
        break # 처음 입력한 수가 원래 수로 돌아왔을 때 == 무한반복을 멈춘다.

print(count) #사이클의 길이를 출력한다.



""" 다른수로도 테스트
    a = num // 10 68 // 10 몫 6
    b = num % 10 68 % 10 나머지 8
    c = (a+b)%10 6+8 14 % 10 나머지 4 = 오른쪽 자리 수
    num = (b*10)+c 8*10= 80+4= 84
"""