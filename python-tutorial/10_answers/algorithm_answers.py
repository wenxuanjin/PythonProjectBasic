"""
第10章：标准答案 - 算法练习答案
==============================

本文件包含 09_practice/algorithm_exercises.md 中所有练习题的标准答案。
"""

# ============================================================
# 一、排序算法（3题）
# ============================================================

print("=" * 60)
print("一、排序算法")
print("=" * 60)


# 练习 A1：选择排序
print("\n练习 A1：选择排序")


def selection_sort(arr):
    """
    选择排序

    思路：每次找到最小元素，放到已排序部分的末尾

    时间复杂度: O(n^2)
    空间复杂度: O(1)
    """
    arr = arr.copy()
    n = len(arr)

    for i in range(n - 1):
        # 找到未排序部分的最小元素
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # 交换到已排序部分的末尾
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


test_arr = [64, 25, 12, 22, 11]
print(f"原数组: {test_arr}")
print(f"排序后: {selection_sort(test_arr)}")


# 练习 A2：插入排序
print("\n练习 A2：插入排序")


def insertion_sort(arr):
    """
    插入排序

    思路：将每个元素插入到前面已排序部分的正确位置

    时间复杂度: O(n^2)
    空间复杂度: O(1)
    """
    arr = arr.copy()
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # 将大于 key 的元素向后移动
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


test_arr = [12, 11, 13, 5, 6]
print(f"原数组: {test_arr}")
print(f"排序后: {insertion_sort(test_arr)}")


# 练习 A3：归并排序
print("\n练习 A3：归并排序")


def merge_sort(arr):
    """
    归并排序

    思路：分治法，将数组分成两半，分别排序后合并

    时间复杂度: O(n log n)
    空间复杂度: O(n)
    """
    if len(arr) <= 1:
        return arr

    # 分割
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 合并
    return merge(left, right)


def merge(left, right):
    """合并两个有序数组"""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


test_arr = [38, 27, 43, 3, 9, 82, 10]
print(f"原数组: {test_arr}")
print(f"排序后: {merge_sort(test_arr)}")


# ============================================================
# 二、查找算法（2题）
# ============================================================

print("\n" + "=" * 60)
print("二、查找算法")
print("=" * 60)


# 练习 A4：查找第 K 大的元素
print("\n练习 A4：查找第 K 大的元素")


def find_kth_largest(nums, k):
    """
    找到第 K 大的元素

    方法1：排序后取第 K 个（简单但不是最优）
    时间复杂度: O(n log n)
    """
    sorted_nums = sorted(nums, reverse=True)
    return sorted_nums[k - 1]


# 方法2：使用堆（更优）
import heapq


def find_kth_largest_heap(nums, k):
    """使用最小堆，时间复杂度 O(n log k)"""
    return heapq.nlargest(k, nums)[-1]


nums = [3, 2, 1, 5, 6, 4]
print(f"数组: {nums}")
print(f"第2大的元素: {find_kth_largest(nums, 2)}")
print(f"第4大的元素: {find_kth_largest(nums, 4)}")


# 练习 A5：查找峰值元素
print("\n练习 A5：查找峰值元素")


def find_peak_element(nums):
    """
    找到峰值元素的索引

    使用二分查找，时间复杂度 O(log n)
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            # 峰值在左边（包括 mid）
            right = mid
        else:
            # 峰值在右边
            left = mid + 1

    return left


nums = [1, 2, 3, 1]
print(f"数组: {nums}")
print(f"峰值索引: {find_peak_element(nums)}")

nums = [1, 2, 1, 3, 5, 6, 4]
print(f"数组: {nums}")
print(f"峰值索引: {find_peak_element(nums)}")


# ============================================================
# 三、递归与动态规划（3题）
# ============================================================

print("\n" + "=" * 60)
print("三、递归与动态规划")
print("=" * 60)


# 练习 A6：爬楼梯
print("\n练习 A6：爬楼梯")


def climb_stairs(n):
    """
    爬楼梯

    动态规划：dp[i] = dp[i-1] + dp[i-2]
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
    if n <= 2:
        return n

    prev2, prev1 = 1, 2
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current

    return prev1


for n in range(1, 8):
    print(f"climb_stairs({n}) = {climb_stairs(n)}")


# 练习 A7：最大子数组和
print("\n练习 A7：最大子数组和")


def max_subarray(nums):
    """
    最大子数组和（Kadane 算法）

    思路：遍历数组，维护当前最大和和全局最大和
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
    if not nums:
        return 0

    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        # 要么加入当前子数组，要么从当前元素重新开始
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"数组: {nums}")
print(f"最大子数组和: {max_subarray(nums)}")


# 练习 A8：零钱兑换
print("\n练习 A8：零钱兑换")


def coin_change(coins, amount):
    """
    零钱兑换

    动态规划：dp[i] 表示凑成金额 i 所需的最少硬币数
    时间复杂度: O(amount * len(coins))
    空间复杂度: O(amount)
    """
    # dp[i] 表示凑成金额 i 所需的最少硬币数
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


print(f"coin_change([1, 2, 5], 11) = {coin_change([1, 2, 5], 11)}")
print(f"coin_change([2], 3) = {coin_change([2], 3)}")


# ============================================================
# 四、字符串算法（2题）
# ============================================================

print("\n" + "=" * 60)
print("四、字符串算法")
print("=" * 60)


# 练习 A9：回文判断
print("\n练习 A9：回文判断")


def is_palindrome(s):
    """
    判断是否是回文（忽略大小写和非字母数字字符）

    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    # 只保留字母和数字，转为小写
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


test_strings = [
    "A man, a plan, a canal: Panama",
    "race a car",
    "Was it a car or a cat I saw?"
]
for s in test_strings:
    print(f"'{s}' -> {is_palindrome(s)}")


# 练习 A10：最长公共前缀
print("\n练习 A10：最长公共前缀")


def longest_common_prefix(strs):
    """
    最长公共前缀

    时间复杂度: O(S)，S 是所有字符串的字符总数
    """
    if not strs:
        return ""

    # 以第一个字符串为基准
    prefix = strs[0]

    for s in strs[1:]:
        # 逐步缩短前缀
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix


print(f"['flower','flow','flight'] -> '{longest_common_prefix(['flower','flow','flight'])}'")
print(f"['dog','racecar','car'] -> '{longest_common_prefix(['dog','racecar','car'])}'")


# ============================================================
# 五、数据结构应用（2题）
# ============================================================

print("\n" + "=" * 60)
print("五、数据结构应用")
print("=" * 60)


# 练习 A11：有效的括号
print("\n练习 A11：有效的括号")


def is_valid_parentheses(s):
    """
    有效的括号

    使用栈，时间复杂度 O(n)
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            # 右括号
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            # 左括号
            stack.append(char)

    return len(stack) == 0


test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}"]
for s in test_cases:
    print(f"'{s}' -> {is_valid_parentheses(s)}")


# 练习 A12：两数之和
print("\n练习 A12：两数之和")


def two_sum(nums, target):
    """
    两数之和

    使用哈希表，时间复杂度 O(n)
    """
    seen = {}  # 值 -> 索引

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []


nums = [2, 7, 11, 15]
target = 9
print(f"nums = {nums}, target = {target}")
print(f"结果: {two_sum(nums, target)}")

nums = [3, 2, 4]
target = 6
print(f"nums = {nums}, target = {target}")
print(f"结果: {two_sum(nums, target)}")


print("\n" + "=" * 60)
print("算法练习答案完成！")
print("=" * 60)
