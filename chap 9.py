# 연습문제 9.1
n = 123
print(n.__add__(334)) #(1)
print(n.__sub__(334)) #(2)
print(n.__mul__(334)) #(3)
print(n.__truediv__(3)) #(4)

# 연습문제 9.3
s = 'Hello World~'
print(s.pop()) # 사용 불가능
print(s.sort()) # 사용 불가능
print(s.append()) # 사용 불가능
print(s.upper()) # 사용 가능
print(s.insert()) # 사용 불가능
print(s.remove()) # 사용 불가능

# 연습문제 9.5
a=1
b=1
c=2
d=3
e=3

print("a와 b가 같은 객체인가?", a is b)
print("b와 c가 같은 객체인가?", b is c)
print("c와 d가 같은 객체인가?", c is d)
print("d와 e가 같은 객체인가?", d is e)


# 연습문제 9.7
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) :
        return '이름은 {}이고, 나이는 {}살 입니다.'.format(my_dog.name, my_dog.age)

my_dog = Dog("Mango", 3)
print(my_dog)

# 연습문제 9.9
class Counter :
    def __init__(self, number = 0) :
        if number >= 100 or number <= -1 :
            self.__number = 0
        else :
            self.__number = number

    def reset(self) :
        self.__number = 0

    def inc(self) :
        self.__number += 1
        if self.__number > 100 :
            self.__number = 0

    def dec(self) :
        self.__number -= 1
        if self.__number < -1 :
            self.__number = 0

    def __str__(self) : 
        return 'C({})'.format(self.__number)

    def __add__(self, other) :
        return 'C({})'.format(self.__number + other.__number)

    def __sub__(self, other) :
        return 'C({})'.format(self.__number - other.__number)

c1 = Counter(10)
c2 = Counter(20)
c3 = c1+ c2
c4 = c1 - c2
print('c3 =', c3)
print('c4 =', c4)

# 연습문제 9.11
class Student :
    def __init__(self, name, student_id, korean_quiz=0, math_quiz=0, science_quiz=0) :
        self.__name = name
        self.__student_id = student_id
        self.__korean_quiz = korean_quiz
        self.__math_quiz = math_quiz
        self.__science_quiz = science_quiz
        self.__total_score = korean_quiz + math_quiz + science_quiz

    def __str__(self) :
        return '이름: {}, 학번: {}\n국어: {}, 수학: {}, 과학: {}\n합계: {}, 평균: {}'.format(
        self.__name, self.__student_id,
        self.__korean_quiz, self.__math_quiz, self.__science_quiz,
        self.__total_score, self.get_avg_score())

    def get_name(self) :
        return self.__name

    def get_korean_quiz(self) :
        return self.__korean_quiz

    def get_math_quiz(self) :
        return self.__math_quiz

    def get_science_quiz(self) :
        return self.__science_quiz

    def set_korean_quiz(self, score) :
        self.__korean_quiz = score
        self.__total_score = self.__korean_quiz + self.__math_quiz + self.__science_quiz

    def set_math_quiz(self, score) :
        self.__math_quiz = score
        self.__total_score = self.__korean_quiz + self.__math_quiz + self.__science_quiz

    def set_science_quiz(self, score) :
        self.__science_quiz = score
        self.__total_score = self.__korean_quiz + self.__math_quiz + self.__science_quiz

    def set_total_score(self) :
        return self.__total_score

    def get_avg_score(self) :
        return self.__total_score / 3

name = input('학생의 이름을 입력하세요 : ')
student_id = input('학생의 학번을 입력하세요 : ')
student = Student(name, student_id)
korean_quiz = int(input('학생의 국어 성적을 입력하세요 : '))
math_quiz = int(input('학생의 수학 성적을 입력하세요 : '))
science_quiz = int(input('학생의 과학 성적을 입력하세요 : '))

student.set_korean_quiz(korean_quiz)
student.set_math_quiz(math_quiz)
student.set_science_quiz(science_quiz)

print(student)

# 연습문제 9.13
class Rectangle:
    def __init__(self, x, y, width, height) :
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def __str__(self) :
        return 'Rectangle : (x = {}, y = {}, w = {}, h = {}), 면적 : {}'.format(self.__x, self.__y, self.__width, self.__height, self.__width * self.__height)

    def set_x(self, x) :
        self.__x = x

    def get_x(self) :
        return self.__x

    def set_y(self, y) :
        self.__y = y

    def get_y(self) :
        return self.__y

    def set_width(self, width) :
        self.___width = width

    def get_width(self) :
        return self.__width

    def set_height(self, height) :
        self.__height = height

    def get_height(self) :
        return self.__height

    def area(self) :
        return self.__width * self.__height

    def overlaps(self, r) :
        if (self.__x < r.get_x() + r.get_width() and self.__x + self.__width > r.get_x() and self.__y < r.get_y() + r.get_height() and self.__y + self.__height > r.get_y()) :
            return True
        else:
            return False

    def contains(self, r):
        if (self.__x <= r.get_x() and self.__x + self.__width >= r.get_x() + r.get_width() and self.__y <= r.get_y() and self.__y + self.__height >= r.get_y() + r.get_height()) :
            return True
        else:
            return False

r1 = Rectangle(0, 0, 100, 100)
r2 = Rectangle(0, -10, 10, 10)
r3 = Rectangle(-100, 0, 120, 100)

print('r1 =', r1)
print('r2 =', r2)
print('r3 =', r3)

print('r1 contains r2 :', r1.contains(r2))
print('r1 contains r3 :', r1.contains(r3))
print('r1 overlaps r2 :', r1.overlaps(r2))
print('r1 overlaps r3 :', r1.overlaps(r3))
