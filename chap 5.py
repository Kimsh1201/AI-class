# 연습문제 5.1
list_ex = [10, 20, 30, 40, 50, 60, 70]
high = 5
low = 3

list_ex[low] # 답: 40
list_ex[low + 2] # 답: 60
list_ex[high - low] # 답: 30
list_ex[low - high] # 답: 60
list_ex[-1] # 답: 70
list_ex[-low] # 답: 50
list_ex[2 * 3] # 답: 70
list_ex[2] * 3 # 답: 90
list_ex[5 % 4] # 답: 20
len(list_ex) # 답: 7

# 연습문제 5.3
list1 = [3, 5, 7]
list2 = [2, 3, 4, 5, 6]

for a in list1:
    for b in list2:
        print("{} * {} = {}".format(a, b, a*b))

# 연습문제 5.5
list1 = ["I like", "I love"]
list2 = ["pancakes.", "kiwi juice.", "espresso."]
for a in list1:
    for b in list2:
        print("{} {}".format(a, b))

# 연습문제 5.7
n_list = [10, 20, 30, 50, 60]

v_sum = 0
for i in n_list:
    v_sum += i
print(v_sum)

# 연습문제 5.9
n_list = [10, 20, 30, 50, 60]

v_max = 0
for i in n_list:
    if i > v_max:
        v_max = i
print(v_max)

# 연습문제 5.11
List = list(map(int, input("5개의 수를 입력하세요: ").split()))

print("합: {}".format(sum(List)))
print("평균: {}".format(sum(List) / len(List)))
print("최댓값: {}".format(max(List)))
print("최솟값: {}".format(min(List)))

# 연습문제 5.13
nums = list(map(int, input("10개의 수를 입력하세요: ").split()))
print("합 :", sum(nums))

nums_average = sum(nums) / len(nums)
print("평균 :", nums_average)

nums_sigma = 0
for i in nums:
    nums_sigma += (i - nums_average) ** 2
print("표준편차 : {:.2f}".format((nums_sigma / len(nums)) ** 0.5))

# 연습문제 5.15
greet = "Have a beautiful day."
print(greet[0:4]) # Have
print(greet[7:16]) # beautiful
print(greet[17:20]) # day

# 연습문제 5.17
# (1)
animals = ["dog", "cat", "tiger", "lion"]
print("animals : {}".format(animals))

# (2)
animals = ["dog", "cat", "tiger", "lion"]
animals.append(animals.pop(0))
print("animals : {}".format(animals))

# (3)
animals = ["dog", "cat", "tiger", "lion"]
print("animals : {}".format(animals))
for i in animals:
    print("I love {}.".format(i))

# 연습문제 5.19
s_list = ["abc", "bcd", "abc", "abba", "cddc", "opq", "opq"]
new_s_list = []
for i in s_list:
    if not i in new_s_list:
        new_s_list.append(i)

print(s_list)
print(new_s_list)

# 연습문제 5.21 (모르는 문제)
src = "a2b3c6a2c3f1g1"
print("src = {}".format(src))

for ch in src:
  if ch.isnumeric():
    for i in range(int(ch)):
      print("output = {}".format(ch_old,end=""))
  else:
    ch_old = ch

# 연습문제 5.23
# (1)
def how_many_persons(person_list):
    return len(person_list) // 5

person1 = ["온달", 20, 1, 180.0, 100.0]
person2 = ["이사부", 25, 1, 170.0, 70.0]
person3 = ["평강", 22, 0, 169.0, 60.0]
person4 = ["혁거세", 40, 1, 150.0, 50.0]

person_list = person1 + person3 + person4
n_persons = how_many_persons(person_list)
print(str(n_persons) + "명의 정보가 담겨 있습니다.")

# (2)
def compute_average_age(person_list):
    ages = [person[1] for person in person_list]
    total_age = sum(ages)
    num_persons = len(person_list)
    average_age = total_age / num_persons
    return average_age

person1 = ["온달", 20, 1, 180.0, 100.0]
person2 = ["이사부", 25, 1, 170.0, 70.0]
person3 = ["평강", 22, 0, 169.0, 60.0]
person4 = ["혁거세", 40, 1, 150.0, 50.0]

person_list = [person1, person2, person3, person4] 
average_age = compute_average_age(person_list)
print("평균 나이는 " + str(average_age) + "세입니다.")

# (3)
def count_males_females(person_list):
    male_count = 0
    female_count = 0

    for person in person_list:
        gender = person[2]
        if gender == 1:
            male_count += 1
        elif gender == 0:
            female_count += 1

    return male_count, female_count

person1 = ["온달", 20, 1, 180.0, 100.0]
person2 = ["이사부", 25, 1, 170.0, 70.0]
person3 = ["평강", 22, 0, 169.0, 60.0]
person4 = ["혁거세", 40, 1, 150.0, 50.0]

person_list = [person1, person2, person3, person4]

n_male, n_female = count_males_females(person_list)
print("리스트에는 남자가", n_male, "명, 여자가", n_female, "명입니다.")

# (4)
def display_persons(person_list):
    for i in range(0, len(person_list), 5):
        print(person_list[i:i+5])

person1 = ["온달", 20, 1, 180.0, 100.0]
person2 = ["이사부", 25, 1, 170.0, 70.0]
person3 = ["평강", 22, 0, 169.0, 60.0]
person4 = ["혁거세", 40, 1, 150.0, 50.0]

person_list = person1 + person2 + person3 + person4
display_persons(person_list)
