"""
第4章：函数 - 作用域
==================

本文件学习目标：
1. 理解变量作用域的概念
2. 掌握局部变量和全局变量
3. 理解 LEGB 规则
4. 学会使用 global 和 nonlocal 关键字
"""

# ============================================================
# 一、什么是作用域？
# ============================================================
#
# 作用域（Scope）是指变量可以被访问的范围。
#
# Python 中有四种作用域（LEGB）：
# 1. Local（局部）：函数内部
# 2. Enclosing（嵌套）：外层函数
# 3. Global（全局）：模块级别
# 4. Built-in（内置）：Python 内置


# ============================================================
# 二、局部变量
# ============================================================

# 局部变量：在函数内部定义的变量
# 只能在函数内部访问

def my_function():
    """演示局部变量"""
    local_var = "我是局部变量"
    print(f"函数内部: {local_var}")


print("局部变量:")
my_function()

# 在函数外部无法访问局部变量
# print(local_var)  # NameError: name 'local_var' is not defined


# 每次调用函数，局部变量都会重新创建
def counter():
    """每次调用都从 0 开始"""
    count = 0
    count += 1
    print(f"count = {count}")


print("\n每次调用都重新创建:")
counter()  # count = 1
counter()  # count = 1
counter()  # count = 1


# ============================================================
# 三、全局变量
# ============================================================

# 全局变量：在函数外部定义的变量
# 可以在整个模块中访问

global_var = "我是全局变量"


def read_global():
    """读取全局变量"""
    print(f"函数内部读取: {global_var}")


print("\n全局变量:")
print(f"函数外部: {global_var}")
read_global()


# 在函数内部修改全局变量需要使用 global 关键字
counter_value = 0


def increment_wrong():
    """错误的方式：创建了局部变量"""
    counter_value = 1  # 这是局部变量，不是全局变量
    print(f"函数内部: counter_value = {counter_value}")


def increment_correct():
    """正确的方式：使用 global"""
    global counter_value
    counter_value += 1
    print(f"函数内部: counter_value = {counter_value}")


print("\n修改全局变量:")
print(f"初始值: counter_value = {counter_value}")
increment_wrong()
print(f"错误方式后: counter_value = {counter_value}")  # 没有改变
increment_correct()
print(f"正确方式后: counter_value = {counter_value}")  # 改变了


# ============================================================
# 四、LEGB 规则
# ============================================================

# Python 查找变量的顺序：Local -> Enclosing -> Global -> Built-in

# Built-in（内置）
# print, len, sum 等都是内置函数

# Global（全局）
x = "global"


def outer():
    # Enclosing（嵌套）
    x = "enclosing"

    def inner():
        # Local（局部）
        x = "local"
        print(f"inner: x = {x}")

    inner()
    print(f"outer: x = {x}")


print("\nLEGB 规则演示:")
outer()
print(f"global: x = {x}")


# 演示查找顺序
y = "global y"


def outer_func():
    y = "enclosing y"

    def inner_func():
        # 没有定义局部 y，会向上查找
        print(f"inner_func: y = {y}")  # 找到 enclosing y

    inner_func()


print("\n查找顺序演示:")
outer_func()


# ============================================================
# 五、global 关键字
# ============================================================

# global 用于在函数内部声明全局变量

total = 0


def add_to_total(value):
    """将值加到全局总和"""
    global total
    total += value
    print(f"当前总和: {total}")


print("\nglobal 关键字:")
add_to_total(10)
add_to_total(20)
add_to_total(30)
print(f"最终总和: {total}")


# 在函数内部创建全局变量
def create_global():
    """在函数内部创建全局变量"""
    global new_global_var
    new_global_var = "我是在函数内部创建的全局变量"


print("\n在函数内部创建全局变量:")
create_global()
print(new_global_var)


# ============================================================
# 六、nonlocal 关键字
# ============================================================

# nonlocal 用于在嵌套函数中修改外层函数的变量

def outer_counter():
    """外层函数"""
    count = 0

    def inner_increment():
        """内层函数"""
        nonlocal count  # 声明使用外层函数的 count
        count += 1
        print(f"count = {count}")

    return inner_increment


print("\nnonlocal 关键字:")
increment = outer_counter()
increment()  # count = 1
increment()  # count = 2
increment()  # count = 3


# 对比 global 和 nonlocal
def demonstrate_nonlocal():
    """演示 nonlocal 和 global 的区别"""
    x = "outer x"

    def inner():
        nonlocal x  # 修改外层函数的 x
        x = "modified by inner"
        print(f"inner: x = {x}")

    print(f"修改前: x = {x}")
    inner()
    print(f"修改后: x = {x}")


print("\nnonlocal vs global:")
demonstrate_nonlocal()


