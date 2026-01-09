"""
第5章：模块与文件 - 文件读取
==========================

本文件学习目标：
1. 掌握文件读取的基本方法
2. 理解文件打开模式
3. 学会使用 with 语句
4. 掌握不同的读取方式
"""

# ============================================================
# 一、文件操作基础
# ============================================================
#
# 文件操作的基本步骤：
# 1. 打开文件：open()
# 2. 读取/写入文件
# 3. 关闭文件：close()
#
# 文件打开模式：
# 'r'  - 读取（默认）
# 'w'  - 写入（覆盖）
# 'a'  - 追加
# 'x'  - 创建（文件存在则报错）
# 'b'  - 二进制模式
# 't'  - 文本模式（默认）
# '+'  - 读写模式


# ============================================================
# 二、基本文件读取
# ============================================================

import os

# 获取当前文件所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 创建示例文件用于演示
sample_file = os.path.join(current_dir, "sample.txt")

# 先创建一个示例文件
with open(sample_file, 'w', encoding='utf-8') as f:
    f.write("第一行：Hello, Python!\n")
    f.write("第二行：文件操作很简单\n")
    f.write("第三行：让我们一起学习\n")
    f.write("第四行：Python 是最好的语言\n")
    f.write("第五行：加油！\n")

print("基本文件读取:")

# 方式1：传统方式（需要手动关闭）
print("\n方式1：传统方式")
f = open(sample_file, 'r', encoding='utf-8')
content = f.read()
f.close()  # 必须关闭文件
print(content)

