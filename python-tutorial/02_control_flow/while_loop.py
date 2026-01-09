"""
第2章：流程控制 - while 循环
==========================

本文件学习目标：
1. 掌握 while 循环的基本用法
2. 理解 while 循环与 for 循环的区别
3. 学会避免无限循环
4. 掌握 while-else 语句
"""

# ============================================================
# 一、while 循环基本语法
# ============================================================

# while 循环的语法：
# while 条件:
#     循环体（条件为真时重复执行）

# 示例：打印 1 到 5
print("打印 1 到 5:")
count = 1
while count <= 5:
    print(count, end=" ")
    count += 1  # 重要：必须更新条件，否则会无限循环
print()  # 换行

# 示例：计算 1 到 100 的和
total = 0
number = 1
while number <= 100:
    total += number
    number += 1
print(f"\n1 到 100 的和: {total}")


# ============================================================
# 二、while 循环 vs for 循环
# ============================================================

# for 循环：适合遍历已知序列，次数确定
# while 循环：适合条件控制，次数不确定

# 示例：用 for 循环打印 1 到 5
print("\nfor 循环:")
for i in range(1, 6):
    print(i, end=" ")
print()

# 示例：用 while 循环打印 1 到 5
print("while 循环:")
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1
print()

# while 循环更适合的场景：
# 1. 不知道要循环多少次
# 2. 需要根据某个条件来决定是否继续

# 示例：猜数字游戏（模拟）
print("\n猜数字游戏模拟:")
secret_number = 7
guesses = [3, 5, 7]  # 模拟用户的猜测
guess_index = 0

while guess_index < len(guesses):
    guess = guesses[guess_index]
    print(f"  猜测: {guess}", end=" -> ")

    if guess == secret_number:
        print("猜对了！")
        break
    elif guess < secret_number:
        print("太小了")
    else:
        print("太大了")

    guess_index += 1


# ============================================================
# 三、无限循环
# ============================================================

# 无限循环：条件永远为真，循环永不停止
# 通常是编程错误，但有时是故意的

# 错误示例（不要运行）：
# while True:
#     print("这会一直打印")  # 永远不会停止

# 正确使用无限循环：配合 break 使用
print("\n使用 break 退出无限循环:")
count = 0
while True:
    print(f"  循环次数: {count}")
    count += 1
    if count >= 3:
        print("  达到 3 次，退出循环")
        break

# 常见的无限循环错误：
# 1. 忘记更新循环变量
# 2. 条件写错，永远为真
# 3. 更新语句放在了 if 里面，某些情况下不执行


# ============================================================
# 四、while-else 语句
# ============================================================

# while 循环也可以带 else 子句
# 当循环正常结束（条件变为 False）时，执行 else
# 如果是被 break 中断的，不执行 else

print("\nwhile-else 示例:")

# 正常结束
count = 0
while count < 3:
    print(f"  count = {count}")
    count += 1
else:
    print("  循环正常结束")

# 被 break 中断
print("\n被 break 中断:")
count = 0
while count < 5:
    print(f"  count = {count}")
    if count == 2:
        print("  遇到 break，退出")
        break
    count += 1
else:
    print("  这行不会执行")  # 因为被 break 中断了


# ============================================================
# 五、实用示例
# ============================================================

# 示例1：输入验证（模拟）
print("\n输入验证示例:")
valid_inputs = ["yes", "no", "quit"]
test_inputs = ["maybe", "hello", "yes"]  # 模拟用户输入
input_index = 0

while input_index < len(test_inputs):
    user_input = test_inputs[input_index]
    print(f"  用户输入: {user_input}", end=" -> ")

    if user_input in valid_inputs:
        print("有效输入")
        break
    else:
        print("无效，请重新输入")
        input_index += 1

# 示例2：计算阶乘
print("\n计算阶乘:")
n = 5
factorial = 1
current = n

while current > 0:
    factorial *= current
    current -= 1

print(f"  {n}! = {factorial}")

# 示例3：找出第一个能被 7 整除的数
print("\n找第一个能被 7 整除的数:")
numbers = [12, 25, 33, 42, 55, 63]
index = 0

while index < len(numbers):
    if numbers[index] % 7 == 0:
        print(f"  找到: {numbers[index]}")
        break
    index += 1
else:
    print("  没有找到")


# ============================================================
# 六、循环控制技巧
# ============================================================

# 1. 使用标志变量
print("\n使用标志变量:")
found = False
numbers = [1, 3, 5, 7, 9, 11]
target = 7
index = 0

while index < len(numbers) and not found:
    if numbers[index] == target:
        found = True
        print(f"  在索引 {index} 找到 {target}")
    index += 1

if not found:
    print(f"  没有找到 {target}")

# 2. 使用计数器限制循环次数
print("\n限制循环次数:")
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    attempts += 1
    print(f"  尝试第 {attempts} 次")

print(f"  已达到最大尝试次数 {max_attempts}")

# 3. 使用哨兵值
print("\n使用哨兵值:")
# 哨兵值是一个特殊值，用于标记循环结束
data = [10, 20, 30, -1]  # -1 是哨兵值
index = 0
total = 0

while data[index] != -1:
    total += data[index]
    index += 1

print(f"  数据: {data[:-1]}")  # 不包括哨兵值
print(f"  总和: {total}")


# ============================================================
# 七、常见错误
# ============================================================

print("\n常见错误示例:")

# 错误1：条件永远为真
# x = 10
# while x > 0:  # x 永远大于 0
#     print(x)
#     # 忘记 x -= 1

# 错误2：更新语句位置错误
# count = 0
# while count < 5:
#     if count % 2 == 0:
#         count += 1  # 只在偶数时更新，奇数时无限循环
#     print(count)

# 错误3：off-by-one 错误（差一错误）
print("off-by-one 错误示例:")
# 想打印 1 到 5，但写成了：
count = 1
while count < 5:  # 应该是 count <= 5
    print(count, end=" ")
    count += 1
print(" <- 少打印了 5")

# 正确写法
count = 1
while count <= 5:
    print(count, end=" ")
    count += 1
print(" <- 正确")


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("while 循环综合练习")
    print("=" * 50)

    # 练习1：斐波那契数列（前 10 个）
    print("\n斐波那契数列（前 10 个）:")
    a, b = 0, 1
    count = 0
    while count < 10:
        print(a, end=" ")
        a, b = b, a + b
        count += 1
    print()

    # 练习2：数字反转
    print("\n数字反转:")
    number = 12345
    reversed_num = 0
    temp = number

    while temp > 0:
        digit = temp % 10  # 取最后一位
        reversed_num = reversed_num * 10 + digit
        temp //= 10  # 去掉最后一位

    print(f"  原数字: {number}")
    print(f"  反转后: {reversed_num}")

    # 练习3：求最大公约数（辗转相除法）
    print("\n求最大公约数:")
    num1 = 48
    num2 = 18
    a, b = num1, num2

    while b != 0:
        a, b = b, a % b

    print(f"  {num1} 和 {num2} 的最大公约数是: {a}")

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. while 循环语法：while 条件:
#
# 2. while vs for：
#    - for：遍历序列，次数确定
#    - while：条件控制，次数不确定
#
# 3. 避免无限循环：
#    - 确保条件最终会变为 False
#    - 确保循环变量会被更新
#
# 4. while-else：
#    - 正常结束执行 else
#    - break 中断不执行 else
#
# 5. 常用技巧：
#    - 标志变量
#    - 计数器限制
#    - 哨兵值
#
# 6. 常见错误：
#    - 条件永远为真
#    - 更新语句位置错误
#    - off-by-one 错误
