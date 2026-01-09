"""
第10章：标准答案 - 项目练习答案
==============================

本文件包含 09_practice/project_exercises.md 中项目一（学生成绩管理系统）的参考实现。
"""

import json
import os
from datetime import datetime

# ============================================================
# 项目一：学生成绩管理系统
# ============================================================


class Student:
    """学生类"""

    def __init__(self, name, student_id):
        """
        初始化学生

        参数:
            name: 学生姓名
            student_id: 学号
        """
        self.name = name
        self.student_id = student_id
        self.scores = {}  # 科目 -> 分数

    def add_score(self, subject, score):
        """
        添加成绩

        参数:
            subject: 科目
            score: 分数
        """
        if not 0 <= score <= 100:
            raise ValueError("分数必须在 0-100 之间")
        self.scores[subject] = score

    def get_average(self):
        """计算平均分"""
        if not self.scores:
            return 0
        return sum(self.scores.values()) / len(self.scores)

    def to_dict(self):
        """转换为字典（用于保存）"""
        return {
            "name": self.name,
            "student_id": self.student_id,
            "scores": self.scores
        }

    @classmethod
    def from_dict(cls, data):
        """从字典创建学生对象"""
        student = cls(data["name"], data["student_id"])
        student.scores = data.get("scores", {})
        return student

    def __str__(self):
        return f"学生: {self.name} (学号: {self.student_id})"


