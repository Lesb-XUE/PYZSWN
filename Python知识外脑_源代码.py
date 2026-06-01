"""
Python 知识外脑
包含Python核心知识点和代码示例
"""

# ==================== 基础语法 ====================

# 第一个Python程序
print("Hello, World!")
print("你好，Python！")

# 变量与数据类型
name = "小明"
age = 25
height = 1.75
is_student = True

# ==================== 数据类型 ====================

# 列表(List)
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
fruits.append("orange")

# 元组(Tuple) - 不可变列表
coordinates = (10, 20)

# 字典(Dictionary)
person = {
    "name": "小明",
    "age": 25,
    "city": "北京"
}
print(person["name"])

# 集合(Set) - 无序不重复
colors = {"red", "green", "blue"}

# ==================== 控制流程 ====================

# 条件语句
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
else:
    print("继续加油")

# for循环
fruits = ["apple", "banana"]
for fruit in fruits:
    print(fruit)

# while循环
count = 0
while count < 5:
    print(count)
    count += 1

# ==================== 函数 ====================

def greet(name: str) -> str:
    """向用户打招呼"""
    return f"Hello, {name}"

message = greet("小明")
print(message)

# Lambda函数
add = lambda x, y: x + y
print(add(3, 5))

numbers = [1, 2, 3]
squared = list(map(lambda x: x**2, numbers))

# 默认参数
def power(base, exponent=2):
    return base ** exponent

# ==================== 面向对象 ====================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"我是{self.name}，今年{self.age}岁")

p = Person("小明", 25)
p.introduce()

# 继承
class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def study(self):
        print(f"{self.name}在{self.school}学习")

# ==================== 高级特性 ====================

# 列表推导式
squares = [i**2 for i in range(10)]
even_squares = [i**2 for i in range(10) if i % 2 == 0]

# 字典推导式
word_lengths = {word: len(word) for word in ["apple", "banana"]}

# 生成器
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)

# 装饰器
def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}耗时: {end-start:.2f}秒")
        return result
    return wrapper

@timer
def slow_func():
    import time
    time.sleep(1)

# 上下文管理器
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# ==================== 异常处理 ====================

try:
    result = 10 / 0
except ZeroDivisionError:
    print("不能除以零")
except Exception as e:
    print(f"发生错误: {e}")
finally:
    print("执行完成")

# 自定义异常
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# ==================== 文件操作 ====================

# 读写文件
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Python!")

with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 目录操作
import os
os.makedirs("new_folder", exist_ok=True)
os.listdir(".")

# ==================== 常用库 ====================

# NumPy - 科学计算
import numpy as np
arr = np.array([1, 2, 3, 4])
result = arr * 2
mean = np.mean(arr)

# Pandas - 数据分析
import pandas as pd
data = {
    "Name": ["小明", "小红"],
    "Age": [25, 23]
}
df = pd.DataFrame(data)
print(df.head())

# Matplotlib - 数据可视化
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 15, 25]
plt.plot(x, y)
plt.title("示例图表")
plt.show()

# ==================== 函数式编程 ====================

# map
numbers = [1, 2, 3, 4]

# filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# reduce
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)

# ==================== 实用技巧 ====================

# 解包
a, b, c = [1, 2, 3]
first, *rest = [1, 2, 3, 4, 5]

# 枚举
for index, value in enumerate(["a", "b", "c"]):
    print(f"{index}: {value}")

# zip
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name}: {age}")

# ==================== 魔术方法 ====================

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __len__(self):
        return 2

# ==================== 闭包 ====================

def outer(x):
    def inner(y):
        return x + y
    return inner

add_5 = outer(5)
print(add_5(10))

# ==================== 迭代器 ====================

class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        raise StopIteration

for num in Counter(5):
    print(num)

# ==================== 模块和包 ====================

# 导入方式
from collections import defaultdict
from datetime import datetime as dt

# __name__ == "__main__"
if __name__ == "__main__":
    print("直接运行此脚本")

print("=" * 50)
print("Python 知识外脑 - 学习指南")
print("=" * 50)
print("欢迎使用本示例程序进行 Python 学习。")