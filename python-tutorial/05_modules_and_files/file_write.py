"""
第5章：模块与文件 - 文件写入
==========================

本文件学习目标：
1. 掌握文件写入的基本方法
2. 理解写入模式的区别
3. 学会使用 with 语句写入文件
4. 掌握文件追加操作
"""

# ============================================================
# 一、文件写入基础
# ============================================================
#
# 文件写入模式：
# 'w'  - 写入模式（覆盖原有内容）
# 'a'  - 追加模式（在文件末尾添加）
# 'x'  - 创建模式（文件存在则报错）
# 'w+' - 读写模式（覆盖）
# 'a+' - 读写模式（追加）

import os

# 获取当前文件所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))


# ============================================================
# 二、基本文件写入
# ============================================================

print("基本文件写入:")

# 创建写入文件路径
write_file = os.path.join(current_dir, "output.txt")

# 方式1：使用 write() 写入字符串
print("\n方式1：write() 写入字符串")
with open(write_file, 'w', encoding='utf-8') as f:
    f.write("第一行内容\n")
    f.write("第二行内容\n")
    f.write("第三行内容\n")
print(f"文件已写入: {write_file}")

# 读取验证
with open(write_file, 'r', encoding='utf-8') as f:
    print("文件内容:")
    print(f.read())


# 方式2：使用 writelines() 写入多行
print("方式2：writelines() 写入多行")
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open(write_file, 'w', encoding='utf-8') as f:
    f.writelines(lines)

# 读取验证
with open(write_file, 'r', encoding='utf-8') as f:
    print("文件内容:")
    print(f.read())


# ============================================================
# 三、写入模式对比
# ============================================================

print("=" * 50)
print("写入模式对比:")

# 'w' 模式：覆盖写入
print("\n'w' 模式：覆盖写入")
with open(write_file, 'w', encoding='utf-8') as f:
    f.write("原始内容\n")

with open(write_file, 'w', encoding='utf-8') as f:
    f.write("新内容（覆盖了原始内容）\n")

with open(write_file, 'r', encoding='utf-8') as f:
    print(f.read())


# 'a' 模式：追加写入
print("'a' 模式：追加写入")
with open(write_file, 'a', encoding='utf-8') as f:
    f.write("追加的内容1\n")

with open(write_file, 'a', encoding='utf-8') as f:
    f.write("追加的内容2\n")

with open(write_file, 'r', encoding='utf-8') as f:
    print(f.read())


# 'x' 模式：创建新文件
print("'x' 模式：创建新文件")
new_file = os.path.join(current_dir, "new_file.txt")

# 先删除文件（如果存在）
if os.path.exists(new_file):
    os.remove(new_file)

try:
    with open(new_file, 'x', encoding='utf-8') as f:
        f.write("这是新创建的文件\n")
    print(f"文件创建成功: {new_file}")
except FileExistsError:
    print("文件已存在，无法创建")

# 再次尝试创建（会失败）
try:
    with open(new_file, 'x', encoding='utf-8') as f:
        f.write("尝试再次创建\n")
except FileExistsError:
    print("文件已存在，创建失败（这是预期的）")

# 清理
os.remove(new_file)


# ============================================================
# 四、with 语句详解
# ============================================================

print("\n" + "=" * 50)
print("with 语句详解:")

# with 语句的优点：
# 1. 自动关闭文件
# 2. 即使发生异常也会关闭文件
# 3. 代码更简洁

# 不使用 with（不推荐）
print("\n不使用 with（不推荐）:")
f = None
try:
    f = open(write_file, 'w', encoding='utf-8')
    f.write("不使用 with 的写法\n")
finally:
    if f:
        f.close()
print("需要手动处理异常和关闭文件")

# 使用 with（推荐）
print("\n使用 with（推荐）:")
with open(write_file, 'w', encoding='utf-8') as f:
    f.write("使用 with 的写法\n")
print("自动处理关闭，代码更简洁")

# 同时打开多个文件
print("\n同时打开多个文件:")
file1 = os.path.join(current_dir, "file1.txt")
file2 = os.path.join(current_dir, "file2.txt")

with open(file1, 'w', encoding='utf-8') as f1, \
     open(file2, 'w', encoding='utf-8') as f2:
    f1.write("文件1的内容\n")
    f2.write("文件2的内容\n")
print("同时写入两个文件成功")

# 清理
os.remove(file1)
os.remove(file2)


# ============================================================
# 五、写入不同类型的数据
# ============================================================

print("\n" + "=" * 50)
print("写入不同类型的数据:")

# write() 只能写入字符串，其他类型需要转换

# 写入数字
print("\n写入数字:")
with open(write_file, 'w', encoding='utf-8') as f:
    number = 12345
    f.write(str(number) + "\n")  # 需要转换为字符串
    f.write(f"{number}\n")  # 使用 f-string

