"""
第4章：函数 - lambda 表达式
=========================

本文件学习目标：
1. 理解 lambda 表达式的概念
2. 掌握 lambda 的语法
3. 学会 lambda 的合理使用场景
4. 理解 lambda 与普通函数的区别
"""

# ============================================================
# 一、什么是 lambda 表达式？
# ============================================================
#
# lambda 表达式是一种创建匿名函数的简洁方式。
# 匿名函数：没有名字的函数。
#
# lambda 的特点：
# 1. 只能包含一个表达式
# 2. 自动返回表达式的结果
# 3. 适合简单的、一次性使用的函数


# ============================================================
# 二、lambda 的语法
# ============================================================

# 语法：lambda 参数: 表达式

# 普通函数
def add_normal(a, b):
    return a + b


# 等价的 lambda 表达式
add_lambda = lambda a, b: a + b

print("lambda 基本语法:")
print(f"普通函数: add_normal(3, 5) = {add_normal(3, 5)}")
print(f"lambda: add_lambda(3, 5) = {add_lambda(3, 5)}")


# 更多示例
square = lambda x: x ** 2
print(f"\n平方: square(4) = {square(4)}")

is_even = lambda x: x % 2 == 0
print(f"是否偶数: is_even(4) = {is_even(4)}")

greet = lambda name: f"你好，{name}！"
print(f"问候: greet('张三') = {greet('张三')}")


# ============================================================
# 三、lambda 的参数
# ============================================================

print("\nlambda 的参数:")

# 无参数
say_hello = lambda: "Hello!"
print(f"无参数: {say_hello()}")

# 单个参数
double = lambda x: x * 2
print(f"单个参数: double(5) = {double(5)}")

# 多个参数
multiply = lambda x, y: x * y
print(f"多个参数: multiply(3, 4) = {multiply(3, 4)}")

# 默认参数
power = lambda x, n=2: x ** n
print(f"默认参数: power(3) = {power(3)}")
print(f"默认参数: power(3, 3) = {power(3, 3)}")

# *args
sum_all = lambda *args: sum(args)
print(f"*args: sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")


# ============================================================
# 四、lambda 的常见使用场景
# ============================================================

print("\nlambda 的常见使用场景:")

# 1. 作为 sorted() 的 key 参数
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78},
]

print("\n1. 排序:")
print(f"原列表: {students}")

# 按分数排序
sorted_by_score = sorted(students, key=lambda x: x["score"])
print(f"按分数升序: {sorted_by_score}")

sorted_by_score_desc = sorted(students, key=lambda x: x["score"], reverse=True)
print(f"按分数降序: {sorted_by_score_desc}")

# 按名字长度排序
words = ["apple", "pie", "banana", "cat"]
sorted_by_length = sorted(words, key=lambda x: len(x))
print(f"\n按长度排序: {sorted_by_length}")


# 2. 作为 map() 的参数
print("\n2. map():")
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(f"原列表: {numbers}")
print(f"平方: {squares}")


# 3. 作为 filter() 的参数
print("\n3. filter():")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"原列表: {numbers}")
print(f"偶数: {evens}")


# 4. 作为 max()/min() 的 key 参数
print("\n4. max()/min():")
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78},
]
top_student = max(students, key=lambda x: x["score"])
print(f"最高分学生: {top_student}")


# 5. 在字典中存储简单函数
print("\n5. 字典中的函数:")
operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y if y != 0 else "除数不能为0",
}

print(f"add(10, 5) = {operations['add'](10, 5)}")
print(f"subtract(10, 5) = {operations['subtract'](10, 5)}")
print(f"multiply(10, 5) = {operations['multiply'](10, 5)}")
print(f"divide(10, 5) = {operations['divide'](10, 5)}")


# ============================================================
# 五、lambda vs 普通函数
# ============================================================

print("\nlambda vs 普通函数:")

# lambda 的限制：
# 1. 只能有一个表达式
# 2. 不能包含语句（如 if 语句、循环等）
# 3. 没有函数名，调试困难
# 4. 没有文档字符串

# 普通函数更适合：
# 1. 复杂的逻辑
# 2. 需要多行代码
# 3. 需要文档字符串
# 4. 需要重复使用

# 示例：判断成绩等级

# 使用 lambda（不推荐，太复杂）
# get_grade = lambda score: "A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else ("D" if score >= 60 else "F")))


