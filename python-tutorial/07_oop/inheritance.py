"""
第7章：面向对象编程 - 继承
========================

本文件学习目标：
1. 理解继承的概念
2. 学会定义子类
3. 掌握方法重写
4. 理解 super() 的用法
"""

# ============================================================
# 一、什么是继承？
# ============================================================
#
# 继承是面向对象编程的重要特性。
# 子类可以继承父类的属性和方法，并可以添加新的或修改已有的。
#
# 继承的好处：
# 1. 代码复用：避免重复编写相同的代码
# 2. 扩展性：可以在父类基础上添加新功能
# 3. 层次结构：建立类之间的关系
#
# 术语：
# - 父类（基类、超类）：被继承的类
# - 子类（派生类）：继承的类


# ============================================================
# 二、基本继承
# ============================================================

print("基本继承:")
print("=" * 50)


# 父类
class Animal:
    """动物类 - 父类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} 正在吃东西")

    def sleep(self):
        print(f"{self.name} 正在睡觉")

    def introduce(self):
        print(f"我是 {self.name}，今年 {self.age} 岁")


# 子类
class Dog(Animal):
    """狗类 - 继承自 Animal"""

    def bark(self):
        print(f"{self.name} 说: 汪汪汪!")


class Cat(Animal):
    """猫类 - 继承自 Animal"""

    def meow(self):
        print(f"{self.name} 说: 喵喵喵!")


# 使用子类
print("\n创建子类对象:")
dog = Dog("旺财", 3)
cat = Cat("咪咪", 2)

# 子类可以使用父类的方法
print("\n使用继承的方法:")
dog.introduce()
dog.eat()
dog.bark()  # 子类特有的方法

print()
cat.introduce()
cat.sleep()
cat.meow()  # 子类特有的方法


# ============================================================
# 三、方法重写
# ============================================================

print("\n" + "=" * 50)
print("方法重写:")


class Animal:
    """动物类"""

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} 发出声音")

    def move(self):
        print(f"{self.name} 在移动")


class Dog(Animal):
    """狗类 - 重写 speak 方法"""

    def speak(self):
        # 重写父类的方法
        print(f"{self.name} 说: 汪汪汪!")


class Cat(Animal):
    """猫类 - 重写 speak 方法"""

    def speak(self):
        print(f"{self.name} 说: 喵喵喵!")


class Bird(Animal):
    """鸟类 - 重写 speak 和 move 方法"""

    def speak(self):
        print(f"{self.name} 说: 叽叽喳喳!")

    def move(self):
        print(f"{self.name} 在飞翔")


print("\n方法重写演示:")
animals = [Dog("旺财"), Cat("咪咪"), Bird("小鸟")]

for animal in animals:
    animal.speak()
    animal.move()
    print()


# ============================================================
# 四、super() 函数
# ============================================================

print("=" * 50)
print("super() 函数:")


class Person:
    """人类 - 父类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"我叫 {self.name}，今年 {self.age} 岁")


class Student(Person):
    """学生类 - 使用 super()"""

    def __init__(self, name, age, student_id, grade):
        # 调用父类的 __init__
        super().__init__(name, age)
        # 添加子类特有的属性
        self.student_id = student_id
        self.grade = grade

    def introduce(self):
        # 调用父类的方法
        super().introduce()
        # 添加额外信息
        print(f"学号: {self.student_id}，年级: {self.grade}")


class Teacher(Person):
    """教师类 - 使用 super()"""

    def __init__(self, name, age, subject, years):
        super().__init__(name, age)
        self.subject = subject
        self.years = years

    def introduce(self):
        super().introduce()
        print(f"教授: {self.subject}，教龄: {self.years} 年")


print("\n使用 super():")
student = Student("小明", 18, "2024001", "高三")
teacher = Teacher("张老师", 35, "数学", 10)

print("学生介绍:")
student.introduce()

print("\n教师介绍:")
teacher.introduce()


# ============================================================
# 五、多层继承
# ============================================================

