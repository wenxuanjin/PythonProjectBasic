"""
第10章：标准答案 - 基础语法练习答案
==================================

本文件包含 09_practice/basic_exercises.md 中所有练习题的标准答案。
"""

# ============================================================
# 一、变量与数据类型（10题）
# ============================================================

print("=" * 60)
print("一、变量与数据类型")
print("=" * 60)

# 练习 1.1：变量交换
print("\n练习 1.1：变量交换")
a = 10
b = 20
print(f"交换前: a = {a}, b = {b}")
a, b = b, a  # Python 特有的交换方式
print(f"交换后: a = {a}, b = {b}")


# 练习 1.2：类型判断
print("\n练习 1.2：类型判断")
x = "Hello"
print(f"x 的类型是 {type(x).__name__}")


# 练习 1.3：类型转换
print("\n练习 1.3：类型转换")
s = "123.45"
f = float(s)  # 字符串转浮点数
i = int(f)    # 浮点数转整数
print(f"字符串: {s}")
print(f"浮点数: {f}")
print(f"整数: {i}")


# 练习 1.4：字符串拼接
print("\n练习 1.4：字符串拼接")
name = "张三"
age = 25

# 方式1：+ 拼接
result1 = "我叫" + name + "，今年" + str(age) + "岁"
print(f"方式1: {result1}")

# 方式2：format()
result2 = "我叫{}，今年{}岁".format(name, age)
print(f"方式2: {result2}")

# 方式3：f-string（推荐）
result3 = f"我叫{name}，今年{age}岁"
print(f"方式3: {result3}")


# 练习 1.5：字符串操作
print("\n练习 1.5：字符串操作")
s = "  Hello, Python!  "
print(f"原字符串: '{s}'")
print(f"去除空格: '{s.strip()}'")
print(f"转大写: '{s.upper()}'")
print(f"'o' 出现次数: {s.count('o')}")
print(f"替换后: '{s.replace('Python', 'World')}'")


# 练习 1.6：数字格式化
print("\n练习 1.6：数字格式化")
num = 3.14159265
print(f"保留2位小数: {num:.2f}")
print(f"保留4位小数: {num:.4f}")
percent = 0.75
print(f"百分比: {percent:.1%}")


# 练习 1.7：布尔运算
print("\n练习 1.7：布尔运算")
a = 10
b = 5
c = 10
print(f"a = {a}, b = {b}, c = {c}")
print(f"a > b and b > 0: {a > b and b > 0}")      # True
print(f"a == c or b > a: {a == c or b > a}")      # True
print(f"not (a == b): {not (a == b)}")            # True
print(f"a >= c and b <= a: {a >= c and b <= a}")  # True


# 练习 1.8：空值判断
print("\n练习 1.8：空值判断")


def is_empty(value):
    """判断值是否为空"""
    if value is None:
        return True
    if isinstance(value, str) and value.strip() == "":
        return True
    if isinstance(value, (list, dict, set, tuple)) and len(value) == 0:
        return True
    return False


test_values = [None, "", "  ", [], {}, "hello", [1, 2, 3]]
for v in test_values:
    print(f"is_empty({repr(v)}): {is_empty(v)}")


# 练习 1.9：进制转换
print("\n练习 1.9：进制转换")
num = 255
print(f"十进制: {num}")
print(f"二进制: {bin(num)}")
print(f"八进制: {oct(num)}")
print(f"十六进制: {hex(num)}")


# 练习 1.10：字符串切片
print("\n练习 1.10：字符串切片")
s = "Python Programming"
print(f"原字符串: '{s}'")
print(f"前6个字符: '{s[:6]}'")
print(f"后11个字符: '{s[-11:]}'")
print(f"反转: '{s[::-1]}'")
print(f"每隔一个: '{s[::2]}'")


# ============================================================
# 二、流程控制（10题）
# ============================================================

print("\n" + "=" * 60)
print("二、流程控制")
print("=" * 60)


# 练习 2.1：成绩等级
print("\n练习 2.1：成绩等级")


