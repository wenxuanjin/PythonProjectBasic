# 小项目练习题

本文件包含综合性的小项目练习，帮助你将所学知识应用到实际场景中。

## 项目一：学生成绩管理系统

### 项目描述
创建一个简单的学生成绩管理系统，支持以下功能：
1. 添加学生信息（姓名、学号）
2. 录入学生成绩（科目、分数）
3. 查询学生成绩
4. 计算平均分
5. 按成绩排名
6. 保存数据到文件
7. 从文件加载数据

### 要求
- 使用面向对象编程
- 使用文件存储数据（JSON 格式）
- 提供命令行交互界面

### 示例结构
```python
class Student:
    """学生类"""
    def __init__(self, name, student_id):
        pass

    def add_score(self, subject, score):
        pass

    def get_average(self):
        pass

class GradeManager:
    """成绩管理器"""
    def __init__(self):
        pass

    def add_student(self, name, student_id):
        pass

    def add_score(self, student_id, subject, score):
        pass

    def get_ranking(self):
        pass

    def save_to_file(self, filename):
        pass

    def load_from_file(self, filename):
        pass

def main():
    """主函数 - 命令行交互"""
    pass
```

### 示例交互
```
=== 学生成绩管理系统 ===
1. 添加学生
2. 录入成绩
3. 查询成绩
4. 查看排名
5. 保存数据
6. 加载数据
7. 退出

请选择操作: 1
请输入学生姓名: 张三
请输入学号: 2024001
添加成功！

请选择操作: 2
请输入学号: 2024001
请输入科目: 数学
请输入成绩: 85
录入成功！
```

---

## 项目二：简易计算器

### 项目描述
创建一个支持基本运算的计算器，支持：
1. 加减乘除
2. 括号运算
3. 幂运算
4. 历史记录

### 要求
- 支持表达式解析（如 "2 + 3 * 4"）
- 正确处理运算符优先级
- 支持括号
- 记录计算历史

### 示例
```python
class Calculator:
    """计算器类"""

    def __init__(self):
        self.history = []

    def calculate(self, expression):
        """
        计算表达式

        参数:
            expression: 数学表达式字符串

        返回:
            计算结果
        """
        pass

    def show_history(self):
        """显示历史记录"""
        pass

# 使用示例
calc = Calculator()
print(calc.calculate("2 + 3 * 4"))  # 14
print(calc.calculate("(2 + 3) * 4"))  # 20
print(calc.calculate("2 ** 3"))  # 8
```

---

## 项目三：待办事项管理器

### 项目描述
创建一个命令行待办事项管理器，支持：
1. 添加待办事项
2. 标记完成
3. 删除事项
4. 查看所有事项
5. 按优先级排序
6. 数据持久化

### 要求
- 每个事项包含：标题、描述、优先级、状态、创建时间
- 支持按优先级和状态筛选
- 数据保存到文件

### 示例结构
```python
from datetime import datetime

class TodoItem:
    """待办事项"""
    def __init__(self, title, description="", priority=1):
        self.title = title
        self.description = description
        self.priority = priority  # 1-5，5最高
        self.completed = False
        self.created_at = datetime.now()

class TodoManager:
    """待办事项管理器"""
    def __init__(self):
        self.items = []

    def add(self, title, description="", priority=1):
        pass

    def complete(self, index):
        pass

    def delete(self, index):
        pass

    def list_all(self, show_completed=True):
        pass

    def list_by_priority(self, priority):
        pass
```

---

## 项目四：文本分析工具

### 项目描述
创建一个文本分析工具，可以分析文本文件并输出统计信息：
1. 字符数（含/不含空格）
2. 单词数
3. 行数
4. 段落数
5. 最常见的单词（Top 10）
6. 平均单词长度

### 要求
- 支持读取文件
- 支持中英文
- 输出格式化的统计报告

### 示例
```python
class TextAnalyzer:
    """文本分析器"""

    def __init__(self, text):
        self.text = text

    def char_count(self, include_spaces=True):
        """统计字符数"""
        pass

    def word_count(self):
        """统计单词数"""
        pass

    def line_count(self):
        """统计行数"""
        pass

    def most_common_words(self, n=10):
        """最常见的单词"""
        pass

    def generate_report(self):
        """生成分析报告"""
        pass

# 使用示例
with open("sample.txt", "r") as f:
    text = f.read()

analyzer = TextAnalyzer(text)
print(analyzer.generate_report())
```

---

## 项目五：简易通讯录

### 项目描述
创建一个通讯录管理程序，支持：
1. 添加联系人（姓名、电话、邮箱、地址）
2. 删除联系人
3. 修改联系人信息
4. 搜索联系人（按姓名或电话）
5. 显示所有联系人
6. 导出为 CSV 文件
7. 从 CSV 文件导入

### 要求
- 使用类封装联系人信息
- 支持模糊搜索
- 数据持久化

### 示例结构
```python
class Contact:
    """联系人"""
    def __init__(self, name, phone, email="", address=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class AddressBook:
    """通讯录"""
    def __init__(self):
        self.contacts = []

    def add(self, contact):
        pass

    def remove(self, name):
        pass

    def update(self, name, **kwargs):
        pass

    def search(self, keyword):
        pass

    def list_all(self):
        pass

    def export_csv(self, filename):
        pass

    def import_csv(self, filename):
        pass
```

---

## 提示

1. 先设计好类的结构和方法
2. 分步实现，先实现核心功能
3. 添加异常处理
4. 编写测试用例
5. 考虑用户体验（输入验证、友好提示）
6. 对照 `10_answers/project_answers.py` 参考实现
