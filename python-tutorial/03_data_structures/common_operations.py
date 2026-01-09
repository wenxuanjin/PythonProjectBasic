"""
第3章：数据结构 - 常用操作
========================

本文件学习目标：
1. 掌握序列类型的通用操作
2. 学会数据结构之间的转换
3. 掌握常用的内置函数
4. 理解可迭代对象的概念
"""

# ============================================================
# 一、序列类型的通用操作
# ============================================================
#
# 序列类型包括：字符串、列表、元组
# 它们有很多通用的操作方法

print("序列类型的通用操作:")

# 示例数据
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_string = "hello"

# 1. 索引访问
print(f"\n1. 索引访问:")
print(f"  列表[0]: {my_list[0]}")
print(f"  元组[-1]: {my_tuple[-1]}")
print(f"  字符串[1]: {my_string[1]}")

# 2. 切片
print(f"\n2. 切片:")
print(f"  列表[1:4]: {my_list[1:4]}")
print(f"  元组[::2]: {my_tuple[::2]}")
print(f"  字符串[::-1]: {my_string[::-1]}")

# 3. 长度
print(f"\n3. 长度:")
print(f"  len(列表): {len(my_list)}")
print(f"  len(元组): {len(my_tuple)}")
print(f"  len(字符串): {len(my_string)}")

# 4. 成员检测
print(f"\n4. 成员检测:")
print(f"  3 in 列表: {3 in my_list}")
print(f"  6 in 元组: {6 in my_tuple}")
print(f"  'e' in 字符串: {'e' in my_string}")

# 5. 连接
print(f"\n5. 连接:")
print(f"  列表 + [6,7]: {my_list + [6, 7]}")
print(f"  元组 + (6,7): {my_tuple + (6, 7)}")
print(f"  字符串 + ' world': {my_string + ' world'}")

# 6. 重复
print(f"\n6. 重复:")
print(f"  [1,2] * 3: {[1, 2] * 3}")
print(f"  (1,2) * 3: {(1, 2) * 3}")
print(f"  'ab' * 3: {'ab' * 3}")

# 7. 最大值、最小值
print(f"\n7. 最大值、最小值:")
print(f"  max(列表): {max(my_list)}")
print(f"  min(元组): {min(my_tuple)}")
print(f"  max(字符串): {max(my_string)}")  # 按 ASCII 码

# 8. 计数
print(f"\n8. 计数:")
numbers = [1, 2, 2, 3, 3, 3]
print(f"  列表 {numbers} 中 3 的个数: {numbers.count(3)}")
print(f"  字符串 'hello' 中 'l' 的个数: {'hello'.count('l')}")

# 9. 查找索引
print(f"\n9. 查找索引:")
print(f"  列表中 3 的索引: {my_list.index(3)}")
print(f"  字符串中 'l' 的索引: {my_string.index('l')}")


# ============================================================
# 二、数据结构之间的转换
# ============================================================

print("\n" + "=" * 50)
print("数据结构之间的转换:")

# 列表 <-> 元组
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
back_to_list = list(my_tuple)
print(f"\n列表 -> 元组: {my_list} -> {my_tuple}")
print(f"元组 -> 列表: {my_tuple} -> {back_to_list}")

# 列表 <-> 集合
my_list = [1, 2, 2, 3, 3, 3]
my_set = set(my_list)
back_to_list = list(my_set)
print(f"\n列表 -> 集合（去重）: {my_list} -> {my_set}")
print(f"集合 -> 列表: {my_set} -> {back_to_list}")

# 字符串 <-> 列表
my_string = "hello"
char_list = list(my_string)
back_to_string = "".join(char_list)
print(f"\n字符串 -> 列表: '{my_string}' -> {char_list}")
print(f"列表 -> 字符串: {char_list} -> '{back_to_string}'")

# 字典 <-> 列表
my_dict = {"a": 1, "b": 2, "c": 3}
keys_list = list(my_dict.keys())
values_list = list(my_dict.values())
items_list = list(my_dict.items())
print(f"\n字典: {my_dict}")
print(f"键列表: {keys_list}")
print(f"值列表: {values_list}")
print(f"键值对列表: {items_list}")

# 从键值对列表创建字典
pairs = [("x", 10), ("y", 20), ("z", 30)]
new_dict = dict(pairs)
print(f"\n键值对列表 -> 字典: {pairs} -> {new_dict}")


# ============================================================
# 三、常用内置函数
# ============================================================

print("\n" + "=" * 50)
print("常用内置函数:")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# len()：长度
print(f"\nlen({numbers}): {len(numbers)}")

# sum()：求和
print(f"sum({numbers}): {sum(numbers)}")

# max()：最大值
print(f"max({numbers}): {max(numbers)}")

# min()：最小值
print(f"min({numbers}): {min(numbers)}")

# sorted()：排序（返回新列表）
print(f"sorted({numbers}): {sorted(numbers)}")
print(f"sorted(降序): {sorted(numbers, reverse=True)}")

# reversed()：反转（返回迭代器）
print(f"list(reversed({numbers})): {list(reversed(numbers))}")

# enumerate()：枚举
print(f"\nenumerate 示例:")
for i, num in enumerate(numbers[:3]):
    print(f"  索引 {i}: {num}")

# zip()：打包
names = ["张三", "李四", "王五"]
ages = [20, 25, 30]
print(f"\nzip 示例:")
for name, age in zip(names, ages):
    print(f"  {name}: {age}岁")

# map()：映射
squares = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
print(f"\nmap 示例（平方）: {squares}")

# filter()：过滤
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
print(f"filter 示例（偶数）: {evens}")

