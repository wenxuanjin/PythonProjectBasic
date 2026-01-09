"""
第2章：流程控制 - break 和 continue
==================================

本文件学习目标：
1. 掌握 break 语句的用法
2. 掌握 continue 语句的用法
3. 理解 break 和 continue 的区别
4. 学会在嵌套循环中使用 break
"""

# ============================================================
# 一、break 语句
# ============================================================

# break 语句用于立即退出循环
# 不管循环条件是否还满足，都会退出

# 示例：找到第一个偶数就退出
print("找到第一个偶数:")
numbers = [1, 3, 5, 8, 9, 10]

for num in numbers:
    print(f"  检查 {num}...", end=" ")
    if num % 2 == 0:
        print(f"找到偶数 {num}，退出循环")
        break
    print("是奇数，继续")

# 示例：在 while 循环中使用 break
print("\nwhile 循环中的 break:")
count = 0
while True:  # 无限循环
    print(f"  count = {count}")
    count += 1
    if count >= 3:
        print("  count >= 3，退出循环")
        break


# ============================================================
# 二、continue 语句
# ============================================================

# continue 语句用于跳过当前迭代，继续下一次迭代
# 不会退出循环，只是跳过本次

# 示例：打印奇数，跳过偶数
print("\n打印 1-10 中的奇数:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # 跳过偶数
    print(i, end=" ")
print()

# 示例：跳过特定值
print("\n跳过数字 5:")
for i in range(1, 10):
    if i == 5:
        continue
    print(i, end=" ")
print()


# ============================================================
# 三、break vs continue
# ============================================================

print("\nbreak vs continue 对比:")

# break：完全退出循环
print("使用 break:")
for i in range(1, 6):
    if i == 3:
        print(f"  i={i}，遇到 break，退出")
        break
    print(f"  i={i}")
# 输出：1, 2, 然后退出

# continue：跳过当前，继续下一次
print("\n使用 continue:")
for i in range(1, 6):
    if i == 3:
        print(f"  i={i}，遇到 continue，跳过")
        continue
    print(f"  i={i}")
# 输出：1, 2, 跳过3, 4, 5


# ============================================================
# 四、在嵌套循环中使用 break
# ============================================================

# break 只能退出当前所在的循环，不能退出外层循环

print("\n嵌套循环中的 break:")
for i in range(1, 4):
    print(f"外层循环 i={i}")
    for j in range(1, 4):
        if j == 2:
            print(f"  内层 j={j}，break 退出内层循环")
            break
        print(f"  内层 j={j}")
    print(f"外层循环 i={i} 继续")

# 如果想退出所有循环，可以使用标志变量
print("\n使用标志变量退出所有循环:")
should_break = False

for i in range(1, 4):
    if should_break:
        break
    print(f"外层 i={i}")
    for j in range(1, 4):
        print(f"  内层 j={j}")
        if i == 2 and j == 2:
            print("  设置标志，准备退出所有循环")
            should_break = True
            break


# ============================================================
# 五、实用示例
# ============================================================

# 示例1：验证用户输入（模拟）
print("\n验证用户输入:")
valid_passwords = ["123456", "password", "admin"]
attempts = ["wrong1", "wrong2", "123456"]  # 模拟输入

for i, password in enumerate(attempts, 1):
    print(f"  第 {i} 次尝试: {password}", end=" -> ")
    if password in valid_passwords:
        print("密码正确！")
        break
    print("密码错误")
else:
    print("  尝试次数用完")

# 示例2：处理数据，跳过无效值
print("\n处理数据，跳过无效值:")
data = [10, -5, 20, None, 30, "error", 40]
total = 0
valid_count = 0

for item in data:
    # 跳过无效数据
    if item is None:
        print(f"  跳过 None")
        continue
    if not isinstance(item, (int, float)):
        print(f"  跳过非数字: {item}")
        continue
    if item < 0:
        print(f"  跳过负数: {item}")
        continue

    total += item
    valid_count += 1
    print(f"  处理: {item}")

print(f"有效数据总和: {total}")
print(f"有效数据个数: {valid_count}")

# 示例3：查找矩阵中的目标值
print("\n在矩阵中查找目标值:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
target = 5
found = False

for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        if value == target:
            print(f"  找到 {target}，位置: ({i}, {j})")
            found = True
            break
    if found:
        break

if not found:
    print(f"  没有找到 {target}")


# ============================================================
# 六、pass 语句
# ============================================================

# pass 是一个空语句，什么都不做
# 用于占位，保持代码结构完整

print("\npass 语句示例:")

# 用于空函数
def not_implemented_yet():
    pass  # 以后再实现

# 用于空循环
for i in range(5):
    pass  # 暂时不做任何事

# 用于空条件分支
x = 10
if x > 0:
    pass  # 正数，暂不处理
else:
    print("非正数")

print("pass 语句不会产生任何输出")


# ============================================================
# 七、常见错误和注意事项
# ============================================================

print("\n常见错误和注意事项:")

# 1. continue 在 while 循环中要小心
print("while 循环中 continue 的陷阱:")
count = 0
while count < 5:
    count += 1  # 更新语句要在 continue 之前
    if count == 3:
        print(f"  跳过 {count}")
        continue
    print(f"  处理 {count}")

# 错误示例（会导致无限循环）：
# count = 0
# while count < 5:
#     if count == 3:
#         continue  # count 永远是 3，无限循环
#     print(count)
#     count += 1

# 2. break 只退出最内层循环
print("\nbreak 只退出最内层循环:")
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # 只退出内层循环
        print(f"  ({i}, {j})")

# 3. 不要过度使用 break 和 continue
# 过多的 break/continue 会让代码难以理解
# 有时候重构循环条件是更好的选择


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("break 和 continue 综合练习")
    print("=" * 50)

    # 练习1：找出列表中第一个质数
    print("\n找出第一个质数:")
    numbers = [4, 6, 8, 9, 11, 12, 13]

    for num in numbers:
        if num < 2:
            continue

        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(f"  第一个质数是: {num}")
            break

    # 练习2：统计有效成绩
    print("\n统计有效成绩:")
    scores = [85, -10, 92, 150, 78, 65, 200, 88]
    valid_scores = []

    for score in scores:
        if score < 0 or score > 100:
            print(f"  跳过无效成绩: {score}")
            continue
        valid_scores.append(score)
        print(f"  有效成绩: {score}")

    if valid_scores:
        average = sum(valid_scores) / len(valid_scores)
        print(f"平均成绩: {average:.2f}")

    # 练习3：简单的命令处理器（模拟）
    print("\n简单命令处理器:")
    commands = ["help", "status", "unknown", "quit", "more"]

    for cmd in commands:
        print(f"  收到命令: {cmd}", end=" -> ")

        if cmd == "quit":
            print("退出程序")
            break
        elif cmd == "help":
            print("显示帮助")
        elif cmd == "status":
            print("显示状态")
        else:
            print("未知命令，跳过")
            continue

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. break 语句：
#    - 立即退出当前循环
#    - 不执行循环的 else 子句
#
# 2. continue 语句：
#    - 跳过当前迭代，继续下一次
#    - 不退出循环
#
# 3. 嵌套循环中的 break：
#    - 只退出最内层循环
#    - 需要标志变量退出所有循环
#
# 4. pass 语句：
#    - 空语句，什么都不做
#    - 用于占位
#
# 5. 注意事项：
#    - while 循环中 continue 要小心更新语句位置
#    - 不要过度使用 break/continue
