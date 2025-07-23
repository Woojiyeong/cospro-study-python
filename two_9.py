def solution(stones):
    cnt = 0 
    current = 0
    n = len(stones) # 이동 수

    while current < n:
        current +=stones[current]
        cnt += 1
    return cnt 

stones = [2,5,1,3,2,1]
ret = solution(stones)

print("soultion 함수의 반환 값은", ret, " 입니다. ")