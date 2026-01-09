"""
第4章：函数 - 函数定义
====================

本文件学习目标：
1. 理解函数的概念和作用
2. 掌握函数的定义语法
3. 学会调用函数
4. 理解函数的文档字符串
"""

# ============================================================
# 一、什么是函数？
# ============================================================
#
# 函数是一段可重复使用的代码块，用于完成特定的任务。
#
# 函数的作用：
# 1. 代码复用：避免重复编写相同的代码
# 2. 模块化：将复杂问题分解为小问题
# 3. 可维护性：修改一处，处处生效
# 4. 可读性：给代码块起一个有意义的名字
#
# 生活中的例子：
# - 微波炉的"加热"按钮就是一个函数
# - 你按下按钮（调用函数），微波炉执行加热（函数体）


# ============================================================
# 二、函数的定义
# ============================================================

# 函数定义的语法：
# def 函数名(参数列表):
#     """文档字符串（可选）"""
#     函数体
#     return 返回值（可选）

# 最简单的函数：无参数，无返回值
def say_hello():
    """打印问候语"""
    print("Hello, World!")


# 调用函数
print("调用 say_hello():")
say_hello()


# 带参数的函数
def greet(name):
    """
    向指定的人打招呼

    参数:
        name: 要问候的人的名字
    """
    print(f"你好，{name}！")


print("\n调用 greet():")
greet("张三")
greet("李四")


# 带返回值的函数
def add(a, b):
    """
    计算两个数的和

    参数:
        a: 第一个数
        b: 第二个数

    返回:
        两数之和
    """
    return a + b


print("\n调用 add():")
result = add(3, 5)
print(f"3 + 5 = {result}")


# ============================================================
# 三、函数命名规范
# ============================================================
#
# 1. 使用小写字母和下划线（snake_case）
# 2. 名字应该描述函数的功能
# 3. 动词开头（如 get_、set_、calculate_、is_、has_）
# 4. 避免使用 Python 内置函数名

# 好的函数名示例
def calculate_area(length, width):
    """计算矩形面积"""
    return length * width


def is_even(number):
    """判断是否为偶数"""
    return number % 2 == 0


def get_max_value(numbers):
    """获取列表中的最大值"""
    return max(numbers)


# 不好的函数名示例（不要这样命名）
# def f(x):  # 名字没有意义
# def calculate():  # 计算什么？
# def list():  # 覆盖了内置函数


# ============================================================
# 四、函数的调用
# ============================================================

print("\n函数的调用:")

# 定义函数
def multiply(a, b):
    """计算两数的乘积"""
    return a * b


# 调用函数并使用返回值
result = multiply(4, 5)
print(f"4 * 5 = {result}")

# 直接在表达式中使用
print(f"3 * 7 = {multiply(3, 7)}")

# 函数的返回值可以作为另一个函数的参数
print(f"(2 * 3) * (4 * 5) = {multiply(multiply(2, 3), multiply(4, 5))}")


# ============================================================
# 五、文档字符串（Docstring）
# ============================================================

print("\n文档字符串:")


def calculate_bmi(weight, height):
    """
    计算身体质量指数（BMI）

    BMI = 体重(kg) / 身高(m)^2

    参数:
        weight (float): 体重，单位：千克
        height (float): 身高，单位：米

    返回:
        float: BMI 值

    示例:
        >>> calculate_bmi(70, 1.75)
        22.857142857142858
    """
    return weight / (height ** 2)


# 查看文档字符串
print("函数文档:")
print(calculate_bmi.__doc__)

# 使用 help() 查看
# help(calculate_bmi)

# 调用函数
bmi = calculate_bmi(70, 1.75)
print(f"\nBMI = {bmi:.2f}")


# ============================================================
# 六、函数的返回值
# ============================================================

print("\n函数的返回值:")


# 没有 return 语句，返回 None
def no_return():
    """没有返回值的函数"""
    print("这个函数没有 return")


result = no_return()
print(f"返回值: {result}")  # None


# return 不带值，也返回 None
def return_nothing():
    """return 不带值"""
    return


result = return_nothing()
print(f"返回值: {result}")  # None


# 返回单个值
def get_square(n):
    """返回平方"""
    return n ** 2


print(f"5 的平方: {get_square(5)}")


# 返回多个值（实际上是返回元组）
def get_min_max(numbers):
    """返回最小值和最大值"""
    return min(numbers), max(numbers)


min_val, max_val = get_min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"最小值: {min_val}, 最大值: {max_val}")


# return 会立即结束函数
def check_positive(n):
    """检查是否为正数"""
    if n <= 0:
        return False
    # 如果 n <= 0，下面的代码不会执行
    print("这是正数")
    return True


print(f"\ncheck_positive(-5): {check_positive(-5)}")
print(f"check_positive(5): {check_positive(5)}")


# ============================================================
# 七、函数是对象
# ============================================================

print("\n函数是对象:")


def say_hi():
    """打印 Hi"""
    print("Hi!")


# 函数可以赋值给变量
greeting = say_hi
greeting()  # 调用

# 函数可以作为参数传递
def execute_twice(func):
    """执行函数两次"""
    func()
    func()


print("\n执行两次:")
execute_twice(say_hi)

# 函数可以存储在数据结构中
operations = {
    "add": add,
    "multiply": multiply,
}

print(f"\n使用字典存储函数:")
print(f"add(2, 3) = {operations['add'](2, 3)}")
print(f"multiply(2, 3) = {operations['multiply'](2, 3)}")


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("函数定义综合练习")
    print("=" * 50)

    # 练习1：定义一个计算圆面积的函数
    def calculate_circle_area(radius):
        """
        计算圆的面积

        参数:
            radius: 圆的半径

        返回:
            圆的面积
        """
        import math
        return math.pi * radius ** 2

    print("\n计算圆面积:")
    for r in [1, 2, 3, 5]:
        area = calculate_circle_area(r)
        print(f"  半径 {r} 的圆面积: {area:.2f}")

    # 练习2：定义一个判断质数的函数
    def is_prime(n):
        """
        判断是否为质数

        参数:
            n: 要判断的数

        返回:
            True 如果是质数，否则 False
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    print("\n判断质数:")
    for num in [1, 2, 3, 4, 5, 17, 20, 23]:
        result = "是" if is_prime(num) else "不是"
        print(f"  {num} {result}质数")

    # 练习3：定义一个反转字符串的函数
    def reverse_string(s):
        """
        反转字符串

        参数:
            s: 要反转的字符串

        返回:
            反转后的字符串
        """
        return s[::-1]

    print("\n反转字符串:")
    test_strings = ["hello", "Python", "12345"]
    for s in test_strings:
        print(f"  '{s}' -> '{reverse_string(s)}'")

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. 函数定义语法：
#    def 函数名(参数):
#        """文档字符串"""
#        函数体
#        return 返回值
#
# 2. 函数命名规范：
#    - 使用 snake_case
#    - 动词开头
#    - 描述功能
#
# 3. 函数调用：函数名(参数)
#
# 4. 文档字符串：
#    - 描述函数功能
#    - 说明参数和返回值
#    - 可以用 __doc__ 或 help() 查看
#
# 5. 返回值：
#    - 没有 return 返回 None
#    - 可以返回多个值（元组）
#    - return 立即结束函数
#
# 6. 函数是对象：
#    - 可以赋值给变量
#    - 可以作为参数传递
#    - 可以存储在数据结构中
