"""
第2章：流程控制 - 条件判断
========================

本文件学习目标：
1. 理解条件判断的概念
2. 掌握 if 语句的基本用法
3. 掌握 if-else 语句
4. 掌握 if-elif-else 语句
5. 理解条件表达式（三元运算符）
"""

# ============================================================
# 一、什么是条件判断？
# ============================================================
#
# 条件判断让程序可以根据不同的情况执行不同的代码。
#
# 生活中的例子：
# - 如果下雨，就带伞；否则，不带伞
# - 如果成绩 >= 60，就及格；否则，不及格
#
# 在 Python 中，使用 if 语句来实现条件判断。


# ============================================================
# 二、if 语句
# ============================================================

# if 语句的基本语法：
# if 条件:
#     条件为真时执行的代码

# 示例：判断是否成年
age = 20

if age >= 18:
    print("你已经成年了")
    print("可以独立承担法律责任")

# 注意：
# 1. 条件后面要加冒号 :
# 2. 条件为真时执行的代码要缩进（4个空格）
# 3. 缩进相同的代码属于同一个代码块

# 条件为假时，if 下面的代码不会执行
temperature = 15

if temperature > 30:
    print("天气很热")  # 这行不会执行，因为 15 不大于 30


# ============================================================
# 三、if-else 语句
# ============================================================

# if-else 语句：条件为真执行一段代码，为假执行另一段代码
# if 条件:
#     条件为真时执行
# else:
#     条件为假时执行

# 示例：判断奇偶数
number = 7

if number % 2 == 0:
    print(f"{number} 是偶数")
else:
    print(f"{number} 是奇数")

# 示例：判断成绩是否及格
score = 55

if score >= 60:
    print("恭喜，你及格了！")
else:
    print("很遗憾，你没有及格")


# ============================================================
# 四、if-elif-else 语句
# ============================================================

# 当有多个条件需要判断时，使用 elif（else if 的缩写）
# if 条件1:
#     条件1为真时执行
# elif 条件2:
#     条件2为真时执行
# elif 条件3:
#     条件3为真时执行
# else:
#     以上条件都不满足时执行

# 示例：成绩等级判断
score = 85

print(f"\n成绩: {score}")

if score >= 90:
    grade = "A"
    comment = "优秀"
elif score >= 80:
    grade = "B"
    comment = "良好"
elif score >= 70:
    grade = "C"
    comment = "中等"
elif score >= 60:
    grade = "D"
    comment = "及格"
else:
    grade = "F"
    comment = "不及格"

print(f"等级: {grade}")
print(f"评价: {comment}")

# 示例：根据月份判断季节
month = 8

print(f"\n月份: {month}")

if month in [3, 4, 5]:
    season = "春季"
elif month in [6, 7, 8]:
    season = "夏季"
elif month in [9, 10, 11]:
    season = "秋季"
elif month in [12, 1, 2]:
    season = "冬季"
else:
    season = "无效月份"

print(f"季节: {season}")


# ============================================================
# 五、嵌套的 if 语句
# ============================================================

# if 语句可以嵌套使用
# 但要注意不要嵌套太深，否则代码难以阅读

# 示例：判断是否可以参加活动
age = 25
has_ticket = True

print(f"\n年龄: {age}, 有票: {has_ticket}")

if age >= 18:
    if has_ticket:
        print("欢迎参加活动！")
    else:
        print("请先购票")
else:
    print("未成年人不能参加此活动")

# 更好的写法：使用 and 合并条件
if age >= 18 and has_ticket:
    print("（使用 and）欢迎参加活动！")
elif age < 18:
    print("（使用 and）未成年人不能参加")
else:
    print("（使用 and）请先购票")


# ============================================================
# 六、条件表达式（三元运算符）
# ============================================================

# Python 的条件表达式可以在一行内完成简单的条件判断
# 语法：值1 if 条件 else 值2
# 如果条件为真，返回值1；否则返回值2

age = 20

# 传统写法
if age >= 18:
    status = "成年"
else:
    status = "未成年"

# 条件表达式写法（更简洁）
status = "成年" if age >= 18 else "未成年"
print(f"\n年龄 {age}，状态: {status}")

