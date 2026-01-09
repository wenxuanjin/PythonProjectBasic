"""
第7章：面向对象编程 - 多态
========================

本文件学习目标：
1. 理解多态的概念
2. 掌握多态的实现方式
3. 理解鸭子类型
4. 学会使用抽象基类
"""

# ============================================================
# 一、什么是多态？
# ============================================================
#
# 多态（Polymorphism）是指同一个方法在不同对象上有不同的行为。
#
# 通俗解释：
# - 同样是"说话"这个动作
# - 狗会"汪汪汪"
# - 猫会"喵喵喵"
# - 鸟会"叽叽喳喳"
#
# 多态的好处：
# 1. 代码更灵活
# 2. 可以统一处理不同类型的对象
# 3. 便于扩展


# ============================================================
# 二、多态的基本示例
# ============================================================

print("多态的基本示例:")
print("=" * 50)


class Animal:
    """动物基类"""

    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    """狗"""

    def speak(self):
        return f"{self.name} 说: 汪汪汪!"


class Cat(Animal):
    """猫"""

    def speak(self):
        return f"{self.name} 说: 喵喵喵!"


class Duck(Animal):
    """鸭子"""

    def speak(self):
        return f"{self.name} 说: 嘎嘎嘎!"


class Cow(Animal):
    """牛"""

    def speak(self):
        return f"{self.name} 说: 哞哞哞!"


# 多态的体现：同一个函数处理不同类型的对象
def animal_speak(animal):
    """让动物说话 - 多态函数"""
    print(animal.speak())


print("\n让不同的动物说话:")
animals = [
    Dog("旺财"),
    Cat("咪咪"),
    Duck("唐老鸭"),
    Cow("大壮")
]

for animal in animals:
    animal_speak(animal)


# ============================================================
# 三、鸭子类型
# ============================================================

print("\n" + "=" * 50)
print("鸭子类型:")

# Python 使用"鸭子类型"（Duck Typing）
# "如果它走起来像鸭子，叫起来像鸭子，那它就是鸭子"
# 不关心对象的类型，只关心对象是否有需要的方法


class Robot:
    """机器人 - 不继承 Animal，但有 speak 方法"""

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} 说: 我是机器人!"


class Parrot:
    """鹦鹉 - 不继承 Animal，但有 speak 方法"""

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} 说: 你好你好!"


print("\n鸭子类型演示:")
# Robot 和 Parrot 不继承 Animal，但也可以使用 animal_speak
speakers = [
    Dog("小狗"),
    Robot("机器人"),
    Parrot("鹦鹉")
]

for speaker in speakers:
    animal_speak(speaker)  # 只要有 speak 方法就可以


# ============================================================
# 四、多态的实际应用
# ============================================================

print("\n" + "=" * 50)
print("多态的实际应用:")


# 示例：支付系统
class Payment:
    """支付基类"""

    def pay(self, amount):
        raise NotImplementedError("子类必须实现 pay 方法")


class CreditCard(Payment):
    """信用卡支付"""

    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"使用信用卡 {self.card_number[-4:]} 支付 {amount} 元")
        return True


class Alipay(Payment):
    """支付宝支付"""

    def __init__(self, account):
        self.account = account

    def pay(self, amount):
        print(f"使用支付宝账户 {self.account} 支付 {amount} 元")
        return True


class WechatPay(Payment):
    """微信支付"""

    def __init__(self, account):
        self.account = account

    def pay(self, amount):
        print(f"使用微信账户 {self.account} 支付 {amount} 元")
        return True


def process_payment(payment_method, amount):
    """处理支付 - 多态函数"""
    print(f"\n处理 {amount} 元的支付...")
    if payment_method.pay(amount):
        print("支付成功！")
    else:
        print("支付失败！")


print("\n支付系统演示:")
credit_card = CreditCard("1234567890123456")
alipay = Alipay("user@example.com")
wechat = WechatPay("user123")

process_payment(credit_card, 100)
process_payment(alipay, 200)
process_payment(wechat, 300)