# all()：全部为真
print(f"\nall([True, True, True]): {all([True, True, True])}")
print(f"all([True, False, True]): {all([True, False, True])}")

# any()：任一为真
print(f"any([False, False, True]): {any([False, False, True])}")
print(f"any([False, False, False]): {any([False, False, False])}")


# ============================================================
# 四、字符串的常用方法
# ============================================================

print("\n" + "=" * 50)
print("字符串的常用方法:")

text = "  Hello, World!  "

# 大小写转换
print(f"\n原字符串: '{text}'")
print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.lower()}'")
print(f"title(): '{text.title()}'")
print(f"capitalize(): '{text.capitalize()}'")

# 去除空白
print(f"\nstrip(): '{text.strip()}'")
print(f"lstrip(): '{text.lstrip()}'")
print(f"rstrip(): '{text.rstrip()}'")

# 查找和替换
text = "Hello, World!"
print(f"\n原字符串: '{text}'")
print(f"find('o'): {text.find('o')}")
print(f"rfind('o'): {text.rfind('o')}")
print(f"replace('World', 'Python'): '{text.replace('World', 'Python')}'")

# 分割和连接
text = "apple,banana,orange"
print(f"\n原字符串: '{text}'")
print(f"split(','): {text.split(',')}")

words = ["apple", "banana", "orange"]
print(f"'-'.join({words}): '{'-'.join(words)}'")

# 判断方法
print(f"\n'123'.isdigit(): {'123'.isdigit()}")
print(f"'abc'.isalpha(): {'abc'.isalpha()}")
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")
print(f"'   '.isspace(): {'   '.isspace()}")
print(f"'Hello'.startswith('He'): {'Hello'.startswith('He')}")
print(f"'Hello'.endswith('lo'): {'Hello'.endswith('lo')}")


# ============================================================
# 五、列表的排序
# ============================================================

print("\n" + "=" * 50)
print("列表的排序:")

# 基本排序
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\n原列表: {numbers}")

# sort()：原地排序
numbers_copy = numbers.copy()
numbers_copy.sort()
print(f"sort() 后: {numbers_copy}")

# sorted()：返回新列表
sorted_numbers = sorted(numbers)
print(f"sorted() 返回: {sorted_numbers}")
print(f"原列表不变: {numbers}")

# 降序排序
print(f"降序: {sorted(numbers, reverse=True)}")

# 按自定义规则排序
words = ["banana", "apple", "cherry", "date"]
print(f"\n单词列表: {words}")
print(f"按字母排序: {sorted(words)}")
print(f"按长度排序: {sorted(words, key=len)}")

# 复杂对象排序
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78},
]
print(f"\n学生列表: {students}")
sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
print(f"按成绩排序: {sorted_students}")


# ============================================================
# 六、可迭代对象
# ============================================================

print("\n" + "=" * 50)
print("可迭代对象:")

# 可迭代对象是可以用 for 循环遍历的对象
# 包括：字符串、列表、元组、字典、集合、range 等

# 检查是否可迭代
from collections.abc import Iterable

print(f"\n列表可迭代: {isinstance([1,2,3], Iterable)}")
print(f"字符串可迭代: {isinstance('hello', Iterable)}")
print(f"整数可迭代: {isinstance(123, Iterable)}")

# 迭代器
my_list = [1, 2, 3]
my_iter = iter(my_list)  # 获取迭代器
print(f"\n迭代器:")
print(f"  next(): {next(my_iter)}")
print(f"  next(): {next(my_iter)}")
print(f"  next(): {next(my_iter)}")
# print(next(my_iter))  # StopIteration


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("数据结构综合练习")
    print("=" * 50)

    # 练习1：统计单词频率
    print("\n统计单词频率:")
    text = "apple banana apple cherry banana apple"
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    print(f"文本: '{text}'")
    print(f"单词频率: {word_count}")

    # 练习2：找出两个列表的差异
    print("\n找出列表差异:")
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    only_in_1 = [x for x in list1 if x not in list2]
    only_in_2 = [x for x in list2 if x not in list1]
    print(f"列表1: {list1}")
    print(f"列表2: {list2}")
    print(f"只在列表1中: {only_in_1}")
    print(f"只在列表2中: {only_in_2}")

    # 练习3：矩阵转置
    print("\n矩阵转置:")
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print("原矩阵:")
    for row in matrix:
        print(f"  {row}")
    print("转置后:")
    for row in transposed:
        print(f"  {row}")

    # 练习4：扁平化嵌套列表
    print("\n扁平化嵌套列表:")
    nested = [[1, 2], [3, 4], [5, 6]]
    flattened = [item for sublist in nested for item in sublist]
    print(f"嵌套列表: {nested}")
    print(f"扁平化后: {flattened}")

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. 序列通用操作：
#    - 索引、切片、长度、成员检测
#    - 连接、重复、最大最小值
#
# 2. 数据结构转换：
#    - list()、tuple()、set()、dict()
#    - str.split()、str.join()
#
# 3. 常用内置函数：
#    - len()、sum()、max()、min()
#    - sorted()、reversed()
#    - enumerate()、zip()
#    - map()、filter()
#    - all()、any()
#
# 4. 字符串方法：
#    - 大小写：upper()、lower()、title()
#    - 去空白：strip()、lstrip()、rstrip()
#    - 查找替换：find()、replace()
#    - 分割连接：split()、join()
#
# 5. 排序：
#    - sort()：原地排序
#    - sorted()：返回新列表
#    - key 参数：自定义排序规则
#
# 6. 可迭代对象：可以用 for 循环遍历的对象
