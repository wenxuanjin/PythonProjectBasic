"""
第4章：函数 - 参数与返回值
========================

本文件学习目标：
1. 掌握位置参数和关键字参数
2. 理解默认参数的用法
3. 掌握可变参数 *args 和 **kwargs
4. 理解参数的传递方式
"""

# ============================================================
# 一、位置参数
# ============================================================

# 位置参数：按照位置顺序传递的参数

def greet(name, greeting):
    """
    打招呼

    参数:
        name: 名字
        greeting: 问候语
    """
    print(f"{greeting}, {name}!")


print("位置参数:")
greet("张三", "你好")  # 按位置传递
greet("李四", "早上好")


# ============================================================
# 二、关键字参数
# ============================================================

# 关键字参数：通过参数名传递的参数

print("\n关键字参数:")
greet(name="王五", greeting="下午好")  # 使用参数名
greet(greeting="晚上好", name="赵六")  # 顺序可以不同

# 混合使用：位置参数必须在关键字参数之前
greet("小明", greeting="嗨")


# ============================================================
# 三、默认参数
# ============================================================

# 默认参数：定义时指定默认值，调用时可以省略

def greet_with_default(name, greeting="你好"):
    """
    打招呼（带默认问候语）

    参数:
        name: 名字
        greeting: 问候语，默认为"你好"
    """
    print(f"{greeting}, {name}!")


print("\n默认参数:")
greet_with_default("张三")  # 使用默认值
greet_with_default("李四", "早安")  # 覆盖默认值


# 多个默认参数
def create_user(name, age=18, city="北京"):
    """创建用户信息"""
    return {"name": name, "age": age, "city": city}


print("\n多个默认参数:")
print(create_user("张三"))
print(create_user("李四", 25))
print(create_user("王五", 30, "上海"))
print(create_user("赵六", city="广州"))  # 跳过 age


# 注意：默认参数必须放在非默认参数后面
# def wrong_func(a=1, b):  # SyntaxError
#     pass


# ============================================================
# 四、默认参数的陷阱
# ============================================================

print("\n默认参数的陷阱:")


# 错误示例：使用可变对象作为默认值
def append_to_list_wrong(item, my_list=[]):
    """错误的写法：默认列表会被共享"""
    my_list.append(item)
    return my_list


print("错误写法的结果:")
print(append_to_list_wrong(1))  # [1]
print(append_to_list_wrong(2))  # [1, 2] - 不是 [2]！
print(append_to_list_wrong(3))  # [1, 2, 3] - 不是 [3]！


# 正确示例：使用 None 作为默认值
def append_to_list_correct(item, my_list=None):
    """正确的写法：使用 None 作为默认值"""
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list


print("\n正确写法的结果:")
print(append_to_list_correct(1))  # [1]
print(append_to_list_correct(2))  # [2]
print(append_to_list_correct(3))  # [3]


# ============================================================
# 五、可变参数 *args
# ============================================================

# *args：接收任意数量的位置参数，打包成元组

def sum_all(*args):
    """
    计算所有参数的和

    参数:
        *args: 任意数量的数字
    """
    print(f"args 的类型: {type(args)}")
    print(f"args 的值: {args}")
    return sum(args)


print("\n可变参数 *args:")
print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")


# 混合使用普通参数和 *args
def greet_all(greeting, *names):
    """向多个人打招呼"""
    for name in names:
        print(f"{greeting}, {name}!")


print("\n混合使用:")
greet_all("你好", "张三", "李四", "王五")


# ============================================================
# 六、可变参数 **kwargs
# ============================================================

# **kwargs：接收任意数量的关键字参数，打包成字典

def print_info(**kwargs):
    """
    打印所有信息

    参数:
        **kwargs: 任意数量的关键字参数
    """
    print(f"kwargs 的类型: {type(kwargs)}")
    print(f"kwargs 的值: {kwargs}")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


print("\n可变参数 **kwargs:")
print_info(name="张三", age=25, city="北京")


# 混合使用
def create_profile(name, **kwargs):
    """创建用户档案"""
    profile = {"name": name}
    profile.update(kwargs)
    return profile


print("\n混合使用:")
print(create_profile("张三", age=25, city="北京", job="工程师"))


# ============================================================
# 七、参数的完整顺序
# ============================================================

# 参数顺序：位置参数 -> 默认参数 -> *args -> **kwargs

def full_example(a, b, c=3, *args, **kwargs):
    """
    展示完整的参数顺序

    参数:
        a: 位置参数
        b: 位置参数
        c: 默认参数
        *args: 可变位置参数
        **kwargs: 可变关键字参数
    """
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")


