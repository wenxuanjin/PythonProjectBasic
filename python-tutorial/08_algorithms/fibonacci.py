"""
第8章：基础算法 - 斐波那契数列
============================

本文件学习目标：
1. 理解斐波那契数列的定义
2. 掌握递归实现方式
3. 掌握迭代实现方式
4. 对比两种方式的性能
5. 理解时间复杂度的概念
"""

# ============================================================
# 一、什么是斐波那契数列？
# ============================================================
#
# 斐波那契数列是一个经典的数学序列：
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# 定义：
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2)  (n >= 2)
#
# 每个数都是前两个数的和。
#
# 斐波那契数列在自然界中广泛存在：
# - 向日葵的种子排列
# - 松果的鳞片
# - 贝壳的螺旋


# ============================================================
# 二、递归实现
# ============================================================

print("斐波那契数列 - 递归实现:")
print("=" * 50)


def fibonacci_recursive(n):
    """
    递归方式计算斐波那契数列第 n 项

    思路：
    直接按照数学定义实现
    F(n) = F(n-1) + F(n-2)

    参数:
        n: 第 n 项（从 0 开始）

    返回:
        第 n 项的值

    时间复杂度: O(2^n) - 指数级，非常慢
    空间复杂度: O(n) - 递归调用栈
    """
    # 基本情况（递归终止条件）
    if n == 0:
        return 0
    if n == 1:
        return 1

    # 递归情况
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# 测试递归实现
print("\n递归实现结果:")
for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")


# 递归的问题：重复计算
# 计算 F(5) 时：
#   F(5) = F(4) + F(3)
#   F(4) = F(3) + F(2)  <- F(3) 被计算了两次
#   F(3) = F(2) + F(1)  <- F(2) 被计算了多次
#   ...


# ============================================================
# 三、迭代实现
# ============================================================

print("\n" + "=" * 50)
print("斐波那契数列 - 迭代实现:")


def fibonacci_iterative(n):
    """
    迭代方式计算斐波那契数列第 n 项

    思路：
    从前往后计算，保存前两个数，逐步推进

    参数:
        n: 第 n 项（从 0 开始）

    返回:
        第 n 项的值

    时间复杂度: O(n) - 线性，高效
    空间复杂度: O(1) - 只用了几个变量
    """
    # 处理基本情况
    if n == 0:
        return 0
    if n == 1:
        return 1

    # 初始化前两个数
    prev2 = 0  # F(0)
    prev1 = 1  # F(1)

    # 从 F(2) 开始计算到 F(n)
    for i in range(2, n + 1):
        current = prev1 + prev2  # F(i) = F(i-1) + F(i-2)
        prev2 = prev1  # 更新 F(i-2)
        prev1 = current  # 更新 F(i-1)

    return prev1


# 测试迭代实现
print("\n迭代实现结果:")
for i in range(10):
    print(f"F({i}) = {fibonacci_iterative(i)}")


# ============================================================
# 四、生成斐波那契数列
# ============================================================

print("\n" + "=" * 50)
print("生成斐波那契数列:")


def fibonacci_sequence(n):
    """
    生成前 n 个斐波那契数

    参数:
        n: 要生成的数量

    返回:
        包含前 n 个斐波那契数的列表
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]

    sequence = [0, 1]
    for i in range(2, n):
        next_num = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_num)

    return sequence


# 生成前 15 个斐波那契数
print("\n前 15 个斐波那契数:")
fib_seq = fibonacci_sequence(15)
print(fib_seq)


# 使用生成器（内存效率更高）
def fibonacci_generator(n):
    """
    斐波那契数列生成器

    使用生成器可以节省内存，适合处理大量数据
    """
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


print("\n使用生成器:")
for num in fibonacci_generator(10):
    print(num, end=" ")
print()


# ============================================================
# 五、性能对比
# ============================================================

print("\n" + "=" * 50)
print("性能对比:")

import time


def measure_time(func, n, name):
    """测量函数执行时间"""
    start = time.time()
    result = func(n)
    end = time.time()
    print(f"{name}: F({n}) = {result}, 耗时: {end - start:.6f} 秒")
    return end - start


# 对比小数值
print("\n计算 F(30):")
measure_time(fibonacci_iterative, 30, "迭代")
# 递归太慢，只测试较小的值
measure_time(fibonacci_recursive, 30, "递归")

# 迭代可以计算更大的值
print("\n计算 F(100)（仅迭代）:")
measure_time(fibonacci_iterative, 100, "迭代")

# 递归计算 F(35) 就已经很慢了
# measure_time(fibonacci_recursive, 35, "递归")  # 非常慢！


# ============================================================
# 六、带记忆化的递归
# ============================================================

print("\n" + "=" * 50)
print("带记忆化的递归:")


def fibonacci_memoized(n, memo=None):
    """
    带记忆化的递归实现

    思路：
    使用字典保存已计算的结果，避免重复计算

    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    if memo is None:
        memo = {}

    # 检查是否已经计算过
    if n in memo:
        return memo[n]

    # 基本情况
    if n == 0:
        return 0
    if n == 1:
        return 1

    # 计算并保存结果
    result = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    memo[n] = result

    return result


