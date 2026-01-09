"""
第3章：数据结构 - 列表（List）
============================

本文件学习目标：
1. 理解列表的概念和特点
2. 掌握列表的创建方式
3. 掌握列表的增删改查操作
4. 学会列表的常用方法
5. 理解列表的切片操作
"""

# ============================================================
# 一、什么是列表？
# ============================================================
#
# 列表（List）是 Python 中最常用的数据结构之一。
#
# 列表的特点：
# 1. 有序：元素按照添加顺序排列
# 2. 可变：可以修改、添加、删除元素
# 3. 可重复：可以包含重复的元素
# 4. 可以包含不同类型的元素
#
# 列表用方括号 [] 表示，元素之间用逗号分隔。


# ============================================================
# 二、创建列表
# ============================================================

# 方式1：直接创建
fruits = ["苹果", "香蕉", "橙子"]
print("水果列表:", fruits)

# 方式2：创建空列表
empty_list = []
print("空列表:", empty_list)

# 方式3：使用 list() 函数
numbers = list(range(1, 6))
print("数字列表:", numbers)

# 方式4：列表推导式
squares = [x ** 2 for x in range(1, 6)]
print("平方列表:", squares)

# 列表可以包含不同类型的元素
mixed = [1, "hello", 3.14, True, None]
print("混合列表:", mixed)

# 列表可以嵌套
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("嵌套列表:", matrix)


# ============================================================
# 三、访问列表元素
# ============================================================

fruits = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]

print("\n访问列表元素:")

# 通过索引访问（索引从 0 开始）
print(f"第一个元素: {fruits[0]}")   # 苹果
print(f"第二个元素: {fruits[1]}")   # 香蕉
print(f"最后一个元素: {fruits[-1]}")  # 西瓜
print(f"倒数第二个: {fruits[-2]}")   # 葡萄

# 获取列表长度
print(f"列表长度: {len(fruits)}")

# 检查元素是否存在
print(f"'苹果' 在列表中: {'苹果' in fruits}")
print(f"'芒果' 在列表中: {'芒果' in fruits}")


# ============================================================
# 四、列表切片
# ============================================================

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\n列表切片:")
print(f"原列表: {numbers}")

# 基本切片：list[start:stop]
print(f"[2:5]: {numbers[2:5]}")     # [2, 3, 4]
print(f"[:5]: {numbers[:5]}")       # [0, 1, 2, 3, 4]
print(f"[5:]: {numbers[5:]}")       # [5, 6, 7, 8, 9]
print(f"[-3:]: {numbers[-3:]}")     # [7, 8, 9]

# 带步长的切片：list[start:stop:step]
print(f"[::2]: {numbers[::2]}")     # [0, 2, 4, 6, 8]
print(f"[1::2]: {numbers[1::2]}")   # [1, 3, 5, 7, 9]
print(f"[::-1]: {numbers[::-1]}")   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] 反转

# 切片创建的是新列表（浅拷贝）
copy_list = numbers[:]
print(f"复制列表: {copy_list}")


# ============================================================
# 五、修改列表元素
# ============================================================

fruits = ["苹果", "香蕉", "橙子"]
print("\n修改列表元素:")
print(f"原列表: {fruits}")

# 修改单个元素
fruits[1] = "草莓"
print(f"修改后: {fruits}")

# 修改多个元素（切片赋值）
fruits[1:3] = ["葡萄", "西瓜", "芒果"]
print(f"切片修改后: {fruits}")


# ============================================================
# 六、添加元素
# ============================================================

fruits = ["苹果", "香蕉"]
print("\n添加元素:")
print(f"原列表: {fruits}")

# append()：在末尾添加一个元素
fruits.append("橙子")
print(f"append 后: {fruits}")

# insert()：在指定位置插入元素
fruits.insert(1, "草莓")  # 在索引 1 处插入
print(f"insert 后: {fruits}")

# extend()：添加多个元素
fruits.extend(["葡萄", "西瓜"])
print(f"extend 后: {fruits}")

# 使用 + 连接列表（创建新列表）
more_fruits = fruits + ["芒果", "榴莲"]
print(f"+ 连接后: {more_fruits}")

# 使用 * 重复列表
repeated = ["a", "b"] * 3
print(f"* 重复: {repeated}")


# ============================================================
# 七、删除元素
# ============================================================

fruits = ["苹果", "香蕉", "橙子", "香蕉", "葡萄"]
print("\n删除元素:")
print(f"原列表: {fruits}")

# remove()：删除第一个匹配的元素
fruits.remove("香蕉")
print(f"remove 后: {fruits}")

# pop()：删除并返回指定位置的元素（默认最后一个）
removed = fruits.pop()
print(f"pop() 返回: {removed}, 列表: {fruits}")

removed = fruits.pop(1)
print(f"pop(1) 返回: {removed}, 列表: {fruits}")

