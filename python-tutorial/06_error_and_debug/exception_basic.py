"""
第6章：异常与调试 - 异常基础
==========================

本文件学习目标：
1. 理解什么是异常
2. 认识常见的异常类型
3. 理解异常的产生原因
4. 学会阅读异常信息
"""

# ============================================================
# 一、什么是异常？
# ============================================================
#
# 异常（Exception）是程序运行时发生的错误。
#
# 当 Python 遇到无法处理的情况时，会抛出异常。
# 如果异常没有被处理，程序会终止并显示错误信息。
#
# 异常 vs 语法错误：
# - 语法错误：代码不符合 Python 语法，无法运行
# - 异常：代码语法正确，但运行时出错


# ============================================================
# 二、常见异常类型
# ============================================================

print("常见异常类型演示:")
print("=" * 50)

# 1. ZeroDivisionError：除零错误
print("\n1. ZeroDivisionError（除零错误）:")
print("   原因：除数为零")
print("   示例：10 / 0")
# 10 / 0  # 取消注释会报错

# 2. TypeError：类型错误
print("\n2. TypeError（类型错误）:")
print("   原因：操作或函数应用于不适当类型的对象")
print("   示例：'hello' + 123")
# 'hello' + 123  # 取消注释会报错

# 3. ValueError：值错误
print("\n3. ValueError（值错误）:")
print("   原因：操作或函数接收到类型正确但值不合适的参数")
print("   示例：int('abc')")
# int('abc')  # 取消注释会报错

# 4. IndexError：索引错误
print("\n4. IndexError（索引错误）:")
print("   原因：序列索引超出范围")
print("   示例：[1, 2, 3][10]")
# [1, 2, 3][10]  # 取消注释会报错

# 5. KeyError：键错误
print("\n5. KeyError（键错误）:")
print("   原因：字典中不存在指定的键")
print("   示例：{'a': 1}['b']")
# {'a': 1}['b']  # 取消注释会报错

# 6. NameError：名称错误
print("\n6. NameError（名称错误）:")
print("   原因：使用了未定义的变量")
print("   示例：print(undefined_variable)")
# print(undefined_variable)  # 取消注释会报错

# 7. AttributeError：属性错误
print("\n7. AttributeError（属性错误）:")
print("   原因：对象没有该属性或方法")
print("   示例：'hello'.append('!')")
# 'hello'.append('!')  # 取消注释会报错

# 8. FileNotFoundError：文件未找到错误
print("\n8. FileNotFoundError（文件未找到错误）:")
print("   原因：尝试打开不存在的文件")
print("   示例：open('不存在的文件.txt')")
# open('不存在的文件.txt')  # 取消注释会报错

# 9. ImportError：导入错误
print("\n9. ImportError（导入错误）:")
print("   原因：导入模块失败")
print("   示例：import 不存在的模块")
# import 不存在的模块  # 取消注释会报错

# 10. IndentationError：缩进错误
print("\n10. IndentationError（缩进错误）:")
print("    原因：代码缩进不正确")
print("    这是语法错误，不是运行时异常")


# ============================================================
# 三、异常信息的阅读
# ============================================================

print("\n" + "=" * 50)
print("异常信息的阅读:")

# 异常信息包含：
# 1. Traceback：调用栈，显示错误发生的位置
# 2. 异常类型：如 ZeroDivisionError
# 3. 异常消息：描述错误的具体原因

# 示例异常信息：
"""
Traceback (most recent call last):
  File "example.py", line 10, in <module>
    result = divide(10, 0)
  File "example.py", line 5, in divide
    return a / b
ZeroDivisionError: division by zero

解读：
1. 最后一行是异常类型和消息
2. 从下往上看调用栈
3. 找到自己代码中的错误位置
"""

print("异常信息阅读技巧：")
print("1. 先看最后一行：异常类型和消息")
print("2. 从下往上看 Traceback")
print("3. 找到自己代码中的错误位置")
print("4. 根据异常类型判断问题原因")


# ============================================================
# 四、异常的层次结构
# ============================================================

print("\n" + "=" * 50)
print("异常的层次结构:")

# Python 异常是类，有继承关系
# BaseException
#   +-- SystemExit
#   +-- KeyboardInterrupt
#   +-- Exception
#       +-- ArithmeticError
#       |   +-- ZeroDivisionError
#       +-- LookupError
#       |   +-- IndexError
#       |   +-- KeyError
#       +-- ValueError
#       +-- TypeError
#       +-- ...

print("""
BaseException（所有异常的基类）
  |-- SystemExit（sys.exit() 引发）
  |-- KeyboardInterrupt（Ctrl+C 引发）
  |-- Exception（常规异常的基类）
      |-- ArithmeticError（算术错误）
      |   |-- ZeroDivisionError
      |-- LookupError（查找错误）
      |   |-- IndexError
      |   |-- KeyError
      |-- ValueError
      |-- TypeError
      |-- FileNotFoundError
      |-- ...
""")


# ============================================================
# 五、主动触发异常
# ============================================================

print("=" * 50)
print("主动触发异常:")


def divide(a, b):
    """除法函数，演示主动触发异常"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


def check_age(age):
    """检查年龄，演示主动触发异常"""
    if not isinstance(age, int):
        raise TypeError("年龄必须是整数")
    if age < 0:
        raise ValueError("年龄不能为负数")
    if age > 150:
        raise ValueError("年龄不能超过150")
    return age


print("\n使用 raise 主动触发异常:")
print("raise ValueError('错误消息')")
print("raise TypeError('类型错误')")


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("异常基础综合练习")
    print("=" * 50)

    # 练习1：识别异常类型
    print("\n练习1：识别以下代码会产生什么异常")

    test_cases = [
        ("10 / 0", "ZeroDivisionError"),
        ("int('abc')", "ValueError"),
        ("[1, 2, 3][10]", "IndexError"),
        ("{'a': 1}['b']", "KeyError"),
        ("'hello' + 123", "TypeError"),
    ]

    for code, expected in test_cases:
        print(f"  {code} -> {expected}")

    # 练习2：阅读异常信息
    print("\n练习2：模拟异常信息")

    def func_a():
        return func_b()

    def func_b():
        return func_c()

    def func_c():
        # 这里会产生异常
        return 1 / 0

    print("调用链：func_a -> func_b -> func_c -> 异常")
    print("Traceback 会显示完整的调用栈")

    # 练习3：异常类型判断
    print("\n练习3：判断异常类型")

    def get_exception_type(func):
        """获取函数执行时的异常类型"""
        try:
            func()
        except Exception as e:
            return type(e).__name__
        return "无异常"

    print(f"  lambda: 1/0 -> {get_exception_type(lambda: 1/0)}")
    print(f"  lambda: int('x') -> {get_exception_type(lambda: int('x'))}")
    print(f"  lambda: [][0] -> {get_exception_type(lambda: [][0])}")

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. 异常是程序运行时发生的错误
#
# 2. 常见异常类型：
#    - ZeroDivisionError：除零
#    - TypeError：类型错误
#    - ValueError：值错误
#    - IndexError：索引越界
#    - KeyError：键不存在
#    - NameError：变量未定义
#    - AttributeError：属性不存在
#    - FileNotFoundError：文件不存在
#
# 3. 异常信息阅读：
#    - 先看最后一行（异常类型和消息）
#    - 从下往上看 Traceback
#    - 找到自己代码中的错误位置
#
# 4. 异常有层次结构，都继承自 BaseException
#
# 5. 使用 raise 可以主动触发异常
