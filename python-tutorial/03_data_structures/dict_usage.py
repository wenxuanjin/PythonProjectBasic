"""
第3章：数据结构 - 字典（Dict）
============================

本文件学习目标：
1. 理解字典的概念和特点
2. 掌握字典的创建方式
3. 掌握字典的增删改查操作
4. 学会字典的常用方法
5. 理解字典的遍历方式
"""

# ============================================================
# 一、什么是字典？
# ============================================================
#
# 字典（Dict）是 Python 中的映射类型，存储键值对。
#
# 字典的特点：
# 1. 键值对：每个元素由键（key）和值（value）组成
# 2. 键唯一：同一个字典中键不能重复
# 3. 键不可变：键必须是不可变类型（字符串、数字、元组）
# 4. 值可以是任意类型
# 5. 无序（Python 3.7+ 保持插入顺序）
#
# 字典用花括号 {} 表示，键值对用冒号分隔。


# ============================================================
# 二、创建字典
# ============================================================

# 方式1：使用花括号
student = {"name": "张三", "age": 20, "grade": "大二"}
print("学生信息:", student)

# 方式2：创建空字典
empty_dict = {}
print("空字典:", empty_dict)

# 方式3：使用 dict() 函数
person = dict(name="李四", age=25, city="北京")
print("人员信息:", person)

# 方式4：从键值对列表创建
items = [("a", 1), ("b", 2), ("c", 3)]
letter_dict = dict(items)
print("字母字典:", letter_dict)

# 方式5：使用 fromkeys() 创建
keys = ["name", "age", "city"]
default_dict = dict.fromkeys(keys, "未知")
print("默认字典:", default_dict)

# 方式6：字典推导式
squares = {x: x ** 2 for x in range(1, 6)}
print("平方字典:", squares)


# ============================================================
# 三、访问字典元素
# ============================================================

student = {"name": "张三", "age": 20, "grade": "大二", "scores": [85, 90, 78]}

print("\n访问字典元素:")

# 通过键访问
print(f"姓名: {student['name']}")
print(f"年龄: {student['age']}")

# 访问不存在的键会报错
# print(student["address"])  # KeyError: 'address'

# 使用 get() 方法（推荐）
print(f"城市: {student.get('city')}")  # 返回 None
print(f"城市: {student.get('city', '未知')}")  # 返回默认值

# 检查键是否存在
print(f"'name' 在字典中: {'name' in student}")
print(f"'city' 在字典中: {'city' in student}")

# 获取字典长度
print(f"字典长度: {len(student)}")


# ============================================================
# 四、修改字典
# ============================================================

student = {"name": "张三", "age": 20}
print("\n修改字典:")
print(f"原字典: {student}")

# 修改已有的键
student["age"] = 21
print(f"修改年龄后: {student}")

# 添加新的键值对
student["city"] = "北京"
print(f"添加城市后: {student}")

# 使用 update() 批量更新
student.update({"grade": "大三", "age": 22})
print(f"批量更新后: {student}")

# update() 也可以用关键字参数
student.update(major="计算机", gpa=3.5)
print(f"再次更新后: {student}")


# ============================================================
# 五、删除字典元素
# ============================================================

student = {"name": "张三", "age": 20, "city": "北京", "grade": "大二"}
print("\n删除字典元素:")
print(f"原字典: {student}")

# pop()：删除指定键并返回值
age = student.pop("age")
print(f"pop('age') 返回: {age}, 字典: {student}")

# pop() 可以指定默认值，避免 KeyError
address = student.pop("address", "不存在")
print(f"pop('address') 返回: {address}")

# popitem()：删除并返回最后一个键值对
item = student.popitem()
print(f"popitem() 返回: {item}, 字典: {student}")

# del：删除指定键
student = {"name": "张三", "age": 20, "city": "北京"}
del student["city"]
print(f"del 后: {student}")

# clear()：清空字典
student.clear()
print(f"clear() 后: {student}")


# ============================================================
# 六、字典的遍历
# ============================================================

student = {"name": "张三", "age": 20, "city": "北京"}

print("\n字典的遍历:")

# 遍历键
print("遍历键:")
for key in student:
    print(f"  {key}")

# 或者使用 keys()
print("使用 keys():")
for key in student.keys():
    print(f"  {key}")

# 遍历值
print("遍历值:")
for value in student.values():
    print(f"  {value}")

# 遍历键值对
print("遍历键值对:")
for key, value in student.items():
    print(f"  {key}: {value}")


# ============================================================
# 七、字典常用方法
# ============================================================

print("\n字典常用方法:")

student = {"name": "张三", "age": 20}

# keys()：获取所有键
print(f"所有键: {list(student.keys())}")

