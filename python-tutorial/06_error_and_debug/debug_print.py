"""
第6章：异常与调试 - 使用 print 调试
=================================

本文件学习目标：
1. 学会使用 print 进行调试
2. 掌握调试的基本技巧
3. 理解常见的调试场景
4. 学会定位和解决问题
"""

# ============================================================
# 一、为什么使用 print 调试？
# ============================================================
#
# print 调试是最简单、最直接的调试方法。
#
# 优点：
# 1. 简单易用，不需要额外工具
# 2. 适合初学者
# 3. 可以快速定位问题
#
# 缺点：
# 1. 需要手动添加和删除
# 2. 大量 print 会影响代码可读性
# 3. 不适合复杂的调试场景


# ============================================================
# 二、基本的 print 调试
# ============================================================

print("基本的 print 调试:")
print("=" * 50)


def calculate_average(numbers):
    """计算平均值（带调试信息）"""
    print(f"[DEBUG] 输入: {numbers}")  # 调试：查看输入

    if not numbers:
        print("[DEBUG] 列表为空，返回 0")  # 调试：查看分支
        return 0

    total = sum(numbers)
    print(f"[DEBUG] 总和: {total}")  # 调试：查看中间结果

    count = len(numbers)
    print(f"[DEBUG] 数量: {count}")  # 调试：查看中间结果

    average = total / count
    print(f"[DEBUG] 平均值: {average}")  # 调试：查看结果

    return average


# 测试
print("\n测试 calculate_average:")
result = calculate_average([10, 20, 30, 40, 50])
print(f"最终结果: {result}")


# ============================================================
# 三、调试技巧
# ============================================================

print("\n" + "=" * 50)
print("调试技巧:")

# 技巧1：使用标记区分调试信息
print("\n技巧1：使用标记")


def debug_print(message, level="DEBUG"):
    """带标记的调试输出"""
    print(f"[{level}] {message}")


debug_print("这是调试信息")
debug_print("这是警告信息", "WARNING")
debug_print("这是错误信息", "ERROR")


# 技巧2：打印变量名和值
print("\n技巧2：打印变量名和值")

x = 10
y = 20
z = x + y

# 不好的方式
print(x)  # 不知道这是什么变量

# 好的方式
print(f"x = {x}")
print(f"y = {y}")
print(f"z = x + y = {z}")


# 技巧3：打印类型
print("\n技巧3：打印类型")

data = "123"
print(f"data = {data}, type = {type(data)}")

# 这可以帮助发现类型错误
# 比如：期望是 int，实际是 str


# 技巧4：打印函数调用
print("\n技巧4：打印函数调用")


def outer_function(x):
    print(f"[ENTER] outer_function(x={x})")
    result = inner_function(x * 2)
    print(f"[EXIT] outer_function, result={result}")
    return result


def inner_function(y):
    print(f"[ENTER] inner_function(y={y})")
    result = y + 10
    print(f"[EXIT] inner_function, result={result}")
    return result


outer_function(5)


# 技巧5：打印循环状态
print("\n技巧5：打印循环状态")


def find_first_even(numbers):
    """找到第一个偶数"""
    for i, num in enumerate(numbers):
        print(f"[LOOP] i={i}, num={num}, is_even={num % 2 == 0}")
        if num % 2 == 0:
            print(f"[FOUND] 找到偶数: {num}")
            return num
    print("[NOT FOUND] 没有找到偶数")
    return None


find_first_even([1, 3, 5, 6, 7, 8])


# ============================================================
# 四、调试开关
# ============================================================

print("\n" + "=" * 50)
print("调试开关:")

# 使用全局变量控制调试输出
DEBUG = True


def debug(message):
    """可控制的调试输出"""
    if DEBUG:
        print(f"[DEBUG] {message}")


debug("这条信息会显示")

DEBUG = False
debug("这条信息不会显示")

DEBUG = True  # 恢复


# ============================================================
# 五、常见调试场景
# ============================================================

print("\n" + "=" * 50)
print("常见调试场景:")

# 场景1：循环不按预期执行
print("\n场景1：循环调试")