# 使用 functools.lru_cache 装饰器（更简洁）
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci_cached(n):
    """
    使用 lru_cache 装饰器的递归实现

    lru_cache 自动缓存函数的返回值
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


print("\n带记忆化的递归:")
measure_time(fibonacci_memoized, 100, "记忆化递归")
measure_time(fibonacci_cached, 100, "lru_cache")


# ============================================================
# 七、时间复杂度分析
# ============================================================

print("\n" + "=" * 50)
print("时间复杂度分析:")

print("""
不同实现方式的时间复杂度：

1. 普通递归: O(2^n)
   - 每次调用产生两个子调用
   - 存在大量重复计算
   - n=40 时就已经很慢

2. 迭代: O(n)
   - 只需要一次遍历
   - 没有重复计算
   - 可以计算很大的 n

3. 记忆化递归: O(n)
   - 每个值只计算一次
   - 需要额外的存储空间
   - 性能接近迭代

空间复杂度：
- 普通递归: O(n) - 递归调用栈
- 迭代: O(1) - 只用几个变量
- 记忆化递归: O(n) - 缓存空间
""")


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("斐波那契数列综合练习")
    print("=" * 50)

    # 练习1：找出小于 1000 的所有斐波那契数
    print("\n小于 1000 的斐波那契数:")
    fib_under_1000 = []
    a, b = 0, 1
    while a < 1000:
        fib_under_1000.append(a)
        a, b = b, a + b
    print(fib_under_1000)

    # 练习2：判断一个数是否是斐波那契数
    def is_fibonacci(num):
        """判断一个数是否是斐波那契数"""
        if num < 0:
            return False
        a, b = 0, 1
        while a < num:
            a, b = b, a + b
        return a == num

    print("\n判断是否是斐波那契数:")
    test_numbers = [0, 1, 2, 3, 4, 5, 8, 10, 13, 20, 21]
    for num in test_numbers:
        result = "是" if is_fibonacci(num) else "不是"
        print(f"  {num} {result}斐波那契数")

    # 练习3：计算斐波那契数列的比值（趋近黄金比例）
    print("\n斐波那契数列的比值（趋近黄金比例 1.618...）:")
    a, b = 1, 1
    for i in range(15):
        ratio = b / a
        print(f"  F({i+2})/F({i+1}) = {b}/{a} = {ratio:.6f}")
        a, b = b, a + b

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. 斐波那契数列定义：
#    F(0) = 0, F(1) = 1
#    F(n) = F(n-1) + F(n-2)
#
# 2. 递归实现：
#    - 直接按定义实现
#    - 时间复杂度 O(2^n)，非常慢
#    - 存在大量重复计算
#
# 3. 迭代实现：
#    - 从前往后计算
#    - 时间复杂度 O(n)，高效
#    - 空间复杂度 O(1)
#
# 4. 记忆化递归：
#    - 缓存已计算的结果
#    - 时间复杂度 O(n)
#    - 可以使用 @lru_cache 装饰器
#
# 5. 性能对比：
#    - 迭代 > 记忆化递归 >> 普通递归
#    - 实际应用中推荐使用迭代
