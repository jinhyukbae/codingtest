"""
1부터 100까지의 숫자가 있고 이를 1* 99 2*98 같이 계산한다 했을 때 최대가 되는 경우는 어떤숫자를 곱했을 때 인지 찾아주세요

print(f"최대가 되는 경우는 {} * {} = {} 입니다") 형태로 출력한다.

"""

max_value = 0
a = 0
b = 0

for i in range(1,99+1): #1*99 ~ 99*1처럼 되야 하므로 99까지만 범위로 잡는다.
    j = 100 - i # i가 1이면 99 2면 98식으로 줄어듬
    if max_value < i*j: #i*j가 최대값보다 크면
        a = i 
        b = j 
        max_value = i*j # i*j = 최대값으로 해준다 
        # 최대값 = 0 i*j= 99이므로 최대값=99
        # 다음 반복 2*98=196 최대값 98보다 i*j 196이 더크므로 최대값=196 식으로 반복하면 2500이 나온다
        # print(f"최대가 되는 경우는 {} * {} = {} 입니다") 형태로 출력한다.식으로 출력하라 했으므로 a와 b 값도 구해준다
print(f"최대가 되는 경우는 {a} * {b} = {max_value} 입니다")        
print(a)
print(b) 
print(max_value)