# 写入列表
print("写入列表:")
data = [1, 2, 3, 4, 5]
with open(write_file, 'w', encoding='utf-8') as f:
    f.write(str(data) + "\n")  # 写入列表的字符串表示
    for item in data:
        f.write(f"{item}\n")  # 逐个写入

with open(write_file, 'r', encoding='utf-8') as f:
    print(f.read())

# 写入字典（使用 JSON）
print("写入字典（JSON）:")
import json

data = {"name": "张三", "age": 25, "city": "北京"}
with open(write_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open(write_file, 'r', encoding='utf-8') as f:
    print(f.read())


# ============================================================
# 六、写入二进制文件
# ============================================================

print("\n" + "=" * 50)
print("写入二进制文件:")

binary_file = os.path.join(current_dir, "binary.bin")

# 写入二进制数据
with open(binary_file, 'wb') as f:
    # 写入字节
    f.write(b'\x00\x01\x02\x03\x04')
    # 写入字符串的字节表示
    f.write("Hello".encode('utf-8'))

# 读取验证
with open(binary_file, 'rb') as f:
    data = f.read()
    print(f"二进制数据: {data}")
    print(f"十六进制: {data.hex()}")

# 清理
os.remove(binary_file)


# ============================================================
# 七、文件复制
# ============================================================

print("\n" + "=" * 50)
print("文件复制:")

# 创建源文件
source_file = os.path.join(current_dir, "source.txt")
dest_file = os.path.join(current_dir, "dest.txt")

with open(source_file, 'w', encoding='utf-8') as f:
    f.write("这是源文件的内容\n")
    f.write("第二行\n")
    f.write("第三行\n")

# 方式1：一次性复制（适合小文件）
print("\n方式1：一次性复制")
with open(source_file, 'r', encoding='utf-8') as src:
    with open(dest_file, 'w', encoding='utf-8') as dst:
        dst.write(src.read())
print("复制完成")

# 方式2：逐行复制（适合大文件）
print("\n方式2：逐行复制")
with open(source_file, 'r', encoding='utf-8') as src:
    with open(dest_file, 'w', encoding='utf-8') as dst:
        for line in src:
            dst.write(line)
print("复制完成")

# 方式3：使用 shutil 模块（推荐）
print("\n方式3：使用 shutil 模块")
import shutil
shutil.copy(source_file, dest_file)
print("复制完成")

# 清理
os.remove(source_file)
os.remove(dest_file)


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("文件写入综合练习")
    print("=" * 50)

    # 练习1：写入学生成绩
    print("\n写入学生成绩:")
    students = [
        {"name": "张三", "score": 85},
        {"name": "李四", "score": 92},
        {"name": "王五", "score": 78},
    ]

    scores_file = os.path.join(current_dir, "scores.txt")
    with open(scores_file, 'w', encoding='utf-8') as f:
        f.write("学生成绩表\n")
        f.write("=" * 20 + "\n")
        for student in students:
            f.write(f"{student['name']}: {student['score']}分\n")
        f.write("=" * 20 + "\n")
        avg = sum(s['score'] for s in students) / len(students)
        f.write(f"平均分: {avg:.2f}\n")

    with open(scores_file, 'r', encoding='utf-8') as f:
        print(f.read())

    # 练习2：日志记录
    print("日志记录:")
    from datetime import datetime

    log_file = os.path.join(current_dir, "app.log")

    def log(message):
        """写入日志"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] {message}\n")

    log("程序启动")
    log("用户登录")
    log("执行操作")
    log("程序结束")

    with open(log_file, 'r', encoding='utf-8') as f:
        print(f.read())

    # 练习3：配置文件
    print("配置文件:")
    config_file = os.path.join(current_dir, "config.json")
    config = {
        "app_name": "Python 教程",
        "version": "1.0.0",
        "debug": True,
        "database": {
            "host": "localhost",
            "port": 3306
        }
    }

    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

    with open(config_file, 'r', encoding='utf-8') as f:
        print(f.read())

    # 清理所有临时文件
    for temp_file in [write_file, scores_file, log_file, config_file]:
        if os.path.exists(temp_file):
            os.remove(temp_file)

    print("\n已清理所有临时文件")

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. 写入模式：
#    - 'w'：覆盖写入
#    - 'a'：追加写入
#    - 'x'：创建新文件
#
# 2. 写入方法：
#    - write()：写入字符串
#    - writelines()：写入字符串列表
#
# 3. with 语句：
#    - 自动关闭文件
#    - 异常安全
#    - 推荐使用
#
# 4. 写入不同类型：
#    - 数字：需要转换为字符串
#    - 列表/字典：使用 JSON
#
# 5. 二进制写入：使用 'wb' 模式
#
# 6. 文件复制：
#    - 小文件：一次性读写
#    - 大文件：逐行或分块
#    - 推荐：shutil.copy()
