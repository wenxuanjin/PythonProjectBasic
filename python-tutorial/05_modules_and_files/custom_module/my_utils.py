"""
自定义模块示例 - my_utils.py
===========================

本文件学习目标：
1. 学会创建自定义模块
2. 理解模块的组织方式
3. 掌握模块的文档字符串
"""

# ============================================================
# 模块文档字符串
# ============================================================

"""
这是一个自定义工具模块，包含一些常用的工具函数。

使用方法：
    from custom_module.my_utils import add, multiply
    或
    from custom_module import my_utils
    my_utils.add(1, 2)
"""

# ============================================================
# 模块级变量
# ============================================================

# 模块版本
__version__ = "1.0.0"

# 模块作者
__author__ = "Python 教程"

# 常量
PI = 3.14159
E = 2.71828


# ============================================================
# 数学工具函数
# ============================================================

def add(a, b):
    """
    计算两个数的和

    参数:
        a: 第一个数
        b: 第二个数

    返回:
        两数之和

    示例:
        >>> add(1, 2)
        3
    """
    return a + b


def subtract(a, b):
    """
    计算两个数的差

    参数:
        a: 被减数
        b: 减数

    返回:
        两数之差
    """
    return a - b


def multiply(a, b):
    """
    计算两个数的积

    参数:
        a: 第一个数
        b: 第二个数

    返回:
        两数之积
    """
    return a * b


def divide(a, b):
    """
    计算两个数的商

    参数:
        a: 被除数
        b: 除数

    返回:
        两数之商

    异常:
        ValueError: 当除数为 0 时
    """
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b


def factorial(n):
    """
    计算阶乘

    参数:
        n: 非负整数

    返回:
        n 的阶乘

    异常:
        ValueError: 当 n 为负数时
    """
    if n < 0:
        raise ValueError("n 必须是非负整数")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


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


# ============================================================
# 字符串工具函数
# ============================================================

def reverse_string(s):
    """
    反转字符串

    参数:
        s: 要反转的字符串

    返回:
        反转后的字符串
    """
    return s[::-1]


def is_palindrome(s):
    """
    判断是否为回文

    参数:
        s: 要判断的字符串

    返回:
        True 如果是回文，否则 False
    """
    # 去除空格并转为小写
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def count_words(text):
    """
    统计单词数量

    参数:
        text: 文本字符串

    返回:
        单词数量
    """
    words = text.split()
    return len(words)


def truncate(text, max_length, suffix="..."):
    """
    截断字符串

    参数:
        text: 要截断的字符串
        max_length: 最大长度
        suffix: 截断后的后缀

    返回:
        截断后的字符串
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


# ============================================================
# 列表工具函数
# ============================================================

def flatten(nested_list):
    """
    扁平化嵌套列表

    参数:
        nested_list: 嵌套列表

    返回:
        扁平化后的列表
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def unique(lst):
    """
    去除列表中的重复元素（保持顺序）

    参数:
        lst: 列表

    返回:
        去重后的列表
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def chunk(lst, size):
    """
    将列表分割成指定大小的块

    参数:
        lst: 列表
        size: 每块的大小

    返回:
        分割后的列表
    """
    return [lst[i:i + size] for i in range(0, len(lst), size)]


# ============================================================
# 私有函数（以下划线开头）
# ============================================================

def _helper_function():
    """
    这是一个私有函数，不应该被外部直接调用。
    以单下划线开头的函数表示"内部使用"。
    """
    pass


# ============================================================
# 模块测试代码
# ============================================================

if __name__ == "__main__":
    # 当直接运行此文件时，执行测试代码
    print("=" * 50)
    print("my_utils 模块测试")
    print("=" * 50)

    print(f"\n模块版本: {__version__}")
    print(f"模块作者: {__author__}")

    # 测试数学函数
    print("\n数学函数测试:")
    print(f"add(3, 5) = {add(3, 5)}")
    print(f"subtract(10, 4) = {subtract(10, 4)}")
    print(f"multiply(6, 7) = {multiply(6, 7)}")
    print(f"divide(20, 4) = {divide(20, 4)}")
    print(f"factorial(5) = {factorial(5)}")
    print(f"is_prime(17) = {is_prime(17)}")

    # 测试字符串函数
    print("\n字符串函数测试:")
    print(f"reverse_string('hello') = '{reverse_string('hello')}'")
    print(f"is_palindrome('level') = {is_palindrome('level')}")
    print(f"count_words('hello world python') = {count_words('hello world python')}")
    print(f"truncate('hello world', 8) = '{truncate('hello world', 8)}'")

    # 测试列表函数
    print("\n列表函数测试:")
    print(f"flatten([[1, 2], [3, [4, 5]]]) = {flatten([[1, 2], [3, [4, 5]]])}")
    print(f"unique([1, 2, 2, 3, 3, 3]) = {unique([1, 2, 2, 3, 3, 3])}")
    print(f"chunk([1, 2, 3, 4, 5], 2) = {chunk([1, 2, 3, 4, 5], 2)}")

    print("\n" + "=" * 50)
    print("测试完成！")
    print("=" * 50)