# 示例：取两个数中的较大值
a = 10
b = 20
max_value = a if a > b else b
print(f"较大值: {max_value}")

# 示例：判断奇偶
number = 7
result = "偶数" if number % 2 == 0 else "奇数"
print(f"{number} 是 {result}")


# ============================================================
# 七、常见的条件表达式
# ============================================================

print("\n常见条件表达式示例:")

# 比较运算符
x = 10
y = 5

print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")   # 等于
print(f"x != y: {x != y}")   # 不等于
print(f"x > y: {x > y}")     # 大于
print(f"x < y: {x < y}")     # 小于
print(f"x >= y: {x >= y}")   # 大于等于
print(f"x <= y: {x <= y}")   # 小于等于

# 逻辑运算符
a = True
b = False

print(f"\na = {a}, b = {b}")
print(f"a and b: {a and b}")  # 与：两个都为 True 才是 True
print(f"a or b: {a or b}")    # 或：有一个为 True 就是 True
print(f"not a: {not a}")      # 非：取反

# 成员运算符
fruits = ["苹果", "香蕉", "橙子"]
print(f"\n水果列表: {fruits}")
print(f"'苹果' in fruits: {'苹果' in fruits}")      # True
print(f"'葡萄' in fruits: {'葡萄' in fruits}")      # False
print(f"'葡萄' not in fruits: {'葡萄' not in fruits}")  # True

# 身份运算符
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"\nlist1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = list1")
print(f"list1 == list2: {list1 == list2}")  # True（值相等）
print(f"list1 is list2: {list1 is list2}")  # False（不是同一个对象）
print(f"list1 is list3: {list1 is list3}")  # True（是同一个对象）


# ============================================================
# 八、常见逻辑错误
# ============================================================

print("\n常见逻辑错误示例:")

# 错误1：使用 = 而不是 ==
x = 10
# if x = 10:  # 错误！= 是赋值，== 才是比较
if x == 10:   # 正确
    print("x 等于 10")

# 错误2：条件顺序不对
score = 95

# 错误的顺序（永远不会输出"优秀"）
# if score >= 60:
#     print("及格")
# elif score >= 90:
#     print("优秀")  # 永远不会执行到这里

# 正确的顺序（从高到低判断）
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")

# 错误3：忘记处理边界情况
age = 18
# 18岁算成年还是未成年？要明确边界
if age >= 18:  # 18岁及以上算成年
    print("成年")

# 错误4：浮点数比较
# 由于浮点数精度问题，直接比较可能出错
a = 0.1 + 0.2
b = 0.3
print(f"\n0.1 + 0.2 == 0.3: {a == b}")  # False！

# 正确做法：使用误差范围比较
epsilon = 0.0001
print(f"使用误差范围比较: {abs(a - b) < epsilon}")  # True


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("条件判断综合练习")
    print("=" * 50)

    # 综合示例：简单的登录验证
    correct_username = "admin"
    correct_password = "123456"

    # 模拟用户输入
    input_username = "admin"
    input_password = "123456"

    print(f"\n输入用户名: {input_username}")
    print(f"输入密码: {'*' * len(input_password)}")

    if input_username == correct_username:
        if input_password == correct_password:
            print("登录成功！欢迎回来！")
        else:
            print("密码错误！")
    else:
        print("用户名不存在！")

    # 使用 and 的简洁写法
    if input_username == correct_username and input_password == correct_password:
        print("（简洁写法）登录成功！")
    else:
        print("（简洁写法）用户名或密码错误！")

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. if 语句：当条件为真时执行代码
#
# 2. if-else 语句：条件为真执行一段，为假执行另一段
#
# 3. if-elif-else 语句：多个条件依次判断
#
# 4. 条件表达式：值1 if 条件 else 值2
#
# 5. 比较运算符：==, !=, >, <, >=, <=
#
# 6. 逻辑运算符：and, or, not
#
# 7. 成员运算符：in, not in
#
# 8. 注意事项：
#    - 条件后要加冒号
#    - 代码块要缩进
#    - 使用 == 比较，不是 =
#    - 多条件判断时注意顺序