# 使用普通函数（推荐）
def get_grade(score):
    """
    根据分数返回等级

    参数:
        score: 分数

    返回:
        等级（A/B/C/D/F）
    """
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


print(f"85 分的等级: {get_grade(85)}")


# ============================================================
# 六、lambda 中的条件表达式
# ============================================================

print("\nlambda 中的条件表达式:")

# lambda 可以使用条件表达式（三元运算符）
# 语法：lambda 参数: 值1 if 条件 else 值2

# 判断正负
sign = lambda x: "正数" if x > 0 else ("负数" if x < 0 else "零")
print(f"sign(5) = {sign(5)}")
print(f"sign(-3) = {sign(-3)}")
print(f"sign(0) = {sign(0)}")

# 取绝对值
abs_value = lambda x: x if x >= 0 else -x
print(f"abs_value(-5) = {abs_value(-5)}")

# 取较大值
max_of_two = lambda a, b: a if a > b else b
print(f"max_of_two(3, 7) = {max_of_two(3, 7)}")


# ============================================================
# 七、lambda 的注意事项
# ============================================================

print("\nlambda 的注意事项:")

# 1. 不要过度使用 lambda
# 如果 lambda 变得复杂，应该使用普通函数

# 2. lambda 在循环中的陷阱
print("\n循环中的陷阱:")

# 错误示例
functions_wrong = []
for i in range(3):
    functions_wrong.append(lambda: i)  # 所有 lambda 都引用同一个 i

print("错误结果:")
for f in functions_wrong:
    print(f"  {f()}")  # 都是 2

# 正确示例
functions_correct = []
for i in range(3):
    functions_correct.append(lambda x=i: x)  # 使用默认参数捕获当前值

print("正确结果:")
for f in functions_correct:
    print(f"  {f()}")  # 0, 1, 2


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("lambda 综合练习")
    print("=" * 50)

    # 练习1：使用 lambda 对列表进行多条件排序
    print("\n多条件排序:")
    students = [
        {"name": "张三", "age": 20, "score": 85},
        {"name": "李四", "age": 19, "score": 85},
        {"name": "王五", "age": 20, "score": 90},
        {"name": "赵六", "age": 19, "score": 90},
    ]

    # 先按分数降序，再按年龄升序
    sorted_students = sorted(students, key=lambda x: (-x["score"], x["age"]))
    print("按分数降序、年龄升序排序:")
    for s in sorted_students:
        print(f"  {s['name']}: 分数={s['score']}, 年龄={s['age']}")

    # 练习2：使用 map 和 lambda 处理数据
    print("\n数据处理:")
    prices = [100, 200, 300, 400, 500]
    # 打 8 折
    discounted = list(map(lambda x: x * 0.8, prices))
    print(f"原价: {prices}")
    print(f"8折后: {discounted}")

    # 练习3：使用 filter 和 lambda 筛选数据
    print("\n数据筛选:")
    products = [
        {"name": "苹果", "price": 5, "stock": 100},
        {"name": "香蕉", "price": 3, "stock": 0},
        {"name": "橙子", "price": 4, "stock": 50},
        {"name": "葡萄", "price": 8, "stock": 0},
    ]

    # 筛选有库存的商品
    in_stock = list(filter(lambda x: x["stock"] > 0, products))
    print("有库存的商品:")
    for p in in_stock:
        print(f"  {p['name']}: 库存={p['stock']}")

    # 练习4：使用 reduce 和 lambda
    from functools import reduce

    print("\n使用 reduce:")
    numbers = [1, 2, 3, 4, 5]
    # 计算阶乘
    factorial = reduce(lambda x, y: x * y, numbers)
    print(f"1*2*3*4*5 = {factorial}")

    # 找出最大值
    max_value = reduce(lambda x, y: x if x > y else y, numbers)
    print(f"最大值: {max_value}")

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. lambda 语法：lambda 参数: 表达式
#
# 2. lambda 特点：
#    - 匿名函数
#    - 只能有一个表达式
#    - 自动返回结果
#
# 3. 常见使用场景：
#    - sorted() 的 key 参数
#    - map() 的函数参数
#    - filter() 的函数参数
#    - max()/min() 的 key 参数
#
# 4. lambda vs 普通函数：
#    - lambda 适合简单的一次性函数
#    - 复杂逻辑应使用普通函数
#
# 5. 注意事项：
#    - 不要过度使用
#    - 注意循环中的陷阱
#    - 保持简洁
