"""
第3章：数据结构 - 集合（Set）
============================

本文件学习目标：
1. 理解集合的概念和特点
2. 掌握集合的创建方式
3. 掌握集合的基本操作
4. 学会集合的数学运算
5. 理解集合的去重特性
"""

# ============================================================
# 一、什么是集合？
# ============================================================
#
# 集合（Set）是 Python 中的无序不重复元素集。
#
# 集合的特点：
# 1. 无序：元素没有固定顺序
# 2. 不重复：自动去除重复元素
# 3. 元素必须是不可变类型
# 4. 可变：可以添加、删除元素
#
# 集合用花括号 {} 表示，但空集合必须用 set() 创建。


# ============================================================
# 二、创建集合
# ============================================================

# 方式1：使用花括号
fruits = {"苹果", "香蕉", "橙子"}
print("水果集合:", fruits)

# 方式2：使用 set() 函数
numbers = set([1, 2, 3, 4, 5])
print("数字集合:", numbers)

# 方式3：创建空集合（必须用 set()）
empty_set = set()
print("空集合:", empty_set)
print("类型:", type(empty_set))

# 注意：{} 创建的是空字典，不是空集合
empty_dict = {}
print("空字典:", empty_dict)
print("类型:", type(empty_dict))

# 方式4：从字符串创建
char_set = set("hello")
print("字符集合:", char_set)  # 自动去重

# 方式5：集合推导式
squares = {x ** 2 for x in range(1, 6)}
print("平方集合:", squares)


# ============================================================
# 三、集合的去重特性
# ============================================================

print("\n集合的去重特性:")

# 创建时自动去重
numbers = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
print(f"去重后: {numbers}")

# 列表去重
list_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_list = list(set(list_with_duplicates))
print(f"原列表: {list_with_duplicates}")
print(f"去重后: {unique_list}")

# 字符串去重
text = "aabbccdd"
unique_chars = set(text)
print(f"原字符串: {text}")
print(f"去重后: {unique_chars}")


# ============================================================
# 四、集合的基本操作
# ============================================================

fruits = {"苹果", "香蕉", "橙子"}
print("\n集合的基本操作:")
print(f"原集合: {fruits}")

# 添加元素：add()
fruits.add("葡萄")
print(f"add 后: {fruits}")

# 添加重复元素不会报错，但也不会添加
fruits.add("苹果")
print(f"添加重复元素后: {fruits}")

# 添加多个元素：update()
fruits.update(["西瓜", "芒果"])
print(f"update 后: {fruits}")

# 删除元素：remove()（元素不存在会报错）
fruits.remove("香蕉")
print(f"remove 后: {fruits}")

# 删除元素：discard()（元素不存在不会报错）
fruits.discard("不存在的水果")
print(f"discard 后: {fruits}")

# 随机删除并返回一个元素：pop()
removed = fruits.pop()
print(f"pop 返回: {removed}, 集合: {fruits}")

# 清空集合：clear()
temp_set = {1, 2, 3}
temp_set.clear()
print(f"clear 后: {temp_set}")


# ============================================================
# 五、集合的数学运算
# ============================================================

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("\n集合的数学运算:")
print(f"集合 A: {set_a}")
print(f"集合 B: {set_b}")

# 并集：所有元素
union = set_a | set_b  # 或 set_a.union(set_b)
print(f"并集 A | B: {union}")

# 交集：共同元素
intersection = set_a & set_b  # 或 set_a.intersection(set_b)
print(f"交集 A & B: {intersection}")

# 差集：在 A 中但不在 B 中
difference = set_a - set_b  # 或 set_a.difference(set_b)
print(f"差集 A - B: {difference}")

difference_ba = set_b - set_a
print(f"差集 B - A: {difference_ba}")

# 对称差集：在 A 或 B 中，但不同时在两者中
symmetric_diff = set_a ^ set_b  # 或 set_a.symmetric_difference(set_b)
print(f"对称差集 A ^ B: {symmetric_diff}")


# ============================================================
# 六、集合的关系判断
# ============================================================

set_a = {1, 2, 3, 4, 5}
set_b = {1, 2, 3}
set_c = {6, 7, 8}

print("\n集合的关系判断:")
print(f"集合 A: {set_a}")
print(f"集合 B: {set_b}")
print(f"集合 C: {set_c}")

# 子集判断
print(f"B 是 A 的子集: {set_b.issubset(set_a)}")  # True
print(f"B <= A: {set_b <= set_a}")  # True

# 超集判断
print(f"A 是 B 的超集: {set_a.issuperset(set_b)}")  # True
print(f"A >= B: {set_a >= set_b}")  # True