# del：删除指定位置的元素
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
del fruits[1]
print(f"del 后: {fruits}")

# del 也可以删除切片
del fruits[1:]
print(f"del 切片后: {fruits}")

# clear()：清空列表
fruits = ["苹果", "香蕉", "橙子"]
fruits.clear()
print(f"clear 后: {fruits}")


# ============================================================
# 八、列表常用方法
# ============================================================

print("\n列表常用方法:")

# index()：查找元素的索引
fruits = ["苹果", "香蕉", "橙子", "香蕉"]
print(f"列表: {fruits}")
print(f"'香蕉' 的索引: {fruits.index('香蕉')}")  # 返回第一个匹配的索引

# count()：统计元素出现次数
print(f"'香蕉' 出现次数: {fruits.count('香蕉')}")

# sort()：排序（原地修改）
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\n原列表: {numbers}")
numbers.sort()
print(f"sort() 后: {numbers}")

numbers.sort(reverse=True)
print(f"降序排序: {numbers}")

# sorted()：排序（返回新列表）
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(f"\n原列表: {numbers}")
print(f"sorted() 返回: {sorted_numbers}")

# reverse()：反转列表（原地修改）
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(f"\nreverse() 后: {numbers}")

# copy()：复制列表
original = [1, 2, 3]
copied = original.copy()
print(f"\n原列表: {original}")
print(f"复制列表: {copied}")


# ============================================================
# 九、列表推导式
# ============================================================

print("\n列表推导式:")

# 基本形式
squares = [x ** 2 for x in range(1, 6)]
print(f"平方数: {squares}")

# 带条件
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(f"偶数的平方: {even_squares}")

# 带 if-else
labels = ["偶数" if x % 2 == 0 else "奇数" for x in range(1, 6)]
print(f"奇偶标签: {labels}")

# 嵌套循环
pairs = [(x, y) for x in range(1, 4) for y in range(1, 4)]
print(f"数对: {pairs}")

# 处理字符串
words = ["Hello", "World", "Python"]
upper_words = [word.upper() for word in words]
print(f"大写: {upper_words}")


# ============================================================
# 十、列表的注意事项
# ============================================================

print("\n列表注意事项:")

# 1. 列表是可变对象，赋值是引用
list1 = [1, 2, 3]
list2 = list1  # list2 和 list1 指向同一个列表
list2.append(4)
print(f"list1: {list1}")  # [1, 2, 3, 4]
print(f"list2: {list2}")  # [1, 2, 3, 4]

# 如果要复制，使用 copy() 或切片
list1 = [1, 2, 3]
list2 = list1.copy()  # 或 list2 = list1[:]
list2.append(4)
print(f"\n复制后:")
print(f"list1: {list1}")  # [1, 2, 3]
print(f"list2: {list2}")  # [1, 2, 3, 4]

# 2. 嵌套列表的深拷贝
import copy
nested = [[1, 2], [3, 4]]
shallow = nested.copy()  # 浅拷贝
deep = copy.deepcopy(nested)  # 深拷贝

nested[0][0] = 100
print(f"\n嵌套列表修改后:")
print(f"原列表: {nested}")
print(f"浅拷贝: {shallow}")  # 也被修改了
print(f"深拷贝: {deep}")     # 没有被修改


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("列表综合练习")
    print("=" * 50)

    # 练习1：学生成绩管理
    print("\n学生成绩管理:")
    scores = [85, 92, 78, 90, 88, 76, 95, 82]
    print(f"成绩列表: {scores}")
    print(f"最高分: {max(scores)}")
    print(f"最低分: {min(scores)}")
    print(f"平均分: {sum(scores) / len(scores):.2f}")
    print(f"及格人数: {len([s for s in scores if s >= 60])}")

    # 练习2：列表去重
    print("\n列表去重:")
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    unique = list(set(numbers))  # 使用集合去重
    print(f"原列表: {numbers}")
    print(f"去重后: {unique}")

    # 练习3：找出两个列表的交集
    print("\n列表交集:")
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    intersection = [x for x in list_a if x in list_b]
    print(f"列表A: {list_a}")
    print(f"列表B: {list_b}")
    print(f"交集: {intersection}")

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. 列表特点：有序、可变、可重复、可包含不同类型
#
# 2. 创建列表：[]、list()、列表推导式
#
# 3. 访问元素：索引（从0开始）、负索引、切片
#
# 4. 添加元素：append()、insert()、extend()
#
# 5. 删除元素：remove()、pop()、del、clear()
#
# 6. 常用方法：
#    - index()：查找索引
#    - count()：统计次数
#    - sort()：排序
#    - reverse()：反转
#    - copy()：复制
#
# 7. 列表推导式：[表达式 for 变量 in 序列 if 条件]
#
# 8. 注意：列表赋值是引用，需要复制时用 copy()
