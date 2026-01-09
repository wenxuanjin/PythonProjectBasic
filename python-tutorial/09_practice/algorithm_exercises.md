# 算法思维练习题

本文件包含算法相关的练习题，帮助培养算法思维和问题解决能力。

## 一、排序算法（3题）

### 练习 A1：选择排序
实现选择排序算法。

选择排序思路：
1. 找到数组中最小的元素，与第一个元素交换
2. 找到剩余元素中最小的，与第二个元素交换
3. 重复直到排序完成

```python
def selection_sort(arr):
    """
    选择排序

    参数:
        arr: 待排序的列表

    返回:
        排序后的列表
    """
    # 你的代码
    pass

# 测试
arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))  # [11, 12, 22, 25, 64]
```

### 练习 A2：插入排序
实现插入排序算法。

插入排序思路：
1. 从第二个元素开始
2. 将当前元素插入到前面已排序部分的正确位置
3. 重复直到所有元素都被插入

```python
def insertion_sort(arr):
    """
    插入排序
    """
    # 你的代码
    pass
```

### 练习 A3：归并排序
实现归并排序算法（分治思想）。

归并排序思路：
1. 将数组分成两半
2. 递归地对两半进行排序
3. 合并两个有序数组

```python
def merge_sort(arr):
    """
    归并排序
    """
    # 你的代码
    pass
```

---

## 二、查找算法（2题）

### 练习 A4：查找第 K 大的元素
在未排序的数组中找到第 K 大的元素。

```python
def find_kth_largest(nums, k):
    """
    找到第 K 大的元素

    参数:
        nums: 数字列表
        k: 第 K 大

    返回:
        第 K 大的元素

    示例:
        find_kth_largest([3,2,1,5,6,4], 2) -> 5
    """
    # 你的代码
    pass
```

### 练习 A5：查找峰值元素
峰值元素是指其值大于左右相邻值的元素。
给定一个数组，找到峰值元素的索引。

```python
def find_peak_element(nums):
    """
    找到峰值元素的索引

    参数:
        nums: 数字列表

    返回:
        峰值元素的索引

    示例:
        find_peak_element([1,2,3,1]) -> 2
        find_peak_element([1,2,1,3,5,6,4]) -> 1 或 5
    """
    # 你的代码
    pass
```

---

## 三、递归与动态规划（3题）

### 练习 A6：爬楼梯
假设你正在爬楼梯，需要 n 阶才能到达楼顶。
每次你可以爬 1 或 2 个台阶。
有多少种不同的方法可以爬到楼顶？

```python
def climb_stairs(n):
    """
    爬楼梯

    参数:
        n: 楼梯阶数

    返回:
        爬到楼顶的方法数

    示例:
        climb_stairs(2) -> 2  (1+1, 2)
        climb_stairs(3) -> 3  (1+1+1, 1+2, 2+1)
    """
    # 你的代码
    pass
```

### 练习 A7：最大子数组和
给定一个整数数组，找到一个具有最大和的连续子数组，返回其最大和。

```python
def max_subarray(nums):
    """
    最大子数组和

    参数:
        nums: 整数列表

    返回:
        最大子数组的和

    示例:
        max_subarray([-2,1,-3,4,-1,2,1,-5,4]) -> 6
        解释: 连续子数组 [4,-1,2,1] 的和最大，为 6
    """
    # 你的代码
    pass
```

### 练习 A8：零钱兑换
给定不同面额的硬币和一个总金额，计算凑成总金额所需的最少硬币个数。

```python
def coin_change(coins, amount):
    """
    零钱兑换

    参数:
        coins: 硬币面额列表
        amount: 总金额

    返回:
        最少硬币个数，如果无法凑成返回 -1

    示例:
        coin_change([1, 2, 5], 11) -> 3  (5+5+1)
        coin_change([2], 3) -> -1
    """
    # 你的代码
    pass
```

---

## 四、字符串算法（2题）

### 练习 A9：回文判断
判断一个字符串是否是回文（忽略大小写和非字母数字字符）。

```python
def is_palindrome(s):
    """
    判断是否是回文

    参数:
        s: 字符串

    返回:
        True 如果是回文，否则 False

    示例:
        is_palindrome("A man, a plan, a canal: Panama") -> True
        is_palindrome("race a car") -> False
    """
    # 你的代码
    pass
```

### 练习 A10：最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

```python
def longest_common_prefix(strs):
    """
    最长公共前缀

    参数:
        strs: 字符串列表

    返回:
        最长公共前缀

    示例:
        longest_common_prefix(["flower","flow","flight"]) -> "fl"
        longest_common_prefix(["dog","racecar","car"]) -> ""
    """
    # 你的代码
    pass
```

---

## 五、数据结构应用（2题）

### 练习 A11：有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效条件：
1. 左括号必须用相同类型的右括号闭合
2. 左括号必须以正确的顺序闭合

```python
def is_valid_parentheses(s):
    """
    有效的括号

    参数:
        s: 括号字符串

    返回:
        True 如果有效，否则 False

    示例:
        is_valid_parentheses("()") -> True
        is_valid_parentheses("()[]{}") -> True
        is_valid_parentheses("(]") -> False
        is_valid_parentheses("([)]") -> False
    """
    # 你的代码
    pass
```

### 练习 A12：两数之和
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数的索引。

```python
def two_sum(nums, target):
    """
    两数之和

    参数:
        nums: 整数列表
        target: 目标值

    返回:
        两个数的索引列表

    示例:
        two_sum([2, 7, 11, 15], 9) -> [0, 1]
        解释: nums[0] + nums[1] = 2 + 7 = 9
    """
    # 你的代码
    pass
```

---

## 提示

1. 先理解问题，画图分析
2. 考虑边界情况
3. 先写出暴力解法，再优化
4. 分析时间复杂度和空间复杂度
5. 对照 `10_answers/algorithm_answers.py` 检查答案
