"""
第6章：异常与调试 - try-except 语句
=================================

本文件学习目标：
1. 掌握 try-except 的基本用法
2. 学会捕获特定类型的异常
3. 理解 else 和 finally 子句
4. 学会自定义异常
"""

# ============================================================
# 一、try-except 基本语法
# ============================================================

print("try-except 基本语法:")
print("=" * 50)

# 基本结构
# try:
#     可能出错的代码
# except:
#     出错时执行的代码

# 示例1：捕获所有异常
print("\n示例1：捕获所有异常")
try:
    result = 10 / 0
except:
    print("发生了错误！")

# 示例2：捕获特定异常
print("\n示例2：捕获特定异常")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("除数不能为零！")


# ============================================================
# 二、捕获异常信息
# ============================================================

print("\n" + "=" * 50)
print("捕获异常信息:")

# 使用 as 获取异常对象
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"异常类型: {type(e).__name__}")
    print(f"异常消息: {e}")

# 获取更详细的信息
import traceback

print("\n获取详细的异常信息:")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("异常堆栈:")
    traceback.print_exc()


# ============================================================
# 三、捕获多种异常
# ============================================================

print("\n" + "=" * 50)
print("捕获多种异常:")

# 方式1：多个 except 子句
print("\n方式1：多个 except 子句")


def safe_divide(a, b):
    """安全的除法"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("错误：除数不能为零")
        return None
    except TypeError:
        print("错误：参数类型不正确")
        return None


print(f"safe_divide(10, 2) = {safe_divide(10, 2)}")
print(f"safe_divide(10, 0) = {safe_divide(10, 0)}")
print(f"safe_divide(10, 'a') = {safe_divide(10, 'a')}")

# 方式2：一个 except 捕获多种异常
print("\n方式2：一个 except 捕获多种异常")


def safe_divide_v2(a, b):
    """安全的除法（简化版）"""
    try:
        return a / b
    except (ZeroDivisionError, TypeError) as e:
        print(f"错误：{e}")
        return None


print(f"safe_divide_v2(10, 0) = {safe_divide_v2(10, 0)}")


# ============================================================
# 四、else 子句
# ============================================================

print("\n" + "=" * 50)
print("else 子句:")

# else 子句在没有异常时执行
# try:
#     可能出错的代码
# except:
#     出错时执行
# else:
#     没有出错时执行


def divide_with_else(a, b):
    """带 else 的除法"""
    try:
        result = a / b
    except ZeroDivisionError:
        print("错误：除数不能为零")
        return None
    else:
        print("计算成功！")
        return result


print("\n正常情况:")
print(f"结果: {divide_with_else(10, 2)}")

print("\n异常情况:")
print(f"结果: {divide_with_else(10, 0)}")


# ============================================================
# 五、finally 子句
# ============================================================

print("\n" + "=" * 50)
print("finally 子句:")

# finally 子句无论是否发生异常都会执行
# 常用于清理资源（关闭文件、释放连接等）


def divide_with_finally(a, b):
    """带 finally 的除法"""
    try:
        print("开始计算...")
        result = a / b
        return result
    except ZeroDivisionError:
        print("错误：除数不能为零")
        return None
    finally:
        print("计算结束（finally 总是执行）")


print("\n正常情况:")
print(f"结果: {divide_with_finally(10, 2)}")

print("\n异常情况:")
print(f"结果: {divide_with_finally(10, 0)}")


# 完整的 try-except-else-finally
print("\n完整结构:")


def complete_example(a, b):
    """完整的异常处理示例"""
    try:
        result = a / b
    except ZeroDivisionError:
        print("except: 捕获到除零错误")
        result = None
    else:
        print("else: 没有发生异常")
    finally:
        print("finally: 无论如何都执行")
    return result


print("\n正常情况:")
complete_example(10, 2)

print("\n异常情况:")
complete_example(10, 0)


# ============================================================
# 六、重新抛出异常
# ============================================================

print("\n" + "=" * 50)
print("重新抛出异常:")


def process_data(data):
    """处理数据，记录日志后重新抛出异常"""
    try:
        result = int(data)
        return result
    except ValueError as e:
        print(f"日志：处理数据 '{data}' 时发生错误")
        raise  # 重新抛出当前异常


# 测试
try:
    process_data("abc")
except ValueError as e:
    print(f"外层捕获到异常: {e}")


# ============================================================
# 七、自定义异常
# ============================================================

print("\n" + "=" * 50)
print("自定义异常:")


# 自定义异常类
class ValidationError(Exception):
    """验证错误"""
    pass


class AgeError(ValidationError):
    """年龄错误"""
    def __init__(self, age, message="年龄无效"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.age}"


def validate_age(age):
    """验证年龄"""
    if not isinstance(age, int):
        raise TypeError("年龄必须是整数")
    if age < 0:
        raise AgeError(age, "年龄不能为负数")
    if age > 150:
        raise AgeError(age, "年龄不能超过150")
    return age


# 测试自定义异常
print("\n测试自定义异常:")
test_ages = [25, -5, 200, "abc"]

for age in test_ages:
    try:
        result = validate_age(age)
        print(f"年龄 {age} 验证通过")
    except AgeError as e:
        print(f"AgeError: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")


# ============================================================
# 八、异常处理最佳实践
# ============================================================

print("\n" + "=" * 50)
print("异常处理最佳实践:")

print("""
1. 只捕获你能处理的异常
   - 不要使用空的 except:
   - 至少使用 except Exception:

