def solution(shirt_size):
    answer = [0]*6
    
    for size in shirt_size:
        if size == "xs":
            answer[0] += 1
        elif size == "s":
            answer[1] += 1
        elif size =="m":
            answer[2] += 1
        elif size =="l":
            answer[3] += 1
        elif size =="xl":
            answer[4] += 1
        elif size =="xxl":
            answer[5] += 1

    return answer

shirt_size = ["xs", "s", "l", "l", "xl", "s"]
ret = solution(shirt_size)
print("solution 함수의 반환 값은", ret, "입니다.")