"""
第7章：面向对象编程 - 类的基础
============================

本文件学习目标：
1. 理解面向对象编程的概念
2. 学会定义类
3. 理解类和对象的关系
4. 掌握类的基本结构
"""

# ============================================================
# 一、什么是面向对象编程？
# ============================================================
#
# 面向对象编程（OOP）是一种编程范式，它将数据和操作数据的方法
# 组织在一起，形成"对象"。
#
# 核心概念：
# 1. 类（Class）：对象的模板/蓝图
# 2. 对象（Object）：类的实例
# 3. 属性（Attribute）：对象的数据
# 4. 方法（Method）：对象的行为
#
# 生活中的例子：
# - 类：汽车的设计图纸
# - 对象：根据图纸生产的具体汽车
# - 属性：颜色、品牌、速度
# - 方法：启动、加速、刹车


# ============================================================
# 二、定义类
# ============================================================

# 最简单的类
class Dog:
    """这是一个简单的狗类"""
    pass  # pass 表示空类


# 创建对象（实例化）
my_dog = Dog()
print("创建对象:")
print(f"my_dog 的类型: {type(my_dog)}")
print(f"my_dog 是 Dog 的实例: {isinstance(my_dog, Dog)}")


# ============================================================
# 三、类的属性
# ============================================================

print("\n" + "=" * 50)
print("类的属性:")


# 带属性的类
class Dog:
    """狗类 - 带属性"""

    # 类属性：所有实例共享
    species = "犬科动物"

    def __init__(self, name, age):
        # 实例属性：每个实例独有
        self.name = name
        self.age = age


# 创建对象
dog1 = Dog("旺财", 3)
dog2 = Dog("小黑", 5)

# 访问实例属性
print(f"\ndog1 的名字: {dog1.name}")
print(f"dog1 的年龄: {dog1.age}")
print(f"dog2 的名字: {dog2.name}")
print(f"dog2 的年龄: {dog2.age}")

# 访问类属性
print(f"\ndog1 的物种: {dog1.species}")
print(f"dog2 的物种: {dog2.species}")
print(f"Dog 类的物种: {Dog.species}")

# 修改实例属性
dog1.age = 4
print(f"\n修改后 dog1 的年龄: {dog1.age}")

# 添加新属性
dog1.color = "黄色"
print(f"dog1 的颜色: {dog1.color}")
# print(dog2.color)  # 报错，dog2 没有 color 属性


# ============================================================
# 四、类的方法
# ============================================================

print("\n" + "=" * 50)
print("类的方法:")


class Dog:
    """狗类 - 带方法"""

    species = "犬科动物"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def bark(self):
        """狗叫"""
        print(f"{self.name} 说: 汪汪汪!")

    def introduce(self):
        """自我介绍"""
        print(f"我叫 {self.name}，今年 {self.age} 岁")

    def get_human_age(self):
        """计算相当于人类的年龄"""
        return self.age * 7


# 创建对象并调用方法
dog = Dog("旺财", 3)

print("\n调用方法:")
dog.bark()
dog.introduce()
print(f"相当于人类年龄: {dog.get_human_age()} 岁")


# ============================================================
# 五、类属性 vs 实例属性
# ============================================================

print("\n" + "=" * 50)
print("类属性 vs 实例属性:")


class Counter:
    """计数器类 - 演示类属性和实例属性"""

    # 类属性：所有实例共享
    total_count = 0

    def __init__(self, name):
        # 实例属性：每个实例独有
        self.name = name
        self.count = 0
        # 每创建一个实例，总计数加1
        Counter.total_count += 1

    def increment(self):
        """增加计数"""
        self.count += 1


# 创建多个实例
c1 = Counter("计数器1")
c2 = Counter("计数器2")
c3 = Counter("计数器3")

print(f"创建了 {Counter.total_count} 个计数器")

# 各自计数
c1.increment()
c1.increment()
c2.increment()

print(f"\n{c1.name} 的计数: {c1.count}")
print(f"{c2.name} 的计数: {c2.count}")
print(f"{c3.name} 的计数: {c3.count}")


# ============================================================
# 六、完整的类示例
# ============================================================

print("\n" + "=" * 50)
print("完整的类示例:")


class BankAccount:
    """
    银行账户类

    属性:
        owner: 账户所有者
        balance: 账户余额

    方法:
        deposit: 存款
        withdraw: 取款
        get_balance: 查询余额
    """

    # 类属性
    bank_name = "Python 银行"
    interest_rate = 0.02  # 年利率 2%

    def __init__(self, owner, balance=0):
        """
        初始化账户

        参数:
            owner: 账户所有者
            balance: 初始余额，默认为 0
        """
        self.owner = owner
        self.balance = balance
        self.transactions = []  # 交易记录

    def deposit(self, amount):
        """
        存款

        参数:
            amount: 存款金额
        """
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"存款: +{amount}")
            print(f"存款成功！存入 {amount} 元")
        else:
            print("存款金额必须大于 0")

    def withdraw(self, amount):
        """
        取款

        参数:
            amount: 取款金额
        """
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transactions.append(f"取款: -{amount}")
                print(f"取款成功！取出 {amount} 元")
            else:
                print(f"余额不足！当前余额: {self.balance} 元")
        else:
            print("取款金额必须大于 0")

    def get_balance(self):
        """查询余额"""
        return self.balance

    def show_transactions(self):
        """显示交易记录"""
        print(f"\n{self.owner} 的交易记录:")
        for t in self.transactions:
            print(f"  {t}")

    def add_interest(self):
        """添加利息"""
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append(f"利息: +{interest:.2f}")
        print(f"添加利息 {interest:.2f} 元")


# 使用银行账户类
print("\n创建账户:")
account = BankAccount("张三", 1000)
print(f"账户所有者: {account.owner}")
print(f"初始余额: {account.get_balance()} 元")

print("\n进行交易:")
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # 余额不足
account.add_interest()

print(f"\n最终余额: {account.get_balance():.2f} 元")
account.show_transactions()


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("类的基础综合练习")
    print("=" * 50)

    # 练习：创建一个学生类
    class Student:
        """学生类"""

        school = "Python 学校"

        def __init__(self, name, student_id, grade):
            self.name = name
            self.student_id = student_id
            self.grade = grade
            self.scores = {}

        def add_score(self, subject, score):
            """添加成绩"""
            self.scores[subject] = score

        def get_average(self):
            """计算平均分"""
            if not self.scores:
                return 0
            return sum(self.scores.values()) / len(self.scores)

        def show_info(self):
            """显示学生信息"""
            print(f"姓名: {self.name}")
            print(f"学号: {self.student_id}")
            print(f"年级: {self.grade}")
            print(f"学校: {self.school}")
            if self.scores:
                print("成绩:")
                for subject, score in self.scores.items():
                    print(f"  {subject}: {score}")
                print(f"平均分: {self.get_average():.2f}")

    # 创建学生对象
    print("\n创建学生:")
    student = Student("小明", "2024001", "高一")
    student.add_score("语文", 85)
    student.add_score("数学", 92)
    student.add_score("英语", 88)
    student.show_info()

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. 面向对象编程的核心概念：
#    - 类：对象的模板
#    - 对象：类的实例
#    - 属性：对象的数据
#    - 方法：对象的行为
#
# 2. 定义类：class 类名:
#
# 3. 创建对象：对象 = 类名()
#
# 4. 类属性 vs 实例属性：
#    - 类属性：所有实例共享
#    - 实例属性：每个实例独有
#
# 5. 方法的第一个参数是 self，代表实例本身
#
# 6. __init__ 方法用于初始化对象
