# name = input("이름을 입력해주세요:")
# phone = input("전화번호를 입력해주세요:")
# email = input("이메일 주소를 입력해주세요:")
# --------------------------------------------
# print("이름:", name)
# print("전화번호:", phone)
# print("이메일 주소:", email)

# name = input("이름을 입력하세요:")
# age= int(input("당신의 나이는?:"))

# age += 2
# print("이름:", name, "2년 후 나이:", age)
# ---------------------------------------------
# su1 = int(input("숫자를 입력해주세요:"))
# su2 = int(input("숫자를 입력해주세요:"))

# hap = su1+su2
# pae = su1-su2
# gop = su1*su2
# mok = su1/su2

# print ( "더하기:",hap, "빼기:", pae, "곱하기:", gop, "나누기", mok)
# -----------------------------------------------
# su = int(input("숫자를 입력해주세요:"))

# if(su % 2 == 0 ):
#     print(su,"짝수")
# else:
#     print(su,"홀수")
# -----------------------------------------------

# os = int(input("점수를 입력해주세요:"))
# db = int(input("점수를 입력해주세요:"))
# c = int(input("점수를 입력해주세요:"))

# if(os >= 90):
#     print( " os는 A")
# elif(os < 90 and os>= 80 ):
#     print(" os는 B")
# elif(os <= 80):
#     print(" os는 F")

# if(db >= 90):
#     print( " db는 A")
# elif(db< 90 and db>= 80 ):
#     print(" db는 B")
# elif(db <= 80):
#     print(" db는 F")

# if(c >= 90):
#     print( " c는 A")
# elif(c< 90 and c>= 80 ):
#     print(" c는 B")
# elif(c <= 80):
#     print(" c는 F")

# ----------------------------------------- 가독성 안좋아ㅜㅡㅜ 함수로 고쳐!!!!!!!!!!!

# result = 0

# for i in range(1, 10):
#     result += i
# print(result)

# a = 0 
# sum = 0 

# for a in range(1, 100+1):
#     sum += a 
# print("1~100까지의 합계 = ", sum)


# ------------------------------------------

# a = [1,2,3,4,5,6,7,8,9]
# print(a)
# print(a[3])

# print(a[-1])
# print(a[-3])
# a[3] = 7 # 네번째 원소 값 변경
# print (a)
# --------------------------------------------

# a= [1,4,3]
# print("기본 리스트", a )

# a.append(2)
# print("삽입:",a)

# a.sort()
# print("오름차순 정렬:",a)

# a.sort(reverse = True)
# print("내림차순 정렬:",a)

# a.reverse()
# print("원소 뒤집기", a)

# a.insert(2, 3)
# print("인덱스 2에 3 추가", a)

# print("값이 3인 테이터 개수:", a.count(3))
# a.remove(1)
# print("값이 1인 데이터 삭제", a)
#------------------------------------------

# a = input("멤버의 이름:")


# namelist = ["Rm","진","슈가","제이홉", "지민", "뷔", "정국"]
# agelist = [29,31,31,30,28,28,25]
# kilist = [181,179,174,177,174,179,177]

# for index in range(0, 6+1):
#     print(namelist[index], agelist[index], kilist[index])

# for wow in range(0, 6+1):
#     if(namelist[wow] == a ):
#         print(namelist[wow], agelist[wow], kilist[wow])
# -----------------------------------------------------------------

# sum = 0

# for n in range(1, 10+1):
#     sum = sum + (n*n)
#     print("1~10까지의 제곱의 합: ", sum)
# ---------------------------------------------------------------------

# result= 1
# x = int(input("수를 입력하세요: "))
# y = int(input("수를 입력하세요: "))

# for n in range(1, x+1):
#     result = result * x
#     print(x,"의", y,"승","=",result)

# ------------------------------------------------------------------------

# for dan in range(2, 10):
#     print("======",dan,"단======")
#     for n in range(1,10):
#         result = dan * n 
#         print(dan,"X",n,"=",result)
#--------------------------------------------------------

# btslist = ["Rm","진","슈가","제이홉", "지민", "뷔", "정국"]
# bplist = ["지수", "제니", "로제", "리시"]

# print('-'*5,"방탄소년단",'-'*5)
# for idolname in btslist:
#     print(idolname)

# print('-'*5,"블랙핑크",'-'*5)
# for idolname in bplist:
#     print(idolname)

# print(btslist)
# print(bplist)
# ---------------------------------------------------------

print("*****************************************")
print("[1]팝콘세트 [2]나초세트 [3]오징어세트 [4]핫도그세트 만약 원하시는 메뉴가 없다면 [5]번을 눌러주세요")
print("*****************************************")

prices = {
    1: 15000,
    2: 12000,
    3: 20000,
    4: 10000
}

total = 0  

while True:
    choice = int(input("선택메뉴: "))
    
    if choice == 5:
        print("주문을 종료합니다.")
        break
    
    if choice in prices:
        n = int(input("수량을 알려주세요: "))
        total += prices[choice] * n
    else:
        print("잘못된 번호입니다. 다시 선택해주세요.")

print(f"총 금액은 {total}원 입니다.")



