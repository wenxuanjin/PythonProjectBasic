"""
第3章：数据结构 - 元组（Tuple）
============================

本文件学习目标：
1. 理解元组的概念和特点
2. 掌握元组的创建方式
3. 理解元组的不可变性
4. 学会元组的常用操作
5. 理解元组与列表的区别
"""

# ============================================================
# 一、什么是元组？
# ============================================================
#
# 元组（Tuple）是 Python 中的另一种序列类型。
#
# 元组的特点：
# 1. 有序：元素按照添加顺序排列
# 2. 不可变：创建后不能修改
# 3. 可重复：可以包含重复的元素
# 4. 可以包含不同类型的元素
#
# 元组用圆括号 () 表示，元素之间用逗号分隔。


# ============================================================
# 二、创建元组
# ============================================================

# 方式1：使用圆括号
fruits = ("苹果", "香蕉", "橙子")
print("水果元组:", fruits)

# 方式2：不使用括号（逗号分隔）
colors = "红", "绿", "蓝"
print("颜色元组:", colors)

# 方式3：创建空元组
empty_tuple = ()
print("空元组:", empty_tuple)

# 方式4：使用 tuple() 函数
numbers = tuple([1, 2, 3, 4, 5])
print("数字元组:", numbers)

# 注意：创建只有一个元素的元组，必须加逗号
single = (1,)  # 这是元组
not_tuple = (1)  # 这是整数，不是元组
print(f"\n单元素元组: {single}, 类型: {type(single)}")
print(f"不是元组: {not_tuple}, 类型: {type(not_tuple)}")

# 元组可以包含不同类型的元素
mixed = (1, "hello", 3.14, True)
print(f"混合元组: {mixed}")

# 元组可以嵌套
nested = ((1, 2), (3, 4), (5, 6))
print(f"嵌套元组: {nested}")


# ============================================================
# 三、访问元组元素
# ============================================================

fruits = ("苹果", "香蕉", "橙子", "葡萄", "西瓜")

print("\n访问元组元素:")

# 通过索引访问（与列表相同）
print(f"第一个元素: {fruits[0]}")
print(f"最后一个元素: {fruits[-1]}")

# 获取元组长度
print(f"元组长度: {len(fruits)}")

# 检查元素是否存在
print(f"'苹果' 在元组中: {'苹果' in fruits}")

# 元组切片
print(f"切片 [1:4]: {fruits[1:4]}")
print(f"反转: {fruits[::-1]}")


# ============================================================
# 四、元组的不可变性
# ============================================================

print("\n元组的不可变性:")

fruits = ("苹果", "香蕉", "橙子")
print(f"原元组: {fruits}")

# 尝试修改元组会报错
# fruits[0] = "草莓"  # TypeError: 'tuple' object does not support item assignment

# 尝试添加元素会报错
# fruits.append("葡萄")  # AttributeError: 'tuple' object has no attribute 'append'

# 尝试删除元素会报错
# del fruits[0]  # TypeError: 'tuple' object doesn't support item deletion

# 但是，如果元组包含可变对象，可变对象的内容可以修改
mixed = ([1, 2, 3], "hello")
print(f"\n包含列表的元组: {mixed}")
mixed[0].append(4)  # 修改元组中的列表
print(f"修改列表后: {mixed}")
# 注意：元组本身没变（还是同一个列表对象），只是列表的内容变了


# ============================================================
# 五、元组的操作
# ============================================================

print("\n元组的操作:")

# 元组连接
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"连接: {tuple1} + {tuple2} = {combined}")

# 元组重复
repeated = (1, 2) * 3
print(f"重复: (1, 2) * 3 = {repeated}")

# 元组解包
point = (10, 20)
x, y = point
print(f"\n元组解包: point = {point}")
print(f"x = {x}, y = {y}")

# 交换变量（利用元组解包）
a, b = 1, 2
print(f"\n交换前: a = {a}, b = {b}")
a, b = b, a
print(f"交换后: a = {a}, b = {b}")

# 使用 * 收集多余的值
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"\n元组: {numbers}")
print(f"first = {first}, middle = {middle}, last = {last}")


# ============================================================
# 六、元组的方法
# ============================================================

print("\n元组的方法:")

# 元组只有两个方法：count() 和 index()

numbers = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)

# count()：统计元素出现次数
print(f"元组: {numbers}")
print(f"3 出现的次数: {numbers.count(3)}")

# index()：查找元素的索引
print(f"3 第一次出现的索引: {numbers.index(3)}")


