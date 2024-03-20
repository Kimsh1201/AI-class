# 연습문제 3.1
if 100 > 200 :
    print("True")
else :
    print("False")
# 결과는 False
100 >= 200 #False
100 < 200 #True
100 <= 200 #True
100 == 200 #False
100 != 200 #True
200 == 200 #True
200 != 200 #False
True or True #True
True or False #True
True and False #False
True and True #True
True or True and False #True
True and True or False #True
'Morning' < 'morning' #True
'A' > 'B' #False

# 연습문제 3.3
age = int(input("나이를 입력하시오 : "))
height = int(input("키를 입력하시오(단위 cm) : "))

if age >= 19 and height >= 150 :
    print("입장할 수 있습니다.")
else :
    print("입장할 수 없습니다.")

# 연습문제 3.5
a, b = map(int, input("두 개의 정수를 입력해 주세요 : ").split())

if a>b :
    print("{0:d} {1:d}".format(b,a))
else:
    print("{0:d} {1:d}".format(a,b))

# 연습문제 3.7
score = int(input("게임점수를 입력하시오 : "))

if score >= 1000 :
    print("고수입니다.")
else :
    print("입문자입니다.")

# 연습문제 3.9
a = int(input("정수를 입력하시오 : "))

if  a % 2 == 0 :
    print(a, "는(은)", "2(으)로 나누어집니다.")
else :
    print(a, "는(은)", "2(으)로 나누어지지 않습니다.")

if  a % 3 == 0 :
    print(a, "는(은)", "3(으)로 나누어집니다.")
else :
    print(a, "는(은)", "3(으)로 나누어지지 않습니다.")

if  a % 2 == 0 and a % 3 == 0 :
    print(a, "는(은)", "2와(과) 3 모두로 나누어집니다.")
else :
    print(a, "는(은)", "2와(과) 3 모두로 나누어지지 않습니다.")

# 연습문제 3.11
a = input("세 복권번호를 입력하시오 : ").split()

if "2" in a and "3" in a and "9" in a :
    print("상금 1억 원")
elif "2" not in a and "3" in a and "9" in a :
    print("상금 1천만 원")
elif "2" in a and "3" not in a and "9" in a :
    print("상금 1천만 원")
elif "2" in a and "3" in a and "9" not in a :
    print("상금 1천만 원")
elif "2" not in a and "3" not in a and "9" in a :
    print("상금 1만 원")
elif "2" not in a and "3" in a and "9" not in a :
    print("상금 1만 원")
elif "2" in a and "3" not in a and "9" not in a :
    print("상금 1만 원")
else :
    print("다음 기회에...")

# 연습문제 3.13
x, y = map(int,input("점의 좌표 x, y를 입력하시오 : ").split())

if  (x-3)**2 + (y-4)**2 > 100 :
    print("원의 외부에 있음")
else :
    print("원의 내부에 있음")

# 연습문제 3.15
# for문
for i in range(1, 10) :
    print("2 *", i, "=", 2 * i)

# while 문
i = 0
while i < 9 :
    i = i +1
    print("2 *", i, "=", 2*i)

# 연습문제 3.17
for i in range(3) :
    print("Python ")
    print("is ")
    print("FUN! ")

for i in range(3) :
    print("Python ")
    print("is ")
print("FUN! ")

for i in range(3) :
    print("Python ")
print("is ")
print("FUN! ")

# 연습문제 3.19
print("맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
print("- 햄버거(입력 b)")
print("- 치킨(입력 c)")
print("- 피자(입력 p)")

menu = input("메뉴를 선택하세요(알파벳 b, c, p 입력) : ")
while menu != "b" and menu != "c" and menu != "p" :
     menu = input("메뉴를 다시 입력하세요(알파벳 b, c, p 입력) : ")

while menu == "b" or menu == "c" or menu == "p" :
    break
if menu == "b" :
    print("햄버거를 선택하였습니다.")
elif menu == "c" :
    print("치킨을 선택하였습니다.")
else :
    print("피자를 선택하였습니다.")

# 연습문제 3.21
 n = int(input("숫자를 입력하세요 : "))
a = 0
if n == 2 :
     print(n, "는 소수입니다")
elif n != 2 and n % 2 == 0 :
    print(n,"는 소수가 아닙니다")
else :
    for i in range(3, n, 2) :
        if n % i == 0 :
            a = a+1
    if a == 0 :
        print(n, "는 소수입니다")
    else :
        print(n, "는 소수가 아닙니다")

# 연습문제 3.23
n = int(input("숫자를 입력하세요 : "))
s = 0
for i in range(1, n+1) :
    s = s + i**2
    
print("결과는", s, "입니다.")

# 연습문제 3.25
m = 5
d = 0
while m <= 30 :
    m += 2
    d += 1
    print("day :", d, " 달팽이의 위치 :", m, "미터")
    
print("우물을 탈출하는 데 걸린 날은", d, "일 입니다.")

# 연습문제 3.27
n = []
for i in range(100, 1000) :
    a = i // 100
    b = (i // 10) % 10
    c = i % 10
    if i == a**3 + b**3 + c**3 :
        n.append(i)
        
print("세 자리의 암스트롱 수 :", n)

# 연습문제 3.29
f = 500
while f >= 50 :
    c = int(input("충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오: "))
    f = f + c
    print("현재 탱크양은", f, "입니다.")
if f < 50 :
    print("경고 : 연료가 10% 미만이니 충전하세요!")

# 연습문제 3.31 (모르는 문제)