print("\n完整参数顺序:")
full_example(1, 2, 3, 4, 5, 6, x=10, y=20)


# ============================================================
# 八、参数解包
# ============================================================

print("\n参数解包:")


def add_three(a, b, c):
    """三个数相加"""
    return a + b + c


# 使用 * 解包列表/元组
numbers = [1, 2, 3]
print(f"列表解包: add_three(*{numbers}) = {add_three(*numbers)}")

# 使用 ** 解包字典
params = {"a": 10, "b": 20, "c": 30}
print(f"字典解包: add_three(**{params}) = {add_three(**params)}")


# ============================================================
# 九、仅限关键字参数
# ============================================================

# 在 * 后面的参数必须使用关键字传递

def keyword_only(a, b, *, c, d):
    """
    c 和 d 必须使用关键字传递
    """
    print(f"a={a}, b={b}, c={c}, d={d}")


print("\n仅限关键字参数:")
keyword_only(1, 2, c=3, d=4)
# keyword_only(1, 2, 3, 4)  # TypeError


# 使用 *args 后的参数也是仅限关键字
def mixed_keyword(*args, option=False):
    """option 必须使用关键字传递"""
    print(f"args={args}, option={option}")


mixed_keyword(1, 2, 3, option=True)


# ============================================================
# 十、参数传递方式
# ============================================================

print("\n参数传递方式:")


# Python 的参数传递是"传对象引用"
# 对于不可变对象（数字、字符串、元组），函数内修改不影响外部
# 对于可变对象（列表、字典），函数内修改会影响外部

def modify_immutable(x):
    """尝试修改不可变对象"""
    print(f"  函数内修改前: x = {x}")
    x = x + 10
    print(f"  函数内修改后: x = {x}")


def modify_mutable(lst):
    """修改可变对象"""
    print(f"  函数内修改前: lst = {lst}")
    lst.append(100)
    print(f"  函数内修改后: lst = {lst}")


# 不可变对象
print("不可变对象（数字）:")
num = 5
print(f"调用前: num = {num}")
modify_immutable(num)
print(f"调用后: num = {num}")  # 没有改变

# 可变对象
print("\n可变对象（列表）:")
my_list = [1, 2, 3]
print(f"调用前: my_list = {my_list}")
modify_mutable(my_list)
print(f"调用后: my_list = {my_list}")  # 被修改了


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("参数与返回值综合练习")
    print("=" * 50)

    # 练习1：计算平均值（可变参数）
    def average(*args):
        """计算平均值"""
        if not args:
            return 0
        return sum(args) / len(args)

    print("\n计算平均值:")
    print(f"average(1, 2, 3) = {average(1, 2, 3)}")
    print(f"average(10, 20, 30, 40, 50) = {average(10, 20, 30, 40, 50)}")

    # 练习2：格式化输出（关键字参数）
    def format_output(template, **kwargs):
        """使用关键字参数格式化字符串"""
        return template.format(**kwargs)

    print("\n格式化输出:")
    template = "姓名: {name}, 年龄: {age}, 城市: {city}"
    result = format_output(template, name="张三", age=25, city="北京")
    print(result)

    # 练习3：创建 HTML 标签（混合参数）
    def create_tag(tag_name, content="", **attributes):
        """
        创建 HTML 标签

        参数:
            tag_name: 标签名
            content: 标签内容
            **attributes: 标签属性
        """
        attrs = " ".join(f'{k}="{v}"' for k, v in attributes.items())
        if attrs:
            return f"<{tag_name} {attrs}>{content}</{tag_name}>"
        return f"<{tag_name}>{content}</{tag_name}>"

    print("\n创建 HTML 标签:")
    print(create_tag("p", "Hello, World!"))
    print(create_tag("a", "点击这里", href="https://example.com"))
    print(create_tag("div", "内容", id="main", style="color: red"))

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. 位置参数：按顺序传递
#
# 2. 关键字参数：通过参数名传递
#
# 3. 默认参数：
#    - 定义时指定默认值
#    - 必须放在非默认参数后面
#    - 不要使用可变对象作为默认值
#
# 4. 可变参数：
#    - *args：接收任意位置参数，打包成元组
#    - **kwargs：接收任意关键字参数，打包成字典
#
# 5. 参数顺序：位置参数 -> 默认参数 -> *args -> **kwargs
#
# 6. 参数解包：
#    - * 解包列表/元组
#    - ** 解包字典
#
# 7. 仅限关键字参数：* 后面的参数
#
# 8. 参数传递：
#    - 不可变对象：函数内修改不影响外部
#    - 可变对象：函数内修改会影响外部