2. 异常信息要有意义
   - 提供足够的上下文信息
   - 便于调试和排错

3. 不要用异常控制流程
   - 异常应该用于异常情况
   - 正常逻辑用条件判断

4. 及时清理资源
   - 使用 finally 或 with 语句
   - 确保文件、连接等被正确关闭

5. 记录异常日志
   - 在生产环境中记录异常
   - 便于问题追踪
""")


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("try-except 综合练习")
    print("=" * 50)

    # 练习1：安全的列表访问
    print("\n练习1：安全的列表访问")

    def safe_get(lst, index, default=None):
        """安全地获取列表元素"""
        try:
            return lst[index]
        except IndexError:
            return default
        except TypeError:
            return default

    my_list = [1, 2, 3]
    print(f"safe_get([1,2,3], 1) = {safe_get(my_list, 1)}")
    print(f"safe_get([1,2,3], 10) = {safe_get(my_list, 10)}")
    print(f"safe_get([1,2,3], 10, '默认值') = {safe_get(my_list, 10, '默认值')}")

    # 练习2：安全的字典访问
    print("\n练习2：安全的类型转换")

    def safe_int(value, default=0):
        """安全地转换为整数"""
        try:
            return int(value)
        except (ValueError, TypeError):
            return default

    print(f"safe_int('123') = {safe_int('123')}")
    print(f"safe_int('abc') = {safe_int('abc')}")
    print(f"safe_int(None) = {safe_int(None)}")

    # 练习3：文件操作异常处理
    print("\n练习3：文件操作异常处理")

    def read_file_safe(filename):
        """安全地读取文件"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"文件不存在: {filename}")
            return None
        except PermissionError:
            print(f"没有权限读取: {filename}")
            return None
        except Exception as e:
            print(f"读取文件时发生错误: {e}")
            return None

    result = read_file_safe("不存在的文件.txt")
    print(f"结果: {result}")

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. try-except 基本语法：
#    try:
#        可能出错的代码
#    except 异常类型 as e:
#        处理异常
#
# 2. 捕获多种异常：
#    - 多个 except 子句
#    - except (Type1, Type2)
#
# 3. else 子句：没有异常时执行
#
# 4. finally 子句：无论如何都执行
#
# 5. 重新抛出异常：raise
#
# 6. 自定义异常：继承 Exception 类
#
# 7. 最佳实践：
#    - 只捕获能处理的异常
#    - 提供有意义的错误信息
#    - 及时清理资源