class GradeManager:
    """成绩管理器"""

    def __init__(self):
        """初始化成绩管理器"""
        self.students = {}  # 学号 -> Student

    def add_student(self, name, student_id):
        """
        添加学生

        参数:
            name: 学生姓名
            student_id: 学号

        返回:
            True 如果添加成功，False 如果学号已存在
        """
        if student_id in self.students:
            return False
        self.students[student_id] = Student(name, student_id)
        return True

    def get_student(self, student_id):
        """获取学生"""
        return self.students.get(student_id)

    def add_score(self, student_id, subject, score):
        """
        录入成绩

        参数:
            student_id: 学号
            subject: 科目
            score: 分数

        返回:
            True 如果录入成功，False 如果学生不存在
        """
        student = self.get_student(student_id)
        if not student:
            return False
        student.add_score(subject, score)
        return True

    def get_ranking(self):
        """
        获取排名（按平均分降序）

        返回:
            排名列表 [(学生, 平均分), ...]
        """
        ranking = []
        for student in self.students.values():
            avg = student.get_average()
            ranking.append((student, avg))
        ranking.sort(key=lambda x: x[1], reverse=True)
        return ranking

    def save_to_file(self, filename):
        """
        保存数据到文件

        参数:
            filename: 文件名
        """
        data = {
            "students": [s.to_dict() for s in self.students.values()]
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_from_file(self, filename):
        """
        从文件加载数据

        参数:
            filename: 文件名

        返回:
            True 如果加载成功，False 如果文件不存在
        """
        if not os.path.exists(filename):
            return False

        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        self.students = {}
        for student_data in data.get("students", []):
            student = Student.from_dict(student_data)
            self.students[student.student_id] = student

        return True

    def show_all_students(self):
        """显示所有学生"""
        if not self.students:
            print("暂无学生数据")
            return

        print("\n所有学生:")
        print("-" * 50)
        for student in self.students.values():
            print(f"  {student.name} (学号: {student.student_id})")
            if student.scores:
                for subject, score in student.scores.items():
                    print(f"    {subject}: {score}")
                print(f"    平均分: {student.get_average():.2f}")
            else:
                print("    暂无成绩")
        print("-" * 50)


def main():
    """主函数 - 命令行交互"""
    manager = GradeManager()
    data_file = "students_data.json"

    # 尝试加载已有数据
    if manager.load_from_file(data_file):
        print(f"已加载数据文件: {data_file}")

    while True:
        print("\n" + "=" * 40)
        print("学生成绩管理系统")
        print("=" * 40)
        print("1. 添加学生")
        print("2. 录入成绩")
        print("3. 查询学生")
        print("4. 查看排名")
        print("5. 显示所有学生")
        print("6. 保存数据")
        print("7. 退出")
        print("-" * 40)

        choice = input("请选择操作 (1-7): ").strip()

        if choice == "1":
            # 添加学生
            name = input("请输入学生姓名: ").strip()
            student_id = input("请输入学号: ").strip()
            if manager.add_student(name, student_id):
                print(f"添加成功: {name} ({student_id})")
            else:
                print("添加失败: 学号已存在")

        elif choice == "2":
            # 录入成绩
            student_id = input("请输入学号: ").strip()
            student = manager.get_student(student_id)
            if not student:
                print("学生不存在")
                continue

            subject = input("请输入科目: ").strip()
            try:
                score = float(input("请输入成绩: ").strip())
                if manager.add_score(student_id, subject, score):
                    print("录入成功")
                else:
                    print("录入失败")
            except ValueError as e:
                print(f"输入错误: {e}")

        elif choice == "3":
            # 查询学生
            student_id = input("请输入学号: ").strip()
            student = manager.get_student(student_id)
            if student:
                print(f"\n{student}")
                if student.scores:
                    print("成绩:")
                    for subject, score in student.scores.items():
                        print(f"  {subject}: {score}")
                    print(f"平均分: {student.get_average():.2f}")
                else:
                    print("暂无成绩")
            else:
                print("学生不存在")

        elif choice == "4":
            # 查看排名
            ranking = manager.get_ranking()
            if not ranking:
                print("暂无数据")
                continue

            print("\n成绩排名:")
            print("-" * 40)
            for i, (student, avg) in enumerate(ranking, 1):
                print(f"  {i}. {student.name} - 平均分: {avg:.2f}")
            print("-" * 40)

        elif choice == "5":
            # 显示所有学生
            manager.show_all_students()

        elif choice == "6":
            # 保存数据
            manager.save_to_file(data_file)
            print(f"数据已保存到: {data_file}")

        elif choice == "7":
            # 退出
            save = input("是否保存数据? (y/n): ").strip().lower()
            if save == 'y':
                manager.save_to_file(data_file)
                print(f"数据已保存到: {data_file}")
            print("再见!")
            break

        else:
            print("无效的选择，请重新输入")


# ============================================================
# 演示运行
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("学生成绩管理系统 - 演示")
    print("=" * 60)

    # 创建管理器
    manager = GradeManager()

    # 添加学生
    print("\n1. 添加学生:")
    manager.add_student("张三", "2024001")
    manager.add_student("李四", "2024002")
    manager.add_student("王五", "2024003")
    print("已添加 3 名学生")

    # 录入成绩
    print("\n2. 录入成绩:")
    manager.add_score("2024001", "语文", 85)
    manager.add_score("2024001", "数学", 92)
    manager.add_score("2024001", "英语", 88)

    manager.add_score("2024002", "语文", 78)
    manager.add_score("2024002", "数学", 95)
    manager.add_score("2024002", "英语", 82)

    manager.add_score("2024003", "语文", 90)
    manager.add_score("2024003", "数学", 88)
    manager.add_score("2024003", "英语", 95)
    print("成绩录入完成")

    # 显示所有学生
    print("\n3. 所有学生信息:")
    manager.show_all_students()

    # 查看排名
    print("\n4. 成绩排名:")
    ranking = manager.get_ranking()
    for i, (student, avg) in enumerate(ranking, 1):
        print(f"  {i}. {student.name} - 平均分: {avg:.2f}")

    # 保存数据
    print("\n5. 保存数据:")
    manager.save_to_file("demo_students.json")
    print("数据已保存到 demo_students.json")

    # 加载数据
    print("\n6. 重新加载数据:")
    new_manager = GradeManager()
    new_manager.load_from_file("demo_students.json")
    print(f"已加载 {len(new_manager.students)} 名学生")

    # 清理演示文件
    if os.path.exists("demo_students.json"):
        os.remove("demo_students.json")
        print("\n已清理演示文件")

    print("\n" + "=" * 60)
    print("演示完成！")
    print("=" * 60)
    print("\n提示: 运行 main() 函数可以启动交互式界面")
