"""
第7章：面向对象编程 - __init__ 和 self
=====================================

本文件学习目标：
1. 深入理解 __init__ 方法
2. 理解 self 的本质
3. 掌握对象初始化的技巧
4. 理解特殊方法的概念
"""

# ============================================================
# 一、__init__ 方法
# ============================================================
#
# __init__ 是 Python 类的初始化方法（构造方法）。
# 当创建对象时，__init__ 会自动被调用。
#
# 作用：
# 1. 初始化对象的属性
# 2. 执行创建对象时需要的操作


print("__init__ 方法:")
print("=" * 50)


class Person:
    """人类 - 演示 __init__"""

    def __init__(self, name, age):
        """
        初始化方法

        参数:
            name: 姓名
            age: 年龄
        """
        print(f"__init__ 被调用，创建 {name}")
        self.name = name
        self.age = age


# 创建对象时，__init__ 自动被调用
print("\n创建对象:")
person1 = Person("张三", 25)
person2 = Person("李四", 30)

print(f"\nperson1: {person1.name}, {person1.age}岁")
print(f"person2: {person2.name}, {person2.age}岁")


# ============================================================
# 二、self 的本质
# ============================================================

print("\n" + "=" * 50)
print("self 的本质:")

# self 代表类的实例本身
# 通过 self，方法可以访问和修改实例的属性


class Dog:
    """狗类 - 演示 self"""

    def __init__(self, name):
        print(f"self 的 id: {id(self)}")
        self.name = name

    def bark(self):
        # self 就是调用这个方法的对象
        print(f"self 的 id: {id(self)}")
        print(f"{self.name} 说: 汪汪汪!")


print("\n创建对象并查看 self:")
dog = Dog("旺财")
print(f"dog 的 id: {id(dog)}")

print("\n调用方法:")
dog.bark()

# self 和 dog 是同一个对象
print(f"\nself 和 dog 是同一个对象: {id(dog) == id(dog)}")


# ============================================================
# 三、__init__ 的参数
# ============================================================

print("\n" + "=" * 50)
print("__init__ 的参数:")


# 带默认参数的 __init__
class Student:
    """学生类 - 带默认参数"""

    def __init__(self, name, age=18, grade="一年级"):
        self.name = name
        self.age = age
        self.grade = grade

    def show(self):
        print(f"{self.name}, {self.age}岁, {self.grade}")


print("\n使用默认参数:")
s1 = Student("小明")
s2 = Student("小红", 20)
s3 = Student("小刚", 19, "二年级")

s1.show()
s2.show()
s3.show()


# 使用 *args 和 **kwargs
class FlexibleClass:
    """灵活的类 - 使用可变参数"""

    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.args = args
        self.kwargs = kwargs

    def show(self):
        print(f"name: {self.name}")
        print(f"args: {self.args}")
        print(f"kwargs: {self.kwargs}")


print("\n使用可变参数:")
obj = FlexibleClass("测试", 1, 2, 3, x=10, y=20)
obj.show()


# ============================================================
# 四、__init__ 中的验证
# ============================================================

print("\n" + "=" * 50)
print("__init__ 中的验证:")


class BankAccount:
    """银行账户 - 带验证"""

    def __init__(self, owner, balance=0):
        # 验证所有者名称
        if not owner or not isinstance(owner, str):
            raise ValueError("所有者名称必须是非空字符串")

        # 验证初始余额
        if not isinstance(balance, (int, float)):
            raise TypeError("余额必须是数字")
        if balance < 0:
            raise ValueError("初始余额不能为负数")

        self.owner = owner
        self.balance = balance
        print(f"账户创建成功: {owner}, 余额: {balance}")


print("\n创建有效账户:")
account1 = BankAccount("张三", 1000)

print("\n尝试创建无效账户:")
try:
    account2 = BankAccount("", 1000)
except ValueError as e:
    print(f"错误: {e}")

try:
    account3 = BankAccount("李四", -100)
except ValueError as e:
    print(f"错误: {e}")


# ============================================================
# 五、特殊方法（魔术方法）
# ============================================================

print("\n" + "=" * 50)
print("特殊方法（魔术方法）:")


class Point:
    """点类 - 演示特殊方法"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """定义 str() 和 print() 的输出"""
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        """定义对象的官方字符串表示"""
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        """定义 == 运算符"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __add__(self, other):
        """定义 + 运算符"""
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        raise TypeError("只能与 Point 相加")

    def __len__(self):
        """定义 len() 函数"""
        # 返回到原点的曼哈顿距离
        return abs(self.x) + abs(self.y)


print("\n使用特殊方法:")
p1 = Point(3, 4)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(f"str(p1): {str(p1)}")
print(f"repr(p1): {repr(p1)}")
print(f"p1 == p2: {p1 == p2}")
print(f"p1 == p3: {p1 == p3}")
print(f"p1 + p2: {p1 + p2}")
print(f"len(p1): {len(p1)}")


# ============================================================
# 六、__new__ vs __init__
# ============================================================

print("\n" + "=" * 50)
print("__new__ vs __init__:")


class MyClass:
    """演示 __new__ 和 __init__ 的区别"""

    def __new__(cls, *args, **kwargs):
        print("1. __new__ 被调用 - 创建实例")
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        print("2. __init__ 被调用 - 初始化实例")
        self.value = value


print("\n创建对象的过程:")
obj = MyClass(10)

# __new__：创建实例（分配内存）
# __init__：初始化实例（设置属性）


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("__init__ 和 self 综合练习")
    print("=" * 50)

    # 练习：创建一个矩形类
    class Rectangle:
        """矩形类"""

        def __init__(self, width, height):
            if width <= 0 or height <= 0:
                raise ValueError("宽度和高度必须大于0")
            self.width = width
            self.height = height

        def __str__(self):
            return f"Rectangle({self.width} x {self.height})"

        def __eq__(self, other):
            if isinstance(other, Rectangle):
                return self.width == other.width and self.height == other.height
            return False

        def area(self):
            """计算面积"""
            return self.width * self.height

        def perimeter(self):
            """计算周长"""
            return 2 * (self.width + self.height)

        def is_square(self):
            """判断是否为正方形"""
            return self.width == self.height

    print("\n创建矩形:")
    rect1 = Rectangle(4, 5)
    rect2 = Rectangle(3, 3)

    print(f"rect1: {rect1}")
    print(f"rect1 面积: {rect1.area()}")
    print(f"rect1 周长: {rect1.perimeter()}")
    print(f"rect1 是正方形: {rect1.is_square()}")

    print(f"\nrect2: {rect2}")
    print(f"rect2 是正方形: {rect2.is_square()}")

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. __init__ 方法：
#    - 初始化方法，创建对象时自动调用
#    - 用于设置对象的初始属性
#    - 可以有默认参数
#    - 可以进行参数验证
#
# 2. self 的本质：
#    - 代表类的实例本身
#    - 方法的第一个参数
#    - 通过 self 访问实例属性和方法
#
# 3. 特殊方法（魔术方法）：
#    - __str__：定义 str() 输出
#    - __repr__：定义官方字符串表示
#    - __eq__：定义 == 运算符
#    - __add__：定义 + 运算符
#    - __len__：定义 len() 函数
#
# 4. __new__ vs __init__：
#    - __new__：创建实例
#    - __init__：初始化实例
