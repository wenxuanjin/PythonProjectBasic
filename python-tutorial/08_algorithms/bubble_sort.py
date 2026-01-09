"""
第8章：基础算法 - 冒泡排序
========================

本文件学习目标：
1. 理解冒泡排序的原理
2. 掌握基本实现
3. 学会优化版本
4. 理解时间复杂度
"""

# ============================================================
# 一、什么是冒泡排序？
# ============================================================
#
# 冒泡排序是一种简单的排序算法。
#
# 原理：
# 1. 比较相邻的两个元素
# 2. 如果顺序错误，就交换它们
# 3. 重复这个过程，直到没有需要交换的元素
#
# 为什么叫"冒泡"？
# 因为较大的元素会像气泡一样"浮"到数组的末尾。
#
# 特点：
# - 简单易懂
# - 稳定排序（相等元素的相对顺序不变）
# - 效率较低，不适合大数据量


# ============================================================
# 二、基本实现
# ============================================================

print("冒泡排序 - 基本实现:")
print("=" * 50)


def bubble_sort_basic(arr):
    """
    冒泡排序 - 基本版本

    思路：
    外层循环控制轮数
    内层循环进行相邻元素比较和交换

    参数:
        arr: 待排序的列表

    返回:
        排序后的列表（原地排序）

    时间复杂度: O(n^2)
    空间复杂度: O(1)
    """
    n = len(arr)

    # 外层循环：需要进行 n-1 轮
    for i in range(n - 1):
        print(f"\n第 {i + 1} 轮:")

        # 内层循环：比较相邻元素
        # 每轮结束后，最大的元素会"冒泡"到末尾
        # 所以每轮可以少比较一个元素
        for j in range(n - 1 - i):
            print(f"  比较 arr[{j}]={arr[j]} 和 arr[{j+1}]={arr[j+1]}", end="")

            # 如果前面的元素大于后面的元素，交换
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f" -> 交换")
            else:
                print(f" -> 不交换")

        print(f"  本轮结束: {arr}")

    return arr


# 测试基本版本
print("\n测试基本版本:")
test_arr = [64, 34, 25, 12, 22, 11, 90]
print(f"原始数组: {test_arr}")
sorted_arr = bubble_sort_basic(test_arr.copy())
print(f"\n排序结果: {sorted_arr}")


# ============================================================
# 三、优化版本1：提前终止
# ============================================================

print("\n" + "=" * 50)
print("冒泡排序 - 优化版本1（提前终止）:")


def bubble_sort_optimized1(arr):
    """
    冒泡排序 - 优化版本1

    优化思路：
    如果某一轮没有发生任何交换，说明数组已经有序，可以提前结束

    时间复杂度:
    - 最坏情况: O(n^2)
    - 最好情况: O(n) - 数组已经有序时
    """
    n = len(arr)

    for i in range(n - 1):
        # 标记本轮是否发生交换
        swapped = False

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # 如果没有发生交换，说明已经有序
        if not swapped:
            print(f"第 {i + 1} 轮没有交换，提前结束")
            break

    return arr


# 测试优化版本1
print("\n测试优化版本1（已排序数组）:")
test_arr = [1, 2, 3, 4, 5, 6, 7]
print(f"原始数组: {test_arr}")
sorted_arr = bubble_sort_optimized1(test_arr.copy())
print(f"排序结果: {sorted_arr}")


# ============================================================
# 四、优化版本2：记录最后交换位置
# ============================================================

print("\n" + "=" * 50)
print("冒泡排序 - 优化版本2（记录最后交换位置）:")


def bubble_sort_optimized2(arr):
    """
    冒泡排序 - 优化版本2

    优化思路：
    记录每轮最后一次交换的位置
    下一轮只需要比较到这个位置即可

    这样可以减少不必要的比较
    """
    n = len(arr)
    # 最后一次交换的位置
    last_swap_index = n - 1

    for i in range(n - 1):
        # 本轮是否发生交换
        swapped = False
        # 本轮最后交换的位置
        current_swap_index = 0

        for j in range(last_swap_index):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                current_swap_index = j

        # 更新下一轮的比较范围
        last_swap_index = current_swap_index

        if not swapped:
            break

    return arr