def get_grade(score):
    """根据分数返回等级"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


test_scores = [95, 85, 75, 65, 55]
for score in test_scores:
    print(f"分数 {score} -> 等级 {get_grade(score)}")


# 练习 2.2：闰年判断
print("\n练习 2.2：闰年判断")


def is_leap_year(year):
    """判断是否为闰年"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


test_years = [2000, 2020, 2021, 2024, 1900]
for year in test_years:
    result = "是" if is_leap_year(year) else "不是"
    print(f"{year} {result}闰年")


# 练习 2.3：九九乘法表
print("\n练习 2.3：九九乘法表")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}x{i}={i*j}", end="\t")
    print()


# 练习 2.4：求和
print("\n练习 2.4：求和 1+2+...+100")
total = sum(range(1, 101))
print(f"结果: {total}")


# 练习 2.5：阶乘
print("\n练习 2.5：阶乘")


def factorial(n):
    """计算 n 的阶乘"""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


for n in range(6):
    print(f"{n}! = {factorial(n)}")


# 练习 2.6：质数判断
print("\n练习 2.6：质数判断")


def is_prime(n):
    """判断是否为质数"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


test_nums = [1, 2, 3, 4, 5, 17, 20, 23]
for num in test_nums:
    result = "是" if is_prime(num) else "不是"
    print(f"{num} {result}质数")


# 练习 2.7：找出质数
print("\n练习 2.7：1-100 之间的质数")
primes = [n for n in range(2, 101) if is_prime(n)]
print(primes)


# 练习 2.8：猜数字（模拟）
print("\n练习 2.8：猜数字游戏（模拟）")
import random


def guess_number_game():
    """猜数字游戏"""
    secret = random.randint(1, 100)
    guesses = [50, 75, 62, 68, 65, 67, 66]  # 模拟猜测

    print(f"(答案是 {secret})")
    for guess in guesses:
        print(f"猜测: {guess}", end=" -> ")
        if guess == secret:
            print("猜对了!")
            break
        elif guess < secret:
            print("太小了")
        else:
            print("太大了")


guess_number_game()


# 练习 2.9：水仙花数
print("\n练习 2.9：水仙花数")
narcissistic = []
for num in range(100, 1000):
    digits = [int(d) for d in str(num)]
    if sum(d ** 3 for d in digits) == num:
        narcissistic.append(num)
print(f"三位数的水仙花数: {narcissistic}")


# 练习 2.10：斐波那契数列
print("\n练习 2.10：斐波那契数列前20项")
fib = [0, 1]
for i in range(2, 20):
    fib.append(fib[i-1] + fib[i-2])
print(fib)


# ============================================================
# 三、数据结构（10题）
# ============================================================

print("\n" + "=" * 60)
print("三、数据结构")
print("=" * 60)


# 练习 3.1：列表操作
print("\n练习 3.1：列表操作")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"原列表: {numbers}")

numbers.append(7)
print(f"添加7: {numbers}")

numbers.insert(2, 0)
print(f"索引2插入0: {numbers}")

numbers.remove(1)
print(f"删除第一个1: {numbers}")

numbers.sort()
print(f"排序: {numbers}")

numbers.reverse()
print(f"反转: {numbers}")


# 练习 3.2：列表去重
print("\n练习 3.2：列表去重（保持顺序）")
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]


def remove_duplicates(lst):
    """去重并保持顺序"""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


print(f"原列表: {numbers}")
print(f"去重后: {remove_duplicates(numbers)}")


# 练习 3.3：列表推导式
print("\n练习 3.3：列表推导式")
# 1-10 的平方
squares = [x ** 2 for x in range(1, 11)]
print(f"1-10的平方: {squares}")

# 筛选偶数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(f"偶数: {evens}")

# 转大写
words = ["hello", "world", "python"]
upper_words = [w.upper() for w in words]
print(f"大写: {upper_words}")


# 练习 3.4：字典操作
print("\n练习 3.4：字典操作")
student = {"name": "张三", "age": 20, "score": 85}
print(f"原字典: {student}")

student["city"] = "北京"
print(f"添加city: {student}")

student["score"] = 90
print(f"修改score: {student}")

del student["age"]
print(f"删除age: {student}")

print("遍历键值对:")
for key, value in student.items():
    print(f"  {key}: {value}")


# 练习 3.5：字典统计
print("\n练习 3.5：字典统计字符")
text = "hello world"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(f"字符串: '{text}'")
print(f"统计: {char_count}")


# 练习 3.6：集合操作
print("\n练习 3.6：集合操作")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(f"集合A: {set_a}")
print(f"集合B: {set_b}")
print(f"并集: {set_a | set_b}")
print(f"交集: {set_a & set_b}")
print(f"差集(A-B): {set_a - set_b}")
print(f"对称差集: {set_a ^ set_b}")


# 练习 3.7：元组解包
print("\n练习 3.7：元组解包")
a, b, c = 1, 2, 3
print(f"交换前: a={a}, b={b}, c={c}")
a, b, c = c, a, b
print(f"交换后: a={a}, b={b}, c={c}")


# 练习 3.8：嵌套数据结构
print("\n练习 3.8：嵌套列表求和")
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
total = sum(sum(inner) for inner in nested)
print(f"嵌套列表: {nested}")
print(f"总和: {total}")


# 练习 3.9：排序
print("\n练习 3.9：按成绩排序")
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78},
]
sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
print("按成绩降序:")
for s in sorted_students:
    print(f"  {s['name']}: {s['score']}")


# 练习 3.10：合并字典
print("\n练习 3.10：合并字典（值相加）")
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 3, "c": 4, "d": 5}


def merge_dicts(d1, d2):
    """合并字典，相同键的值相加"""
    result = d1.copy()
    for key, value in d2.items():
        result[key] = result.get(key, 0) + value
    return result


merged = merge_dicts(dict1, dict2)
print(f"dict1: {dict1}")
print(f"dict2: {dict2}")
print(f"合并: {merged}")


# ============================================================
# 四、函数（5题）
# ============================================================

print("\n" + "=" * 60)
print("四、函数")
print("=" * 60)


# 练习 4.1：计算器函数
print("\n练习 4.1：计算器函数")


def calculator(a, b, operator):
    """简单计算器"""
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "除数不能为0"
        return a / b
    else:
        return "不支持的运算符"


print(f"10 + 3 = {calculator(10, 3, '+')}")
print(f"10 - 3 = {calculator(10, 3, '-')}")
print(f"10 * 3 = {calculator(10, 3, '*')}")
print(f"10 / 3 = {calculator(10, 3, '/')}")


# 练习 4.2：递归求和
print("\n练习 4.2：递归求和")


def recursive_sum(n):
    """递归计算 1+2+...+n"""
    if n == 1:
        return 1
    return n + recursive_sum(n - 1)


print(f"1+2+...+10 = {recursive_sum(10)}")


# 练习 4.3：可变参数
print("\n练习 4.3：可变参数求平均值")


def average(*args):
    """计算平均值"""
    if not args:
        return 0
    return sum(args) / len(args)


print(f"average(1, 2, 3) = {average(1, 2, 3)}")
print(f"average(10, 20, 30, 40, 50) = {average(10, 20, 30, 40, 50)}")


# 练习 4.4：装饰器
print("\n练习 4.4：计时装饰器")
import time


def timer(func):
    """计时装饰器"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 执行时间: {end - start:.6f} 秒")
        return result
    return wrapper


@timer
def slow_function():
    """模拟耗时函数"""
    time.sleep(0.1)
    return "完成"


slow_function()


# 练习 4.5：闭包
print("\n练习 4.5：闭包计数器")


def make_counter():
    """创建计数器"""
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


counter = make_counter()
print(f"第1次调用: {counter()}")
print(f"第2次调用: {counter()}")
print(f"第3次调用: {counter()}")


print("\n" + "=" * 60)
print("基础语法练习答案完成！")
print("=" * 60)