# ============================================================
# 七、元组 vs 列表
# ============================================================

print("\n元组 vs 列表:")

# 1. 可变性
# 列表可变，元组不可变
list_example = [1, 2, 3]
tuple_example = (1, 2, 3)
list_example[0] = 100  # 可以
# tuple_example[0] = 100  # 不可以

# 2. 性能
# 元组比列表更快，占用内存更少
import sys
list_size = sys.getsizeof([1, 2, 3, 4, 5])
tuple_size = sys.getsizeof((1, 2, 3, 4, 5))
print(f"列表大小: {list_size} 字节")
print(f"元组大小: {tuple_size} 字节")

# 3. 用途
# 列表：存储同类型的多个元素，需要修改
# 元组：存储不同类型的相关数据，不需要修改

# 4. 作为字典的键
# 元组可以作为字典的键，列表不可以
location = {(0, 0): "原点", (1, 0): "右边"}
print(f"\n元组作为字典键: {location}")
# {[0, 0]: "原点"}  # TypeError: unhashable type: 'list'


# ============================================================
# 八、元组的使用场景
# ============================================================

print("\n元组的使用场景:")

# 1. 函数返回多个值
def get_min_max(numbers):
    """返回列表的最小值和最大值"""
    return min(numbers), max(numbers)

result = get_min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"返回元组: {result}")
min_val, max_val = get_min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"解包: min = {min_val}, max = {max_val}")

# 2. 存储坐标点
point = (10, 20)
print(f"\n坐标点: {point}")

# 3. 存储 RGB 颜色
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
print(f"红色 RGB: {red}")

# 4. 存储数据库记录
student = ("张三", 20, "计算机科学")
name, age, major = student
print(f"\n学生信息: 姓名={name}, 年龄={age}, 专业={major}")

# 5. 作为字典的键
# 存储棋盘位置
chess_board = {
    (0, 0): "车",
    (0, 1): "马",
    (0, 2): "象",
}
print(f"\n棋盘: {chess_board}")


# ============================================================
# 九、命名元组（namedtuple）
# ============================================================

from collections import namedtuple

print("\n命名元组:")

# 创建命名元组类型
Point = namedtuple("Point", ["x", "y"])
Student = namedtuple("Student", ["name", "age", "grade"])

# 创建实例
p = Point(10, 20)
print(f"点: {p}")
print(f"x 坐标: {p.x}")
print(f"y 坐标: {p.y}")

s = Student("张三", 20, "大二")
print(f"\n学生: {s}")
print(f"姓名: {s.name}")
print(f"年龄: {s.age}")
print(f"年级: {s.grade}")

# 命名元组仍然是元组
print(f"\n是否是元组: {isinstance(p, tuple)}")
print(f"可以用索引访问: p[0] = {p[0]}")


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("元组综合练习")
    print("=" * 50)

    # 练习1：使用元组存储学生信息
    print("\n学生信息管理:")
    students = [
        ("张三", 85, "A"),
        ("李四", 72, "B"),
        ("王五", 90, "A"),
        ("赵六", 65, "C"),
    ]

    print("学生成绩表:")
    print(f"{'姓名':<10}{'分数':<10}{'等级':<10}")
    print("-" * 30)
    for name, score, grade in students:
        print(f"{name:<10}{score:<10}{grade:<10}")

    # 练习2：计算多个点之间的距离
    print("\n计算点之间的距离:")
    import math

    points = [(0, 0), (3, 4), (6, 8)]
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print(f"点 {points[i]} 到 {points[i+1]} 的距离: {distance:.2f}")

    # 练习3：元组排序
    print("\n按成绩排序:")
    sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
    for name, score, grade in sorted_students:
        print(f"{name}: {score}分")

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. 元组特点：有序、不可变、可重复
#
# 2. 创建元组：()、tuple()、逗号分隔
#
# 3. 单元素元组：必须加逗号 (1,)
#
# 4. 元组操作：
#    - 索引访问
#    - 切片
#    - 连接 +
#    - 重复 *
#    - 解包
#
# 5. 元组方法：count()、index()
#
# 6. 元组 vs 列表：
#    - 元组不可变，列表可变
#    - 元组更快，占用内存更少
#    - 元组可以作为字典的键
#
# 7. 使用场景：
#    - 函数返回多个值
#    - 存储坐标、颜色等固定数据
#    - 作为字典的键
#
# 8. 命名元组：namedtuple，可以用名字访问元素