# 测试优化版本2
print("\n测试优化版本2:")
test_arr = [3, 2, 1, 4, 5, 6, 7]
print(f"原始数组: {test_arr}")
sorted_arr = bubble_sort_optimized2(test_arr.copy())
print(f"排序结果: {sorted_arr}")


# ============================================================
# 五、可视化排序过程
# ============================================================

print("\n" + "=" * 50)
print("可视化排序过程:")


def bubble_sort_visual(arr):
    """
    冒泡排序 - 可视化版本

    显示每一步的排序过程
    """
    n = len(arr)
    arr = arr.copy()

    print(f"初始: {arr}")
    print("-" * 40)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

                # 可视化当前状态
                visual = ""
                for k, num in enumerate(arr):
                    if k == j or k == j + 1:
                        visual += f"[{num}]"
                    else:
                        visual += f" {num} "
                print(f"交换: {visual}")

        if not swapped:
            break

    print("-" * 40)
    print(f"结果: {arr}")
    return arr


# 测试可视化版本
print("\n测试可视化版本:")
test_arr = [5, 3, 8, 4, 2]
bubble_sort_visual(test_arr)


# ============================================================
# 六、时间复杂度分析
# ============================================================

print("\n" + "=" * 50)
print("时间复杂度分析:")

print("""
冒泡排序的时间复杂度：

1. 最坏情况: O(n^2)
   - 数组完全逆序
   - 需要进行 n-1 轮
   - 每轮比较 n-1, n-2, ..., 1 次
   - 总比较次数: n(n-1)/2

2. 最好情况: O(n)
   - 数组已经有序
   - 只需要一轮，发现没有交换就结束
   - 需要使用优化版本

3. 平均情况: O(n^2)

空间复杂度: O(1)
   - 只使用了几个临时变量
   - 原地排序

稳定性: 稳定
   - 相等元素的相对顺序不变
   - 因为只有 > 时才交换，= 时不交换
""")


# ============================================================
# 七、性能测试
# ============================================================

print("=" * 50)
print("性能测试:")

import time
import random


def measure_sort_time(sort_func, arr, name):
    """测量排序时间"""
    arr_copy = arr.copy()
    start = time.time()
    sort_func(arr_copy)
    end = time.time()
    print(f"{name}: {end - start:.6f} 秒")


# 生成测试数据
sizes = [100, 500, 1000]

for size in sizes:
    print(f"\n数组大小: {size}")
    random_arr = [random.randint(1, 1000) for _ in range(size)]
    measure_sort_time(bubble_sort_optimized1, random_arr, "冒泡排序")
    measure_sort_time(sorted, random_arr, "Python内置排序")


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("冒泡排序综合练习")
    print("=" * 50)

    # 练习1：降序排序
    def bubble_sort_desc(arr):
        """冒泡排序 - 降序"""
        n = len(arr)
        arr = arr.copy()
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if arr[j] < arr[j + 1]:  # 改变比较方向
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    print("\n降序排序:")
    test_arr = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"原始: {test_arr}")
    print(f"降序: {bubble_sort_desc(test_arr)}")

    # 练习2：对字符串列表排序
    print("\n字符串排序:")
    words = ["banana", "apple", "cherry", "date"]
    print(f"原始: {words}")

    def bubble_sort_strings(arr):
        """对字符串列表进行冒泡排序"""
        n = len(arr)
        arr = arr.copy()
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    print(f"排序: {bubble_sort_strings(words)}")

    # 练习3：按自定义规则排序
    print("\n按长度排序:")
    words = ["python", "is", "a", "great", "language"]
    print(f"原始: {words}")

    def bubble_sort_by_length(arr):
        """按字符串长度排序"""
        n = len(arr)
        arr = arr.copy()
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if len(arr[j]) > len(arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    print(f"按长度: {bubble_sort_by_length(words)}")

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. 冒泡排序原理：
#    - 比较相邻元素
#    - 如果顺序错误就交换
#    - 大元素"冒泡"到末尾
#
# 2. 基本实现：
#    - 外层循环控制轮数
#    - 内层循环比较相邻元素
#
# 3. 优化版本：
#    - 提前终止：没有交换时结束
#    - 记录最后交换位置：减少比较次数
#
# 4. 时间复杂度：
#    - 最坏: O(n^2)
#    - 最好: O(n)（优化版本）
#    - 平均: O(n^2)
#
# 5. 特点：
#    - 简单易懂
#    - 稳定排序
#    - 效率较低
