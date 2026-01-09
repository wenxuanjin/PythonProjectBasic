"""
第5章：模块与文件 - 模块导入
==========================

本文件学习目标：
1. 理解模块的概念
2. 掌握 import 的各种用法
3. 学会使用标准库模块
4. 理解模块搜索路径
"""

# ============================================================
# 一、什么是模块？
# ============================================================
#
# 模块（Module）是一个包含 Python 代码的文件（.py 文件）。
#
# 模块的作用：
# 1. 代码组织：将相关功能放在一起
# 2. 代码复用：在多个程序中使用同一模块
# 3. 命名空间：避免命名冲突
#
# Python 模块分类：
# 1. 标准库模块：Python 自带的模块（如 math、os、sys）
# 2. 第三方模块：需要安装的模块（如 requests、numpy）
# 3. 自定义模块：自己编写的模块


# ============================================================
# 二、import 语句
# ============================================================

# 方式1：导入整个模块
import math

print("导入整个模块:")
print(f"math.pi = {math.pi}")
print(f"math.sqrt(16) = {math.sqrt(16)}")
print(f"math.ceil(3.2) = {math.ceil(3.2)}")
print(f"math.floor(3.8) = {math.floor(3.8)}")


# 方式2：导入模块并起别名
import math as m

print("\n导入模块并起别名:")
print(f"m.pi = {m.pi}")
print(f"m.sin(m.pi/2) = {m.sin(m.pi/2)}")


# 方式3：从模块导入特定内容
from math import pi, sqrt, pow

print("\n从模块导入特定内容:")
print(f"pi = {pi}")
print(f"sqrt(25) = {sqrt(25)}")
print(f"pow(2, 10) = {pow(2, 10)}")


# 方式4：从模块导入特定内容并起别名
from math import factorial as fact

print("\n导入并起别名:")
print(f"fact(5) = {fact(5)}")


# 方式5：导入模块的所有内容（不推荐）
# from math import *
# 不推荐原因：
# 1. 可能导致命名冲突
# 2. 不清楚导入了什么
# 3. 代码可读性差


# ============================================================
# 三、常用标准库模块
# ============================================================

print("\n" + "=" * 50)
print("常用标准库模块:")

# 1. os 模块：操作系统相关
import os

print("\n1. os 模块:")
print(f"当前工作目录: {os.getcwd()}")
print(f"目录分隔符: {os.sep}")
print(f"环境变量 PATH 的前100字符: {os.environ.get('PATH', '')[:100]}...")

# 2. sys 模块：Python 解释器相关
import sys

print("\n2. sys 模块:")
print(f"Python 版本: {sys.version}")
print(f"平台: {sys.platform}")
print(f"模块搜索路径（前3个）: {sys.path[:3]}")

# 3. datetime 模块：日期时间
from datetime import datetime, date, timedelta

print("\n3. datetime 模块:")
now = datetime.now()
print(f"当前时间: {now}")
print(f"格式化: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"今天: {date.today()}")
print(f"明天: {date.today() + timedelta(days=1)}")

# 4. random 模块：随机数
import random

print("\n4. random 模块:")
print(f"随机整数 (1-10): {random.randint(1, 10)}")
print(f"随机浮点数 (0-1): {random.random():.4f}")
print(f"随机选择: {random.choice(['苹果', '香蕉', '橙子'])}")
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"打乱列表: {numbers}")

# 5. json 模块：JSON 处理
import json

print("\n5. json 模块:")
data = {"name": "张三", "age": 25, "city": "北京"}
json_str = json.dumps(data, ensure_ascii=False)
print(f"Python -> JSON: {json_str}")
parsed = json.loads(json_str)
print(f"JSON -> Python: {parsed}")

# 6. re 模块：正则表达式
import re

print("\n6. re 模块:")
text = "我的邮箱是 test@example.com，电话是 13812345678"
email = re.search(r'\w+@\w+\.\w+', text)
phone = re.search(r'1\d{10}', text)
print(f"文本: {text}")
print(f"找到邮箱: {email.group() if email else '未找到'}")
print(f"找到电话: {phone.group() if phone else '未找到'}")