print("\n" + "=" * 50)
print("多层继承:")


class Animal:
    """动物 - 第一层"""

    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} 在呼吸")


class Mammal(Animal):
    """哺乳动物 - 第二层"""

    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def feed_milk(self):
        print(f"{self.name} 在哺乳")


class Dog(Mammal):
    """狗 - 第三层"""

    def __init__(self, name, fur_color, breed):
        super().__init__(name, fur_color)
        self.breed = breed

    def bark(self):
        print(f"{self.name} 说: 汪汪汪!")


print("\n多层继承演示:")
dog = Dog("旺财", "黄色", "金毛")
print(f"名字: {dog.name}")
print(f"毛色: {dog.fur_color}")
print(f"品种: {dog.breed}")
dog.breathe()  # 来自 Animal
dog.feed_milk()  # 来自 Mammal
dog.bark()  # 来自 Dog


# ============================================================
# 六、检查继承关系
# ============================================================

print("\n" + "=" * 50)
print("检查继承关系:")

print(f"\nDog 是 Mammal 的子类: {issubclass(Dog, Mammal)}")
print(f"Dog 是 Animal 的子类: {issubclass(Dog, Animal)}")
print(f"Mammal 是 Dog 的子类: {issubclass(Mammal, Dog)}")

print(f"\ndog 是 Dog 的实例: {isinstance(dog, Dog)}")
print(f"dog 是 Mammal 的实例: {isinstance(dog, Mammal)}")
print(f"dog 是 Animal 的实例: {isinstance(dog, Animal)}")

# 查看继承链
print(f"\nDog 的继承链: {Dog.__mro__}")


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("继承综合练习")
    print("=" * 50)

    # 练习：创建一个图形类层次结构
    class Shape:
        """图形基类"""

        def __init__(self, color="黑色"):
            self.color = color

        def area(self):
            """计算面积 - 子类需要重写"""
            raise NotImplementedError("子类必须实现 area 方法")

        def perimeter(self):
            """计算周长 - 子类需要重写"""
            raise NotImplementedError("子类必须实现 perimeter 方法")

        def describe(self):
            """描述图形"""
            print(f"这是一个{self.color}的图形")

    class Rectangle(Shape):
        """矩形"""

        def __init__(self, width, height, color="黑色"):
            super().__init__(color)
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2 * (self.width + self.height)

        def describe(self):
            print(f"这是一个{self.color}的矩形，宽{self.width}，高{self.height}")

    class Square(Rectangle):
        """正方形 - 继承自矩形"""

        def __init__(self, side, color="黑色"):
            super().__init__(side, side, color)
            self.side = side

        def describe(self):
            print(f"这是一个{self.color}的正方形，边长{self.side}")

    class Circle(Shape):
        """圆形"""

        def __init__(self, radius, color="黑色"):
            super().__init__(color)
            self.radius = radius

        def area(self):
            import math
            return math.pi * self.radius ** 2

        def perimeter(self):
            import math
            return 2 * math.pi * self.radius

        def describe(self):
            print(f"这是一个{self.color}的圆形，半径{self.radius}")

    # 测试
    print("\n图形类测试:")
    shapes = [
        Rectangle(4, 5, "红色"),
        Square(3, "蓝色"),
        Circle(2, "绿色")
    ]

    for shape in shapes:
        shape.describe()
        print(f"  面积: {shape.area():.2f}")
        print(f"  周长: {shape.perimeter():.2f}")
        print()

    print("=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. 继承的语法：class 子类(父类):
#
# 2. 子类可以：
#    - 继承父类的属性和方法
#    - 添加新的属性和方法
#    - 重写父类的方法
#
# 3. super() 函数：
#    - 调用父类的方法
#    - 常用于 __init__ 中初始化父类属性
#
# 4. 多层继承：A -> B -> C
#
# 5. 检查继承关系：
#    - issubclass(子类, 父类)
#    - isinstance(对象, 类)
#    - 类.__mro__：查看继承链
