def func_a(k):
    sum = 0 
    for i in range( k + 1):
        sum += i
    return sum 
def solution(n, m):
    sum_to_m = func_a(m)
    sum_to_n = func_a(n -1)
    answer = sum_to_m - sum_to_n
    return answer
ret = solution(5, 6)
print("soultion 함수의 반환 값은", ret, " 입니다. ")
    