# values()：获取所有值
print(f"所有值: {list(student.values())}")

# items()：获取所有键值对
print(f"所有键值对: {list(student.items())}")

# copy()：复制字典
student_copy = student.copy()
print(f"复制字典: {student_copy}")

# setdefault()：获取键的值，如果不存在则设置默认值
student = {"name": "张三"}
age = student.setdefault("age", 18)
print(f"\nsetdefault 后: {student}")
print(f"返回值: {age}")

# 如果键已存在，不会修改
name = student.setdefault("name", "李四")
print(f"键已存在时: {student}")
print(f"返回值: {name}")


# ============================================================
# 八、字典推导式
# ============================================================

print("\n字典推导式:")

# 基本形式
squares = {x: x ** 2 for x in range(1, 6)}
print(f"平方字典: {squares}")

# 带条件
even_squares = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
print(f"偶数平方: {even_squares}")

# 交换键值
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(f"原字典: {original}")
print(f"交换后: {swapped}")

# 从两个列表创建字典
keys = ["name", "age", "city"]
values = ["张三", 20, "北京"]
combined = {k: v for k, v in zip(keys, values)}
print(f"合并字典: {combined}")


# ============================================================
# 九、嵌套字典
# ============================================================

print("\n嵌套字典:")

# 字典可以嵌套
students = {
    "001": {
        "name": "张三",
        "age": 20,
        "scores": {"math": 85, "english": 90}
    },
    "002": {
        "name": "李四",
        "age": 21,
        "scores": {"math": 78, "english": 85}
    }
}

print("学生信息:")
for student_id, info in students.items():
    print(f"  学号: {student_id}")
    print(f"    姓名: {info['name']}")
    print(f"    数学成绩: {info['scores']['math']}")


# ============================================================
# 十、字典的注意事项
# ============================================================

print("\n字典的注意事项:")

# 1. 键必须是不可变类型
valid_dict = {
    "string_key": 1,      # 字符串键
    123: 2,               # 数字键
    (1, 2): 3,            # 元组键
}
print(f"有效的键类型: {valid_dict}")

# 列表不能作为键
# invalid_dict = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'

# 2. 键是唯一的，重复的键会被覆盖
duplicate = {"a": 1, "b": 2, "a": 3}
print(f"重复键: {duplicate}")  # {'a': 3, 'b': 2}

# 3. 字典是可变对象，赋值是引用
dict1 = {"a": 1, "b": 2}
dict2 = dict1
dict2["c"] = 3
print(f"\ndict1: {dict1}")  # 也被修改了
print(f"dict2: {dict2}")

# 复制字典
dict1 = {"a": 1, "b": 2}
dict2 = dict1.copy()
dict2["c"] = 3
print(f"\n复制后 dict1: {dict1}")  # 没有被修改
print(f"复制后 dict2: {dict2}")


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("字典综合练习")
    print("=" * 50)

    # 练习1：统计字符出现次数
    print("\n统计字符出现次数:")
    text = "hello world"
    char_count = {}
    for char in text:
        if char != " ":
            char_count[char] = char_count.get(char, 0) + 1
    print(f"文本: '{text}'")
    print(f"字符统计: {char_count}")

    # 练习2：合并两个字典
    print("\n合并两个字典:")
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    merged = {**dict1, **dict2}  # Python 3.5+
    print(f"dict1: {dict1}")
    print(f"dict2: {dict2}")
    print(f"合并后: {merged}")

    # 练习3：按值排序字典
    print("\n按值排序字典:")
    scores = {"张三": 85, "李四": 92, "王五": 78, "赵六": 90}
    sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
    print(f"原字典: {scores}")
    print(f"按分数排序: {sorted_scores}")

    # 练习4：找出字典中的最大值
    print("\n找出最大值:")
    max_name = max(scores, key=scores.get)
    print(f"最高分: {max_name} - {scores[max_name]}分")

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. 字典特点：键值对、键唯一、键不可变
#
# 2. 创建字典：{}、dict()、fromkeys()、字典推导式
#
# 3. 访问元素：
#    - dict[key]：可能报 KeyError
#    - dict.get(key, default)：推荐使用
#
# 4. 修改字典：
#    - dict[key] = value
#    - dict.update()
#
# 5. 删除元素：pop()、popitem()、del、clear()
#
# 6. 遍历字典：
#    - keys()：遍历键
#    - values()：遍历值
#    - items()：遍历键值对
#
# 7. 常用方法：
#    - keys()、values()、items()
#    - get()、setdefault()
#    - copy()、update()
#
# 8. 字典推导式：{key: value for item in iterable}
#
# 9. 注意：键必须是不可变类型，字典赋值是引用