# 方式2：使用 with 语句（推荐）
print("方式2：使用 with 语句（推荐）")
with open(sample_file, 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
# with 语句会自动关闭文件，即使发生异常


# ============================================================
# 三、不同的读取方式
# ============================================================

print("=" * 50)
print("不同的读取方式:")

# 1. read()：读取全部内容
print("\n1. read() - 读取全部内容:")
with open(sample_file, 'r', encoding='utf-8') as f:
    content = f.read()
    print(f"类型: {type(content)}")
    print(f"长度: {len(content)} 字符")

# 2. read(n)：读取 n 个字符
print("\n2. read(n) - 读取指定字符数:")
with open(sample_file, 'r', encoding='utf-8') as f:
    first_10 = f.read(10)
    print(f"前10个字符: '{first_10}'")
    next_10 = f.read(10)
    print(f"接下来10个字符: '{next_10}'")

# 3. readline()：读取一行
print("\n3. readline() - 读取一行:")
with open(sample_file, 'r', encoding='utf-8') as f:
    line1 = f.readline()
    line2 = f.readline()
    print(f"第一行: {line1}", end="")
    print(f"第二行: {line2}", end="")

# 4. readlines()：读取所有行，返回列表
print("\n4. readlines() - 读取所有行:")
with open(sample_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(f"类型: {type(lines)}")
    print(f"行数: {len(lines)}")
    print(f"第一行: {lines[0]}", end="")

# 5. 遍历文件对象（推荐，内存效率高）
print("\n5. 遍历文件对象（推荐）:")
with open(sample_file, 'r', encoding='utf-8') as f:
    for line_num, line in enumerate(f, 1):
        print(f"  行 {line_num}: {line}", end="")


# ============================================================
# 四、文件编码
# ============================================================

print("\n" + "=" * 50)
print("文件编码:")

# 常见编码：
# utf-8：通用编码，支持所有语言
# gbk/gb2312：中文编码
# ascii：英文编码

# 读取文件时指定编码
with open(sample_file, 'r', encoding='utf-8') as f:
    content = f.read()
    print(f"使用 UTF-8 编码读取成功")

# 如果编码不对，会出现乱码或报错
# 处理编码错误
try:
    with open(sample_file, 'r', encoding='ascii', errors='ignore') as f:
        content = f.read()
        print(f"使用 ASCII 编码（忽略错误）: {content[:20]}...")
except UnicodeDecodeError as e:
    print(f"编码错误: {e}")


# ============================================================
# 五、文件路径
# ============================================================

print("\n" + "=" * 50)
print("文件路径:")

# 绝对路径 vs 相对路径
print(f"当前工作目录: {os.getcwd()}")
print(f"当前文件目录: {current_dir}")

# 使用 os.path 处理路径
file_path = os.path.join(current_dir, "sample.txt")
print(f"\n文件路径: {file_path}")
print(f"文件存在: {os.path.exists(file_path)}")
print(f"是文件: {os.path.isfile(file_path)}")
print(f"文件名: {os.path.basename(file_path)}")
print(f"目录名: {os.path.dirname(file_path)}")

# 获取文件信息
if os.path.exists(file_path):
    file_stat = os.stat(file_path)
    print(f"文件大小: {file_stat.st_size} 字节")


# ============================================================
# 六、读取大文件
# ============================================================

print("\n" + "=" * 50)
print("读取大文件:")

# 对于大文件，不要一次性读取全部内容
# 应该逐行读取或分块读取

# 方式1：逐行读取
print("\n方式1：逐行读取")
with open(sample_file, 'r', encoding='utf-8') as f:
    for line in f:
        # 处理每一行
        print(f"  处理: {line.strip()}")

# 方式2：分块读取
print("\n方式2：分块读取")
chunk_size = 20  # 每次读取 20 个字符
with open(sample_file, 'r', encoding='utf-8') as f:
    chunk_num = 0
    while True:
        chunk = f.read(chunk_size)
        if not chunk:
            break
        chunk_num += 1
        print(f"  块 {chunk_num}: {repr(chunk)}")


# ============================================================
# 七、读取二进制文件
# ============================================================

print("\n" + "=" * 50)
print("读取二进制文件:")

# 创建一个二进制文件
binary_file = os.path.join(current_dir, "sample.bin")
with open(binary_file, 'wb') as f:
    f.write(b'\x00\x01\x02\x03\x04\x05')

# 读取二进制文件
with open(binary_file, 'rb') as f:
    data = f.read()
    print(f"类型: {type(data)}")
    print(f"内容: {data}")
    print(f"十六进制: {data.hex()}")

# 清理临时文件
os.remove(binary_file)


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("文件读取综合练习")
    print("=" * 50)

    # 练习1：统计文件行数和字符数
    print("\n统计文件信息:")
    with open(sample_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        total_chars = sum(len(line) for line in lines)
        total_words = sum(len(line.split()) for line in lines)

    print(f"文件: {sample_file}")
    print(f"行数: {len(lines)}")
    print(f"字符数: {total_chars}")
    print(f"单词数: {total_words}")

    # 练习2：查找包含特定内容的行
    print("\n查找包含 'Python' 的行:")
    with open(sample_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            if 'Python' in line:
                print(f"  行 {line_num}: {line.strip()}")

    # 练习3：读取文件并转换为列表
    print("\n读取文件内容到列表:")
    with open(sample_file, 'r', encoding='utf-8') as f:
        content_list = [line.strip() for line in f if line.strip()]
    print(f"内容列表: {content_list}")

    # 清理示例文件
    if os.path.exists(sample_file):
        os.remove(sample_file)
        print(f"\n已清理示例文件: {sample_file}")

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. 文件操作步骤：打开 -> 读取/写入 -> 关闭
#
# 2. 使用 with 语句自动管理文件（推荐）
#
# 3. 读取方式：
#    - read()：读取全部
#    - read(n)：读取 n 个字符
#    - readline()：读取一行
#    - readlines()：读取所有行
#    - 遍历文件对象：逐行读取（推荐）
#
# 4. 文件编码：
#    - 推荐使用 utf-8
#    - 指定 encoding 参数
#
# 5. 文件路径：
#    - 使用 os.path 处理路径
#    - 注意绝对路径和相对路径
#
# 6. 大文件处理：
#    - 逐行读取
#    - 分块读取
#
# 7. 二进制文件：使用 'rb' 模式
