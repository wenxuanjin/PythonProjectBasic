"""
第1章：基础语法 - 数据类型
========================

本文件学习目标：
1. 掌握 Python 的基本数据类型
2. 理解整数（int）和浮点数（float）
3. 掌握字符串（str）的基本用法
4. 理解布尔值（bool）
5. 学会类型转换
"""

# ============================================================
# 一、Python 的基本数据类型
# ============================================================
#
# Python 中最常用的基本数据类型有四种：
#
# 1. int（整数）：如 1, 100, -50
# 2. float（浮点数）：如 3.14, -0.5, 2.0
# 3. str（字符串）：如 "hello", '你好'
# 4. bool（布尔值）：True 或 False
#
# 这四种类型是编程的基础，必须熟练掌握。


# ============================================================
# 二、整数（int）
# ============================================================

# 整数就是没有小数部分的数字
positive_int = 100      # 正整数
negative_int = -50      # 负整数
zero = 0                # 零也是整数

print("正整数:", positive_int)
print("负整数:", negative_int)
print("零:", zero)

# Python 的整数没有大小限制（不像其他语言有 int32、int64 的限制）
big_number = 12345678901234567890
print("大整数:", big_number)

# 整数的基本运算
a = 10
b = 3

print("\n整数运算示例 (a=10, b=3):")
print("加法 a + b =", a + b)      # 13
print("减法 a - b =", a - b)      # 7
print("乘法 a * b =", a * b)      # 30
print("除法 a / b =", a / b)      # 3.333...（结果是浮点数）
print("整除 a // b =", a // b)    # 3（只保留整数部分）
print("取余 a % b =", a % b)      # 1（余数）
print("幂运算 a ** b =", a ** b)  # 1000（10的3次方）


# ============================================================
# 三、浮点数（float）
# ============================================================

# 浮点数就是带小数点的数字
pi = 3.14159
temperature = -5.5
price = 99.99

print("\n浮点数示例:")
print("圆周率:", pi)
print("温度:", temperature)
print("价格:", price)

# 浮点数也可以用科学计数法表示
light_speed = 3e8      # 3 * 10^8 = 300000000
tiny_number = 1.5e-10  # 1.5 * 10^-10

print("光速:", light_speed)
print("极小数:", tiny_number)

# 浮点数运算
x = 1.5
y = 0.5

print("\n浮点数运算示例 (x=1.5, y=0.5):")
print("x + y =", x + y)  # 2.0
print("x - y =", x - y)  # 1.0
print("x * y =", x * y)  # 0.75
print("x / y =", x / y)  # 3.0

# 注意：浮点数运算可能有精度问题
print("\n浮点数精度问题:")
print("0.1 + 0.2 =", 0.1 + 0.2)  # 0.30000000000000004（不是精确的 0.3）
# 这是计算机存储浮点数的方式导致的，不是 Python 的 bug


# ============================================================
# 四、字符串（str）
# ============================================================

# 字符串是由字符组成的文本，用引号包围
# 可以使用单引号或双引号，效果相同

name1 = "张三"      # 双引号
name2 = '李四'      # 单引号
sentence = "Hello, World!"

print("\n字符串示例:")
print(name1)
print(name2)
print(sentence)

# 字符串中包含引号的处理方式
quote1 = "他说：'你好'"      # 外双内单
quote2 = '他说："你好"'      # 外单内双
quote3 = "他说：\"你好\""    # 使用转义字符

print("\n包含引号的字符串:")
print(quote1)
print(quote2)
print(quote3)

# 多行字符串：使用三引号
multi_line = """这是第一行
这是第二行
这是第三行"""

print("\n多行字符串:")
print(multi_line)

# 字符串拼接
first_name = "张"
last_name = "三"
full_name = first_name + last_name  # 使用 + 拼接
print("\n字符串拼接:", full_name)

# 字符串重复
line = "-" * 20  # 重复 20 次
print("重复字符串:", line)

# 字符串长度
text = "Hello, Python!"
print("字符串长度:", len(text))  # 14

# 字符串索引（从 0 开始）
print("\n字符串索引:")
print("第1个字符:", text[0])   # H
print("第2个字符:", text[1])   # e
print("最后一个字符:", text[-1])  # !

# 字符串切片
print("\n字符串切片:")
print("前5个字符:", text[0:5])   # Hello
print("第7到最后:", text[7:])    # Python!
print("倒数5个:", text[-5:])     # thon!


# ============================================================
# 五、布尔值（bool）
# ============================================================

# 布尔值只有两个：True（真）和 False（假）
# 注意：首字母必须大写

is_raining = True
is_sunny = False

print("\n布尔值示例:")
print("正在下雨:", is_raining)
print("阳光明媚:", is_sunny)

# 布尔值常用于条件判断
age = 20
is_adult = age >= 18  # 比较运算的结果是布尔值
print("是否成年:", is_adult)  # True

# 比较运算符
a = 10
b = 5

print("\n比较运算符示例 (a=10, b=5):")
print("a == b (等于):", a == b)      # False
print("a != b (不等于):", a != b)    # True
print("a > b (大于):", a > b)        # True
print("a < b (小于):", a < b)        # False
print("a >= b (大于等于):", a >= b)  # True
print("a <= b (小于等于):", a <= b)  # False

# 逻辑运算符
x = True
y = False

print("\n逻辑运算符示例 (x=True, y=False):")
print("x and y (与):", x and y)  # False（两个都为 True 才是 True）
print("x or y (或):", x or y)    # True（有一个为 True 就是 True）
print("not x (非):", not x)      # False（取反）


# ============================================================
# 六、类型转换
# ============================================================

# 有时需要将一种类型转换为另一种类型

# 转换为整数：int()
print("\n转换为整数:")
print("int('100') =", int("100"))     # 字符串转整数：100
print("int(3.14) =", int(3.14))       # 浮点数转整数：3（截断小数）
print("int(3.99) =", int(3.99))       # 3（不是四舍五入，是截断）
print("int(True) =", int(True))       # 布尔转整数：1
print("int(False) =", int(False))     # 0

# 转换为浮点数：float()
print("\n转换为浮点数:")
print("float('3.14') =", float("3.14"))  # 字符串转浮点数：3.14
print("float(100) =", float(100))        # 整数转浮点数：100.0
print("float('100') =", float("100"))    # 100.0

# 转换为字符串：str()
print("\n转换为字符串:")
print("str(100) =", str(100))        # 整数转字符串："100"
print("str(3.14) =", str(3.14))      # 浮点数转字符串："3.14"
print("str(True) =", str(True))      # 布尔转字符串："True"

# 转换为布尔值：bool()
print("\n转换为布尔值:")
print("bool(1) =", bool(1))          # True（非零数字为 True）
print("bool(0) =", bool(0))          # False（零为 False）
print("bool('hello') =", bool("hello"))  # True（非空字符串为 True）
print("bool('') =", bool(""))        # False（空字符串为 False）
print("bool([1,2]) =", bool([1, 2])) # True（非空列表为 True）
print("bool([]) =", bool([]))        # False（空列表为 False）


# ============================================================
# 七、None 类型
# ============================================================

# None 是 Python 中的特殊值，表示"没有值"或"空"
# 它不是 0，不是空字符串，而是一个独立的类型

result = None
print("\nNone 类型:")
print("result =", result)
print("result 的类型:", type(result))  # <class 'NoneType'>

# None 常用于：
# 1. 函数没有返回值时，默认返回 None
# 2. 表示变量还没有被赋予有意义的值
# 3. 作为函数参数的默认值


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("数据类型综合练习")
    print("=" * 50)

    # 综合示例：商品信息
    product_name = "Python 编程书"  # 字符串
    product_price = 59.9            # 浮点数
    product_stock = 100             # 整数
    is_on_sale = True               # 布尔值

    print(f"商品名称: {product_name}")
    print(f"商品价格: {product_price} 元")
    print(f"库存数量: {product_stock} 件")
    print(f"是否促销: {is_on_sale}")

    # 计算总价值
    total_value = product_price * product_stock
    print(f"库存总价值: {total_value} 元")

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. Python 基本数据类型：
#    - int（整数）：1, 100, -50
#    - float（浮点数）：3.14, -0.5
#    - str（字符串）："hello", '你好'
#    - bool（布尔值）：True, False
#
# 2. 整数运算：+, -, *, /, //, %, **
#
# 3. 字符串操作：
#    - 拼接：+
#    - 重复：*
#    - 长度：len()
#    - 索引：[0], [-1]
#    - 切片：[0:5]
#
# 4. 布尔运算：and, or, not
#
# 5. 类型转换：int(), float(), str(), bool()
#
# 6. None 表示"没有值"