# ============================================================
# 五、抽象基类
# ============================================================

print("\n" + "=" * 50)
print("抽象基类:")

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    图形抽象基类

    使用 ABC 和 @abstractmethod 定义抽象类和抽象方法
    抽象类不能被实例化
    子类必须实现所有抽象方法
    """

    @abstractmethod
    def area(self):
        """计算面积 - 抽象方法"""
        pass

    @abstractmethod
    def perimeter(self):
        """计算周长 - 抽象方法"""
        pass

    def describe(self):
        """描述图形 - 普通方法"""
        print(f"面积: {self.area():.2f}, 周长: {self.perimeter():.2f}")


class Rectangle(Shape):
    """矩形"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    """圆形"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius


print("\n抽象基类演示:")

# 不能实例化抽象类
# shape = Shape()  # TypeError

# 可以实例化具体子类
rect = Rectangle(4, 5)
circle = Circle(3)

print("矩形:")
rect.describe()

print("\n圆形:")
circle.describe()


# ============================================================
# 六、多态与类型检查
# ============================================================

print("\n" + "=" * 50)
print("多态与类型检查:")


def process_shapes(shapes):
    """处理图形列表"""
    total_area = 0
    for shape in shapes:
        # 使用 isinstance 进行类型检查
        if isinstance(shape, Shape):
            total_area += shape.area()
            shape.describe()
        else:
            print(f"警告: {shape} 不是 Shape 类型")
    return total_area


shapes = [Rectangle(3, 4), Circle(2), Rectangle(5, 6)]
total = process_shapes(shapes)
print(f"\n总面积: {total:.2f}")


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("多态综合练习")
    print("=" * 50)

    # 练习：创建一个文件处理系统
    class FileHandler(ABC):
        """文件处理器抽象基类"""

        @abstractmethod
        def read(self, filename):
            """读取文件"""
            pass

        @abstractmethod
        def write(self, filename, content):
            """写入文件"""
            pass

    class TextFileHandler(FileHandler):
        """文本文件处理器"""

        def read(self, filename):
            print(f"读取文本文件: {filename}")
            return f"文本文件 {filename} 的内容"

        def write(self, filename, content):
            print(f"写入文本文件: {filename}")
            print(f"内容: {content}")

    class JSONFileHandler(FileHandler):
        """JSON 文件处理器"""

        def read(self, filename):
            print(f"读取 JSON 文件: {filename}")
            return {"file": filename, "type": "json"}

        def write(self, filename, content):
            print(f"写入 JSON 文件: {filename}")
            print(f"内容: {content}")

    class CSVFileHandler(FileHandler):
        """CSV 文件处理器"""

        def read(self, filename):
            print(f"读取 CSV 文件: {filename}")
            return [["col1", "col2"], ["data1", "data2"]]

        def write(self, filename, content):
            print(f"写入 CSV 文件: {filename}")
            print(f"内容: {content}")

    def process_file(handler, filename, content=None):
        """统一的文件处理函数"""
        if content:
            handler.write(filename, content)
        else:
            return handler.read(filename)

    print("\n文件处理系统演示:")
    handlers = [
        TextFileHandler(),
        JSONFileHandler(),
        CSVFileHandler()
    ]

    filenames = ["data.txt", "config.json", "report.csv"]

    for handler, filename in zip(handlers, filenames):
        print(f"\n处理 {filename}:")
        result = process_file(handler, filename)
        print(f"结果: {result}")

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. 多态：同一方法在不同对象上有不同行为
#
# 2. 多态的实现：
#    - 继承 + 方法重写
#    - 鸭子类型
#
# 3. 鸭子类型：
#    - 不关心对象类型，只关心是否有需要的方法
#    - Python 的动态特性
#
# 4. 抽象基类：
#    - from abc import ABC, abstractmethod
#    - 定义接口规范
#    - 子类必须实现抽象方法
#
# 5. 多态的好处：
#    - 代码更灵活
#    - 统一处理不同类型
#    - 便于扩展
