"""
第8章：基础算法 - 二分查找
========================

本文件学习目标：
1. 理解二分查找的原理
2. 掌握二分查找的前提条件
3. 实现二分查找算法
4. 理解时间复杂度
"""

# ============================================================
# 一、什么是二分查找？
# ============================================================
#
# 二分查找（Binary Search）是一种高效的查找算法。
#
# 原理：
# 1. 在有序数组中查找目标值
# 2. 每次比较中间元素
# 3. 如果目标值小于中间元素，在左半部分继续查找
# 4. 如果目标值大于中间元素，在右半部分继续查找
# 5. 重复直到找到目标或确定不存在
#
# 前提条件：
# - 数组必须是有序的（升序或降序）
#
# 特点：
# - 时间复杂度 O(log n)，非常高效
# - 每次查找范围减半


# ============================================================
# 二、基本实现
# ============================================================

print("二分查找 - 基本实现:")
print("=" * 50)


def binary_search(arr, target):
    """
    二分查找 - 基本版本

    参数:
        arr: 有序数组（升序）
        target: 要查找的目标值

    返回:
        目标值的索引，如果不存在返回 -1

    时间复杂度: O(log n)
    空间复杂度: O(1)
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        # 计算中间位置
        # 使用 (left + right) // 2 可能会溢出（在其他语言中）
        # 使用 left + (right - left) // 2 更安全
        mid = left + (right - left) // 2

        print(f"  查找范围: [{left}, {right}], 中间位置: {mid}, 中间值: {arr[mid]}")

        if arr[mid] == target:
            # 找到目标
            print(f"  找到目标！")
            return mid
        elif arr[mid] < target:
            # 目标在右半部分
            print(f"  {arr[mid]} < {target}，在右半部分查找")
            left = mid + 1
        else:
            # 目标在左半部分
            print(f"  {arr[mid]} > {target}，在左半部分查找")
            right = mid - 1

    # 没有找到
    print(f"  未找到目标")
    return -1


# 测试基本实现
print("\n测试二分查找:")
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(f"数组: {arr}")

print(f"\n查找 7:")
result = binary_search(arr, 7)
print(f"结果: 索引 {result}")

print(f"\n查找 6:")
result = binary_search(arr, 6)
print(f"结果: 索引 {result}")


# ============================================================
# 三、递归实现
# ============================================================

print("\n" + "=" * 50)
print("二分查找 - 递归实现:")


def binary_search_recursive(arr, target, left=None, right=None):
    """
    二分查找 - 递归版本

    参数:
        arr: 有序数组
        target: 目标值
        left: 左边界
        right: 右边界

    返回:
        目标值的索引，如果不存在返回 -1

    时间复杂度: O(log n)
    空间复杂度: O(log n) - 递归调用栈
    """
    # 初始化边界
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1

    # 基本情况：查找范围为空
    if left > right:
        return -1

    # 计算中间位置
    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        # 在右半部分递归查找
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        # 在左半部分递归查找
        return binary_search_recursive(arr, target, left, mid - 1)


# 测试递归实现
print("\n测试递归实现:")
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(f"数组: {arr}")
print(f"查找 12: 索引 {binary_search_recursive(arr, 12)}")
print(f"查找 5: 索引 {binary_search_recursive(arr, 5)}")


# ============================================================
# 四、查找边界
# ============================================================

print("\n" + "=" * 50)
print("查找边界:")


def binary_search_left(arr, target):
    """
    查找目标值的左边界（第一个等于 target 的位置）

    如果有多个相同的值，返回最左边的索引
    """
    left = 0
    right = len(arr)

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    # 检查是否找到
    if left < len(arr) and arr[left] == target:
        return left
    return -1


def binary_search_right(arr, target):
    """
    查找目标值的右边界（最后一个等于 target 的位置）

    如果有多个相同的值，返回最右边的索引
    """
    left = 0
    right = len(arr)

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    # 检查是否找到
    if left > 0 and arr[left - 1] == target:
        return left - 1
    return -1


# 测试边界查找
print("\n测试边界查找:")
arr = [1, 2, 2, 2, 3, 4, 4, 5]
print(f"数组: {arr}")
print(f"查找 2 的左边界: {binary_search_left(arr, 2)}")
print(f"查找 2 的右边界: {binary_search_right(arr, 2)}")
print(f"查找 4 的左边界: {binary_search_left(arr, 4)}")
print(f"查找 4 的右边界: {binary_search_right(arr, 4)}")


# ============================================================
# 五、使用 bisect 模块
# ============================================================

print("\n" + "=" * 50)
print("使用 bisect 模块:")

import bisect

arr = [1, 3, 5, 7, 9, 11, 13, 15]
print(f"数组: {arr}")

# bisect_left: 返回插入位置（左边）
print(f"\nbisect_left(arr, 7): {bisect.bisect_left(arr, 7)}")
print(f"bisect_left(arr, 6): {bisect.bisect_left(arr, 6)}")

# bisect_right: 返回插入位置（右边）
print(f"\nbisect_right(arr, 7): {bisect.bisect_right(arr, 7)}")

# insort: 插入并保持有序
arr_copy = arr.copy()
bisect.insort(arr_copy, 6)
print(f"\n插入 6 后: {arr_copy}")


# ============================================================
# 六、时间复杂度分析
# ============================================================

print("\n" + "=" * 50)
print("时间复杂度分析:")

print("""
二分查找的时间复杂度：O(log n)

