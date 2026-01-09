"""
第2章：流程控制 - for 循环
========================

本文件学习目标：
1. 理解循环的概念
2. 掌握 for 循环的基本用法
3. 学会使用 range() 函数
4. 掌握遍历各种数据结构
5. 理解嵌套循环
"""

# ============================================================
# 一、什么是循环？
# ============================================================
#
# 循环让程序可以重复执行某段代码。
#
# 生活中的例子：
# - 每天早上重复：起床 -> 洗漱 -> 吃早餐
# - 数数：1, 2, 3, 4, 5...
#
# Python 中有两种循环：
# - for 循环：遍历序列中的每个元素
# - while 循环：当条件为真时重复执行


# ============================================================
# 二、for 循环基本语法
# ============================================================

# for 循环的语法：
# for 变量 in 序列:
#     循环体（要重复执行的代码）

# 示例：遍历列表
fruits = ["苹果", "香蕉", "橙子", "葡萄"]

print("水果列表:")
for fruit in fruits:
    print(f"  - {fruit}")

# 示例：遍历字符串
print("\n遍历字符串:")
word = "Python"
for char in word:
    print(char, end=" ")
print()  # 换行


# ============================================================
# 三、range() 函数
# ============================================================

# range() 函数生成一个数字序列，常用于 for 循环

# range(n)：生成 0 到 n-1 的数字
print("\nrange(5):")
for i in range(5):
    print(i, end=" ")  # 输出：0 1 2 3 4
print()

# range(start, stop)：生成 start 到 stop-1 的数字
print("\nrange(1, 6):")
for i in range(1, 6):
    print(i, end=" ")  # 输出：1 2 3 4 5
print()

# range(start, stop, step)：指定步长
print("\nrange(0, 10, 2)（偶数）:")
for i in range(0, 10, 2):
    print(i, end=" ")  # 输出：0 2 4 6 8
print()

print("\nrange(10, 0, -1)（倒数）:")
for i in range(10, 0, -1):
    print(i, end=" ")  # 输出：10 9 8 7 6 5 4 3 2 1
print()

# 示例：计算 1 到 100 的和
total = 0
for i in range(1, 101):
    total += i
print(f"\n1 到 100 的和: {total}")  # 5050


# ============================================================
# 四、遍历各种数据结构
# ============================================================

# 1. 遍历列表
print("\n遍历列表:")
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print(f"  数字: {num}")

# 2. 遍历元组
print("\n遍历元组:")
colors = ("红", "绿", "蓝")
for color in colors:
    print(f"  颜色: {color}")

# 3. 遍历字典
print("\n遍历字典:")
student = {"name": "张三", "age": 20, "grade": "大二"}

# 遍历键
print("  遍历键:")
for key in student:
    print(f"    {key}")

# 遍历值
print("  遍历值:")
for value in student.values():
    print(f"    {value}")

# 遍历键值对
print("  遍历键值对:")
for key, value in student.items():
    print(f"    {key}: {value}")

# 4. 遍历集合
print("\n遍历集合:")
unique_numbers = {1, 2, 3, 4, 5}
for num in unique_numbers:
    print(f"  {num}", end=" ")
print()


# ============================================================
# 五、enumerate() 函数
# ============================================================

# enumerate() 可以同时获取索引和值

print("\n使用 enumerate():")
fruits = ["苹果", "香蕉", "橙子"]

for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# 指定起始索引
print("\n指定起始索引为 1:")
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}: {fruit}")


# ============================================================
# 六、zip() 函数
# ============================================================

# zip() 可以同时遍历多个序列

print("\n使用 zip():")
names = ["张三", "李四", "王五"]
ages = [20, 25, 30]
cities = ["北京", "上海", "广州"]

for name, age, city in zip(names, ages, cities):
    print(f"  {name}, {age}岁, 来自{city}")


# ============================================================
# 七、嵌套循环
# ============================================================

# 循环可以嵌套使用

# 示例：打印乘法表
print("\n九九乘法表:")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}x{i}={i*j}", end="\t")
    print()  # 换行

# 示例：遍历二维列表
print("\n遍历二维列表:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(f"{item:3}", end=" ")
    print()


# ============================================================
# 八、列表推导式
# ============================================================

# 列表推导式是创建列表的简洁方式

# 传统方式：创建平方数列表
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(f"\n传统方式: {squares}")

# 列表推导式
squares = [i ** 2 for i in range(1, 6)]
print(f"列表推导式: {squares}")

# 带条件的列表推导式
# 只保留偶数的平方
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(f"偶数的平方: {even_squares}")

# 嵌套列表推导式
# 创建乘法表
multiplication = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"乘法表: {multiplication}")


# ============================================================
# 九、for-else 语句
# ============================================================

# for 循环可以带 else 子句
# 当循环正常结束（没有被 break 中断）时，执行 else 中的代码

print("\nfor-else 示例:")

# 查找质数
def is_prime(n):
    """判断是否为质数"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 使用 for-else 查找
number = 17
print(f"检查 {number} 是否为质数:")

for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
        print(f"  {number} 不是质数，可以被 {i} 整除")
        break
else:
    # 循环正常结束，没有找到因子
    print(f"  {number} 是质数")


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("for 循环综合练习")
    print("=" * 50)

    # 练习1：计算列表元素的和与平均值
    numbers = [23, 45, 67, 89, 12, 34, 56, 78]
    total = 0
    count = 0

    for num in numbers:
        total += num
        count += 1

    average = total / count
    print(f"\n数字列表: {numbers}")
    print(f"总和: {total}")
    print(f"平均值: {average:.2f}")

    # 练习2：找出列表中的最大值和最小值
    max_value = numbers[0]
    min_value = numbers[0]

    for num in numbers:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num

    print(f"最大值: {max_value}")
    print(f"最小值: {min_value}")

    # 练习3：统计字符出现次数
    text = "hello world"
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    print(f"\n字符串: '{text}'")
    print("字符统计:")
    for char, count in char_count.items():
        if char != " ":  # 不统计空格
            print(f"  '{char}': {count}")

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. for 循环语法：for 变量 in 序列:
#
# 2. range() 函数：
#    - range(n)：0 到 n-1
#    - range(start, stop)：start 到 stop-1
#    - range(start, stop, step)：指定步长
#
# 3. 遍历数据结构：
#    - 列表、元组、字符串：直接遍历
#    - 字典：keys(), values(), items()
#
# 4. 常用函数：
#    - enumerate()：获取索引和值
#    - zip()：同时遍历多个序列
#
# 5. 列表推导式：[表达式 for 变量 in 序列 if 条件]
#
# 6. for-else：循环正常结束时执行 else
