def func_a(s):
    ret = 0 
    for i in s:
        if i > ret:
            ret = i 
    return ret
def func_b(s):
    ret = 0
    for i in s:
        ret += i
    return ret

def func_c(s):
    ret = 101
    for i in s:
        if i < ret:
            ret = i 
    return ret

def solution(scores):
    sum = func_b(scores)
    max_score = func_a(scores)
    min_score = func_c(scores)
    return sum - max_score - min_score

scores = [50, 90, 65, 100]
ret = solution(scores)

print("soultion 함수의 반환 값은", ret, " 입니다. ")