# ============================================================
# 四、模块搜索路径
# ============================================================

print("\n" + "=" * 50)
print("模块搜索路径:")

# Python 按以下顺序搜索模块：
# 1. 当前目录
# 2. PYTHONPATH 环境变量指定的目录
# 3. Python 安装目录的标准库
# 4. 第三方包目录（site-packages）

print("\n模块搜索路径 (sys.path):")
for i, path in enumerate(sys.path[:5]):
    print(f"  {i}: {path}")
print("  ...")


# ============================================================
# 五、查看模块内容
# ============================================================

print("\n" + "=" * 50)
print("查看模块内容:")

# 使用 dir() 查看模块的所有属性和方法
print("\nmath 模块的内容（部分）:")
math_contents = [item for item in dir(math) if not item.startswith('_')]
print(math_contents[:10])

# 使用 help() 查看帮助文档
# help(math.sqrt)  # 取消注释可以查看

# 查看模块文件位置
print(f"\nmath 模块位置: {math.__file__}")


# ============================================================
# 六、__name__ 变量
# ============================================================

print("\n" + "=" * 50)
print("__name__ 变量:")

# 每个模块都有一个 __name__ 变量
# 当模块被直接运行时，__name__ == "__main__"
# 当模块被导入时，__name__ == 模块名

print(f"当前模块的 __name__: {__name__}")
print(f"math 模块的 __name__: {math.__name__}")


# ============================================================
# 七、包（Package）
# ============================================================

print("\n" + "=" * 50)
print("包（Package）:")

# 包是包含多个模块的目录
# 包目录下必须有 __init__.py 文件（Python 3.3+ 可以没有）

# 包的结构示例：
# my_package/
#     __init__.py
#     module1.py
#     module2.py
#     subpackage/
#         __init__.py
#         module3.py

# 导入包中的模块：
# import my_package.module1
# from my_package import module1
# from my_package.module1 import some_function

print("包是包含多个模块的目录")
print("包目录下通常有 __init__.py 文件")


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("模块导入综合练习")
    print("=" * 50)

    # 练习1：使用 datetime 计算年龄
    print("\n计算年龄:")
    from datetime import date

    def calculate_age(birth_year, birth_month, birth_day):
        """计算年龄"""
        today = date.today()
        birth_date = date(birth_year, birth_month, birth_day)
        age = today.year - birth_date.year
        # 如果今年的生日还没到，年龄减1
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age

    age = calculate_age(2000, 6, 15)
    print(f"2000年6月15日出生的人今年 {age} 岁")

    # 练习2：使用 random 生成随机密码
    print("\n生成随机密码:")
    import string

    def generate_password(length=12):
        """生成随机密码"""
        characters = string.ascii_letters + string.digits + "!@#$%"
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    for i in range(3):
        print(f"  密码 {i+1}: {generate_password()}")

    # 练习3：使用 os 列出目录内容
    print("\n列出当前目录内容:")
    current_dir = os.getcwd()
    items = os.listdir(current_dir)
    print(f"当前目录: {current_dir}")
    print(f"文件数量: {len(items)}")
    print(f"前5个文件: {items[:5]}")

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. 模块是包含 Python 代码的 .py 文件
#
# 2. import 的用法：
#    - import module
#    - import module as alias
#    - from module import name
#    - from module import name as alias
#
# 3. 常用标准库：
#    - os：操作系统
#    - sys：Python 解释器
#    - datetime：日期时间
#    - random：随机数
#    - json：JSON 处理
#    - re：正则表达式
#
# 4. 模块搜索路径：sys.path
#
# 5. 查看模块内容：dir()、help()
#
# 6. __name__ 变量：
#    - 直接运行：__name__ == "__main__"
#    - 被导入：__name__ == 模块名
#
# 7. 包是包含多个模块的目录
