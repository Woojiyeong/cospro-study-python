def solution(scores):
    grade_counter = [0 for i in range(5)]
    for x in scores:
        if  x >= 85:
            grade_counter[0] +=1
        elif x >= 84:
            grade_counter[1] +=1
        elif x >= 55:
            grade_counter[2] +=1
        elif x >= 40:
            grade_counter[3] +=1
        else:
            grade_counter[4] +=1

    return grade_counter

scores = [50, 95, 65, 90, 80, 60]
ret = solution(scores)

print("soultion 함수의 반환 값은", ret, " 입니다. ")