为什么是 O(log n)？
- 每次查找，范围减半
- n 个元素最多需要 log2(n) 次比较

例如：
- 1000 个元素：最多 10 次比较
- 1000000 个元素：最多 20 次比较
- 10亿个元素：最多 30 次比较

对比线性查找 O(n)：
- 1000 个元素：最多 1000 次比较
- 1000000 个元素：最多 1000000 次比较

二分查找比线性查找快得多！

前提条件：
- 数组必须有序
- 如果数组无序，需要先排序 O(n log n)
""")


# ============================================================
# 七、性能对比
# ============================================================

print("=" * 50)
print("性能对比:")

import time
import random


def linear_search(arr, target):
    """线性查找"""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


# 生成测试数据
sizes = [10000, 100000, 1000000]

for size in sizes:
    arr = list(range(size))  # 有序数组
    target = size - 1  # 查找最后一个元素（最坏情况）

    # 线性查找
    start = time.time()
    linear_search(arr, target)
    linear_time = time.time() - start

    # 二分查找
    start = time.time()
    binary_search_recursive(arr, target)
    binary_time = time.time() - start

    print(f"\n数组大小: {size}")
    print(f"  线性查找: {linear_time:.6f} 秒")
    print(f"  二分查找: {binary_time:.6f} 秒")
    if linear_time > 0:
        print(f"  二分查找快 {linear_time / max(binary_time, 0.000001):.0f} 倍")


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("二分查找综合练习")
    print("=" * 50)

    # 练习1：查找插入位置
    def search_insert(arr, target):
        """
        查找目标值应该插入的位置
        如果目标值存在，返回其索引
        如果不存在，返回应该插入的位置
        """
        left = 0
        right = len(arr)

        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left

    print("\n查找插入位置:")
    arr = [1, 3, 5, 6]
    print(f"数组: {arr}")
    print(f"插入 5 的位置: {search_insert(arr, 5)}")
    print(f"插入 2 的位置: {search_insert(arr, 2)}")
    print(f"插入 7 的位置: {search_insert(arr, 7)}")

    # 练习2：查找平方根
    def sqrt_int(x):
        """
        计算 x 的平方根（整数部分）
        使用二分查找
        """
        if x < 2:
            return x

        left = 1
        right = x // 2

        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1

        return right

    print("\n计算平方根（整数部分）:")
    for num in [4, 8, 16, 25, 100]:
        print(f"  sqrt({num}) = {sqrt_int(num)}")

    # 练习3：在旋转数组中查找
    def search_rotated(arr, target):
        """
        在旋转排序数组中查找目标值
        例如：[4,5,6,7,0,1,2] 是 [0,1,2,4,5,6,7] 旋转后的结果
        """
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return mid

            # 判断哪半部分是有序的
            if arr[left] <= arr[mid]:
                # 左半部分有序
                if arr[left] <= target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # 右半部分有序
                if arr[mid] < target <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

    print("\n在旋转数组中查找:")
    arr = [4, 5, 6, 7, 0, 1, 2]
    print(f"数组: {arr}")
    print(f"查找 0: 索引 {search_rotated(arr, 0)}")
    print(f"查找 3: 索引 {search_rotated(arr, 3)}")

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. 二分查找的前提：数组必须有序
#
# 2. 基本思路：
#    - 比较中间元素
#    - 根据比较结果缩小范围
#    - 每次范围减半
#
# 3. 时间复杂度：O(log n)
#
# 4. 实现方式：
#    - 迭代（推荐）
#    - 递归
#
# 5. 变体：
#    - 查找左边界
#    - 查找右边界
#    - 查找插入位置
#
# 6. Python 内置：bisect 模块
