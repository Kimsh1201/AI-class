# 연습문제 4.1
def my_greet() :
    print("환영합니다.")

my_greet()
my_greet()

# 연습문제 4.3
def max2(m, n):
    if m < n:
        return n
    else:
        return m

def min2(m, n):
    if m > n:
        return n
    else:
        return m

print("100과 200중 큰 수는 :", max2(100, 200))
print("100과 200중 작은 수는 :", min2(100, 200))

# 연습문제 4.5
def inch2cm(i) :
    return i * 2.54

for i in range(1, 6) :
    print("{} 인치 = {} 킬로미터".format(i, inch2cm(i)))

# 연습문제 4.7
def mean3(a, b, c) :
    return (a+b+c)/3

def max3(a, b, c) :
    return max(a, b, c)

def min3(a, b, c) :
    return min(a, b, c)

a, b, c = map(int,input("세 수를 입력하시오 : ").split(" "))
print("{}, {}, {}의 평균값은 {}".format(a, b, c, mean3(a, b, c)))
print("{}, {}, {}의 최댓값은 {}".format(a, b, c, max3(a, b, c)))
print("{}, {}, {}의 최솟값은 {}".format(a, b, c, min3(a, b, c)))

# 연습문제 4.9
def mean_of_n(*nums) :
    return sum(nums)/len(nums)

def max_of_n(*nums) :
    return max(nums)

def min_of_n(*nums) :
    return min(nums)

nums = list(map(int,input("정수를 여러 개 입력하시오 : ").split(" ")))
print("평균값은 {}".format(mean_of_n(*nums)))
print("최댓값은 {}".format(max_of_n(*nums)))
print("최솟값은 {}".format(min_of_n(*nums)))

# 연습문제 4.11
def area(x1, y1, x2, y2) :
    return (x2-x1) * (y2-y1) / 2

x1 = int(input("x1 좌표를 입력하시오 : ",))
y1 = int(input("y1 좌표를 입력하시오 : ",))
x2 = int(input("x2 좌표를 입력하시오 : ",))
y2 = int(input("y2 좌표를 입력하시오 : ",))
print("직각삼각형의 면적은 : {}".format(area(x1, y1, x2, y2)))

# 연습문제 4.13
# (1) 모서리의 길이가 12인 정육면체
def cube_volume(s) :
    return s ** 3

print(cube_volume(12))

# (2) 모서리의 길이가 20인 정육면체
def cube_volume(s) :
    return s ** 3

print(cube_volume(20))

# (3) 가로, 세로, 길이가 각각 3, 5, 6인 정육면체
def cube_volume(w, d, h) :
    return w* d * h

print(cube_volume(3, 5, 6))

# (4) 반지름과 높이가 각각 20, 10인 원뿔
pi = 3.14
def cone_volume(r, h) :
    return (1/3) * pi * (r**2) * h

print(cone_volume(20, 10))

# (5) 반지름이 15인 구
pi = 3.14
def sphere_volume(r) :
    return (4/3) * pi * (r**3)

print(sphere_volume(15))

# (6) 반지름과 높이가 각각 20, 10인 원기둥
pi = 3.14
def cylinder_volume(r, h) :
    return pi * (r**2) * h

print(cylinder_volume(20, 10))

# 연습문제 4.15
def my_sort(*nums) :
    a = list(nums)
    a.sort()
    return a

print(my_sort(45, 3, 4, 56, 5)) # 혹은 print(my_sort(9, 8, 7, 6, 5, 4, 3))

# 연습문제 4.17
def sum_range(n1, n2) :
    a = list(range(n1, n2 +1))
    return sum(a)

print("10에서 20까지의 정수의 합 :", sum_range(10, 20))
print("40에서 100까지의 정수의 합 :", sum_range(40, 100))

# 연습문제 4.19
def fibo(n) :
    if n <= 1 :
        return 1
    else :
        return(fibo(n-1) + fibo(n-2))

n = int(input("fibo(n)의 n을 입력하세요 : "))
print("fibo{} = {}".format(n, fibo(n)))

# 연습문제 4.21
RRN = input("주민등록번호 첫 6숫자 형식 입력 : ")
if int(RRN[0:2]) >= 50 :
    YY = "19" + RRN[0:2]
else :
    YY = "20" + RRN[0:2]

print("{}년 {}월 {}일".format(YY, RRN[2:4], RRN[4:6]))

# 연습문제 4.23
import math
pi = math.pi

def area_and_circumference(r):
    area = pi * (r**2)
    circumference = 2 * pi * r
    return area, circumference

while True:
    r = float(input("반지름을 입력하세요 : "))
    
    if r >= 0:
        tuple = area_and_circumference(r)
        print("넓이 : {:7.3f}, 둘레 : {:7.3f}".format(tuple[0], tuple[1]))
    else:
        print("프로그램을 종료합니다.")
        break

# 연습문제 4.25
s1 = "Kang Young Min"
s2 = " Kang Young-Min"
s3 = "Park Dong Min"
s4 = " Park Dong-Yun"

L = [s1, s2, s3, s4]
for i in range(4) :
    result = L[i].replace(" ", "")
    result = result.replace("-", "")
    result = result.upper()
    print("{}(은)는 {}(으)로 수정됨".format(L[i], result))
    L[i] = result

for i in L :
    print("{} : {} 개의 N이 나타남".format(i, i.count("N")))


# 연습문제 4.27
def unit_fraction(frac) :
    n = int(1/frac)
    r1 = 1/n
    r2 = 1/(n+1)
    if abs(r1 - frac) < abs(r2 - frac) :
        return n
    else :
        return n+1

num = float(input("1보다 작고 0보다 큰 소수를 입력하세요 : "))
n = unit_fraction(num)
print("가장 가까운 단위분수는 1/{}이며, 이 값은 {}입니다.".format(n, 1/n))
