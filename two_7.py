def func_a(arr,n):
    ret = []
    for x in arr:
        if x != n:
            ret.append(x)
    return ret

def func_b(a,b):
    if a >=b:
        return a- b
    
def func_c(arr):
    ret = -1
    for x in arr: 
        if ret < x :
            ret = x
    return ret  

def solution(visitor):
    max_first = func_c(visitor) 
    visitor_removed = func_a(visitor, max_first)
    max_second = func_c(visitor_removed)
    answer = func_b(max_first, max_second) 
    return answer

visitor = [50, 20, 30, 10, 40]
ret = solution(visitor)

print("soultion 함수의 반환 값은", ret, " 입니다. ")