def sum_until_100(numbers):
    """累加直到超过100"""
    total = 0
    for i, num in enumerate(numbers):
        print(f"[DEBUG] 第{i}次循环: num={num}, total={total}")
        total += num
        if total > 100:
            print(f"[DEBUG] 超过100，退出循环")
            break
    return total


result = sum_until_100([10, 20, 30, 40, 50])
print(f"结果: {result}")


# 场景2：条件判断不正确
print("\n场景2：条件判断调试")


def check_score(score):
    """检查成绩等级"""
    print(f"[DEBUG] 输入分数: {score}, 类型: {type(score)}")

    if score >= 90:
        print("[DEBUG] 进入 >= 90 分支")
        return "A"
    elif score >= 80:
        print("[DEBUG] 进入 >= 80 分支")
        return "B"
    elif score >= 60:
        print("[DEBUG] 进入 >= 60 分支")
        return "C"
    else:
        print("[DEBUG] 进入 else 分支")
        return "D"


print(f"85分等级: {check_score(85)}")


# 场景3：函数返回值不正确
print("\n场景3：函数返回值调试")


def process_data(data):
    """处理数据"""
    print(f"[DEBUG] 输入: {data}")

    # 步骤1
    step1_result = [x * 2 for x in data]
    print(f"[DEBUG] 步骤1结果: {step1_result}")

    # 步骤2
    step2_result = [x for x in step1_result if x > 5]
    print(f"[DEBUG] 步骤2结果: {step2_result}")

    # 步骤3
    final_result = sum(step2_result)
    print(f"[DEBUG] 最终结果: {final_result}")

    return final_result


process_data([1, 2, 3, 4, 5])


# ============================================================
# 六、调试后的清理
# ============================================================

print("\n" + "=" * 50)
print("调试后的清理:")

print("""
调试完成后，记得：

1. 删除或注释掉调试代码
   # print(f"[DEBUG] ...")

2. 或者使用 logging 模块替代 print
   import logging
   logging.debug("调试信息")

3. 使用 IDE 的调试功能
   - 设置断点
   - 单步执行
   - 查看变量

4. 保留有用的日志
   - 错误日志
   - 关键操作日志
""")


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("调试综合练习")
    print("=" * 50)

    # 练习1：调试一个有 bug 的函数
    print("\n练习1：调试有 bug 的函数")

    def buggy_function(numbers):
        """
        这个函数应该返回列表中所有正数的平均值
        但是有 bug，请使用 print 调试找出问题
        """
        print(f"[DEBUG] 输入: {numbers}")

        positive_numbers = []
        for num in numbers:
            print(f"[DEBUG] 检查 {num}, 是否 > 0: {num > 0}")
            if num > 0:
                positive_numbers.append(num)

        print(f"[DEBUG] 正数列表: {positive_numbers}")

        if not positive_numbers:
            print("[DEBUG] 没有正数，返回 0")
            return 0

        total = sum(positive_numbers)
        count = len(positive_numbers)
        average = total / count

        print(f"[DEBUG] 总和={total}, 数量={count}, 平均值={average}")
        return average

    result = buggy_function([-1, -2, 3, 4, 5])
    print(f"结果: {result}")

    # 练习2：使用调试开关
    print("\n练习2：使用调试开关")

    class Debugger:
        """调试器类"""
        enabled = True

        @classmethod
        def log(cls, message):
            if cls.enabled:
                print(f"[DEBUG] {message}")

        @classmethod
        def enable(cls):
            cls.enabled = True

        @classmethod
        def disable(cls):
            cls.enabled = False

    Debugger.log("调试开启")
    Debugger.disable()
    Debugger.log("这条不会显示")
    Debugger.enable()
    Debugger.log("调试恢复")

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. print 调试是最简单的调试方法
#
# 2. 调试技巧：
#    - 使用标记区分调试信息
#    - 打印变量名和值
#    - 打印类型
#    - 打印函数调用
#    - 打印循环状态
#
# 3. 使用调试开关控制输出
#
# 4. 常见调试场景：
#    - 循环调试
#    - 条件判断调试
#    - 函数返回值调试
#
# 5. 调试完成后记得清理调试代码
#
# 6. 进阶：使用 logging 模块或 IDE 调试功能