# ============================================================
# 七、闭包
# ============================================================

# 闭包：内层函数引用了外层函数的变量，并且外层函数返回内层函数

def make_multiplier(factor):
    """
    创建一个乘法器

    参数:
        factor: 乘数

    返回:
        一个函数，将输入乘以 factor
    """
    def multiplier(x):
        return x * factor  # 引用外层函数的 factor

    return multiplier


print("\n闭包:")
double = make_multiplier(2)
triple = make_multiplier(3)

print(f"double(5) = {double(5)}")  # 10
print(f"triple(5) = {triple(5)}")  # 15


# 闭包的实际应用：计数器
def make_counter():
    """创建一个计数器"""
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


print("\n闭包计数器:")
counter1 = make_counter()
counter2 = make_counter()

print(f"counter1: {counter1()}")  # 1
print(f"counter1: {counter1()}")  # 2
print(f"counter2: {counter2()}")  # 1（独立的计数器）
print(f"counter1: {counter1()}")  # 3


# ============================================================
# 八、变量遮蔽
# ============================================================

# 当局部变量和全局变量同名时，局部变量会遮蔽全局变量

name = "全局 name"


def shadow_example():
    """变量遮蔽示例"""
    name = "局部 name"  # 遮蔽了全局的 name
    print(f"函数内部: {name}")


print("\n变量遮蔽:")
shadow_example()
print(f"函数外部: {name}")  # 全局变量没有改变


# 注意：不要遮蔽内置函数名
# list = [1, 2, 3]  # 不要这样做！会遮蔽内置的 list 函数


# ============================================================
# 九、最佳实践
# ============================================================

print("\n最佳实践:")

# 1. 尽量避免使用全局变量
# 2. 如果需要共享状态，考虑使用类
# 3. 使用函数参数和返回值传递数据
# 4. 不要遮蔽内置函数名


# 不好的做法：使用全局变量
result = 0


def bad_add(a, b):
    global result
    result = a + b


# 好的做法：使用返回值
def good_add(a, b):
    return a + b


print("好的做法:")
result = good_add(3, 5)
print(f"result = {result}")


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("作用域综合练习")
    print("=" * 50)

    # 练习1：创建一个累加器
    def make_accumulator(initial=0):
        """
        创建一个累加器

        参数:
            initial: 初始值

        返回:
            一个函数，每次调用将值累加并返回当前总和
        """
        total = initial

        def accumulate(value):
            nonlocal total
            total += value
            return total

        return accumulate

    print("\n累加器:")
    acc = make_accumulator(100)
    print(f"累加 10: {acc(10)}")   # 110
    print(f"累加 20: {acc(20)}")   # 130
    print(f"累加 30: {acc(30)}")   # 160

    # 练习2：创建一个带记忆的函数
    def make_memory_function():
        """
        创建一个记住所有调用参数的函数
        """
        history = []

        def remember(value):
            history.append(value)
            return history.copy()

        return remember

    print("\n记忆函数:")
    remember = make_memory_function()
    print(f"记住 'a': {remember('a')}")
    print(f"记住 'b': {remember('b')}")
    print(f"记住 'c': {remember('c')}")

    # 练习3：创建一个限制调用次数的函数
    def make_limited_function(func, max_calls):
        """
        创建一个限制调用次数的函数

        参数:
            func: 原函数
            max_calls: 最大调用次数
        """
        calls = 0

        def limited(*args, **kwargs):
            nonlocal calls
            if calls >= max_calls:
                print(f"已达到最大调用次数 {max_calls}")
                return None
            calls += 1
            return func(*args, **kwargs)

        return limited

    print("\n限制调用次数:")
    limited_print = make_limited_function(print, 3)
    limited_print("第 1 次调用")
    limited_print("第 2 次调用")
    limited_print("第 3 次调用")
    limited_print("第 4 次调用")  # 不会执行

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. 作用域类型：
#    - Local（局部）：函数内部
#    - Enclosing（嵌套）：外层函数
#    - Global（全局）：模块级别
#    - Built-in（内置）：Python 内置
#
# 2. LEGB 规则：变量查找顺序 L -> E -> G -> B
#
# 3. 局部变量：
#    - 在函数内部定义
#    - 只能在函数内部访问
#
# 4. 全局变量：
#    - 在函数外部定义
#    - 函数内部读取不需要声明
#    - 函数内部修改需要 global 声明
#
# 5. global 关键字：在函数内部声明/修改全局变量
#
# 6. nonlocal 关键字：在嵌套函数中修改外层函数的变量
#
# 7. 闭包：内层函数引用外层函数的变量
#
# 8. 最佳实践：
#    - 尽量避免全局变量
#    - 使用参数和返回值传递数据
#    - 不要遮蔽内置函数名