# 不相交判断
print(f"A 和 C 不相交: {set_a.isdisjoint(set_c)}")  # True

# 相等判断
set_d = {3, 2, 1}
print(f"\n集合 B: {set_b}")
print(f"集合 D: {set_d}")
print(f"B == D: {set_b == set_d}")  # True（集合无序）


# ============================================================
# 七、集合的遍历
# ============================================================

fruits = {"苹果", "香蕉", "橙子", "葡萄"}

print("\n集合的遍历:")
for fruit in fruits:
    print(f"  {fruit}")

# 注意：集合是无序的，每次遍历顺序可能不同


# ============================================================
# 八、不可变集合（frozenset）
# ============================================================

print("\n不可变集合 frozenset:")

# 创建不可变集合
frozen = frozenset([1, 2, 3, 4, 5])
print(f"frozenset: {frozen}")

# 不可变集合不能添加或删除元素
# frozen.add(6)  # AttributeError

# 不可变集合可以作为字典的键或集合的元素
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(f"集合的集合: {set_of_sets}")

dict_with_frozen_key = {frozenset([1, 2]): "value"}
print(f"frozenset 作为键: {dict_with_frozen_key}")


# ============================================================
# 九、集合的实际应用
# ============================================================

print("\n集合的实际应用:")

# 1. 去重
print("1. 列表去重:")
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(numbers))
print(f"  原列表: {numbers}")
print(f"  去重后: {unique}")

# 2. 成员检测（比列表快）
print("\n2. 成员检测:")
large_set = set(range(10000))
print(f"  9999 in large_set: {9999 in large_set}")

# 3. 找出共同好友
print("\n3. 找出共同好友:")
alice_friends = {"Bob", "Charlie", "David", "Eve"}
bob_friends = {"Alice", "Charlie", "Frank", "Eve"}
common_friends = alice_friends & bob_friends
print(f"  Alice 的好友: {alice_friends}")
print(f"  Bob 的好友: {bob_friends}")
print(f"  共同好友: {common_friends}")

# 4. 找出独有元素
print("\n4. 找出独有元素:")
alice_only = alice_friends - bob_friends
print(f"  只有 Alice 有的好友: {alice_only}")

# 5. 检查是否有重复
print("\n5. 检查是否有重复:")
items = [1, 2, 3, 4, 5]
has_duplicates = len(items) != len(set(items))
print(f"  列表: {items}")
print(f"  有重复: {has_duplicates}")

items_with_dup = [1, 2, 2, 3, 4]
has_duplicates = len(items_with_dup) != len(set(items_with_dup))
print(f"  列表: {items_with_dup}")
print(f"  有重复: {has_duplicates}")


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("集合综合练习")
    print("=" * 50)

    # 练习1：找出两个列表的交集、并集、差集
    print("\n列表运算:")
    list1 = [1, 2, 3, 4, 5, 5, 6]
    list2 = [4, 5, 6, 7, 8, 8, 9]

    set1 = set(list1)
    set2 = set(list2)

    print(f"列表1: {list1}")
    print(f"列表2: {list2}")
    print(f"交集: {list(set1 & set2)}")
    print(f"并集: {list(set1 | set2)}")
    print(f"差集(1-2): {list(set1 - set2)}")

    # 练习2：统计两个字符串的共同字符
    print("\n共同字符:")
    str1 = "hello"
    str2 = "world"
    common_chars = set(str1) & set(str2)
    print(f"字符串1: '{str1}'")
    print(f"字符串2: '{str2}'")
    print(f"共同字符: {common_chars}")

    # 练习3：找出列表中的重复元素
    print("\n找出重复元素:")
    numbers = [1, 2, 3, 2, 4, 3, 5, 6, 5]
    seen = set()
    duplicates = set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    print(f"列表: {numbers}")
    print(f"重复元素: {duplicates}")

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. 集合特点：无序、不重复、元素不可变
#
# 2. 创建集合：{}、set()、集合推导式
#    - 空集合必须用 set()
#
# 3. 基本操作：
#    - 添加：add()、update()
#    - 删除：remove()、discard()、pop()、clear()
#
# 4. 数学运算：
#    - 并集：| 或 union()
#    - 交集：& 或 intersection()
#    - 差集：- 或 difference()
#    - 对称差集：^ 或 symmetric_difference()
#
# 5. 关系判断：
#    - 子集：issubset() 或 <=
#    - 超集：issuperset() 或 >=
#    - 不相交：isdisjoint()
#
# 6. frozenset：不可变集合，可作为字典键
#
# 7. 应用场景：去重、成员检测、集合运算
