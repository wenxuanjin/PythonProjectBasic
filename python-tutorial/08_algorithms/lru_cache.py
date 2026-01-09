"""
第8章：基础算法 - LRU 缓存
========================

本文件学习目标：
1. 理解 LRU 缓存的概念
2. 理解 LRU 的工作原理
3. 使用 dict + list 实现 LRU
4. 理解缓存的应用场景

注意：本实现不是为了性能，而是为了理解 LRU 的思想。
实际应用中可以使用 functools.lru_cache 或 collections.OrderedDict。
"""

# ============================================================
# 一、什么是 LRU 缓存？
# ============================================================
#
# LRU = Least Recently Used（最近最少使用）
#
# LRU 缓存是一种缓存淘汰策略：
# - 缓存有固定的容量
# - 当缓存满了，需要淘汰一些数据
# - LRU 策略：淘汰最近最少使用的数据
#
# 生活中的例子：
# - 手机最近使用的 App 列表
# - 浏览器的历史记录
# - 操作系统的内存页面置换
#
# 核心操作：
# - get(key)：获取数据，如果存在则返回并标记为"最近使用"
# - put(key, value)：存入数据，如果缓存满了则淘汰最久未使用的


# ============================================================
# 二、使用 dict + list 实现 LRU
# ============================================================

print("LRU 缓存 - 使用 dict + list 实现:")
print("=" * 50)


class LRUCache:
    """
    LRU 缓存实现

    使用字典存储数据，使用列表维护访问顺序。
    列表头部是最久未使用的，尾部是最近使用的。

    注意：这个实现的时间复杂度不是最优的（O(n)），
    但是更容易理解 LRU 的思想。
    """

    def __init__(self, capacity):
        """
        初始化 LRU 缓存

        参数:
            capacity: 缓存容量
        """
        self.capacity = capacity
        self.cache = {}  # 存储键值对
        self.order = []  # 维护访问顺序，最近使用的在末尾

    def get(self, key):
        """
        获取缓存中的值

        参数:
            key: 键

        返回:
            如果存在返回值，否则返回 -1
        """
        if key in self.cache:
            # 更新访问顺序：移到末尾
            self.order.remove(key)
            self.order.append(key)
            print(f"  GET {key}: 命中缓存，值为 {self.cache[key]}")
            return self.cache[key]
        else:
            print(f"  GET {key}: 未命中")
            return -1

    def put(self, key, value):
        """
        存入缓存

        参数:
            key: 键
            value: 值
        """
        if key in self.cache:
            # 更新已存在的键
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
            print(f"  PUT {key}={value}: 更新已存在的键")
        else:
            # 检查容量
            if len(self.cache) >= self.capacity:
                # 淘汰最久未使用的（列表头部）
                oldest = self.order.pop(0)
                del self.cache[oldest]
                print(f"  PUT {key}={value}: 缓存已满，淘汰 {oldest}")
            else:
                print(f"  PUT {key}={value}: 添加新键")

            # 添加新键
            self.cache[key] = value
            self.order.append(key)

    def show_state(self):
        """显示缓存状态"""
        print(f"  缓存状态: {self.cache}")
        print(f"  访问顺序: {self.order} (左边最久未使用)")


# 测试 LRU 缓存
print("\n测试 LRU 缓存（容量为 3）:")
cache = LRUCache(3)

print("\n1. 添加数据:")
cache.put("A", 1)
cache.put("B", 2)
cache.put("C", 3)
cache.show_state()

print("\n2. 访问 A（A 变成最近使用）:")
cache.get("A")
cache.show_state()

print("\n3. 添加 D（缓存满，淘汰最久未使用的 B）:")
cache.put("D", 4)
cache.show_state()

print("\n4. 访问 B（已被淘汰）:")
cache.get("B")
cache.show_state()

print("\n5. 添加 E（淘汰 C）:")
cache.put("E", 5)
cache.show_state()


# ============================================================
# 三、使用 OrderedDict 实现 LRU
# ============================================================

print("\n" + "=" * 50)
print("LRU 缓存 - 使用 OrderedDict 实现:")

from collections import OrderedDict


class LRUCacheOrderedDict:
    """
    使用 OrderedDict 实现的 LRU 缓存

    OrderedDict 记住了键的插入顺序，
    并且可以高效地移动元素到末尾。

    时间复杂度: O(1)
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            # move_to_end 将键移到末尾
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            # 更新值并移到末尾
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                # popitem(last=False) 删除第一个元素
                self.cache.popitem(last=False)
            self.cache[key] = value

    def show_state(self):
        print(f"  缓存: {dict(self.cache)}")


print("\n测试 OrderedDict 实现:")
cache2 = LRUCacheOrderedDict(3)
cache2.put("A", 1)
cache2.put("B", 2)
cache2.put("C", 3)
cache2.show_state()

cache2.get("A")
cache2.put("D", 4)
cache2.show_state()


# ============================================================
# 四、使用 functools.lru_cache
# ============================================================

print("\n" + "=" * 50)
print("使用 functools.lru_cache:")

from functools import lru_cache


@lru_cache(maxsize=3)
def expensive_function(x):
    """
    模拟一个耗时的函数

    使用 @lru_cache 装饰器自动缓存结果
    """
    print(f"  计算 {x} 的结果...")
    return x * x


print("\n测试 lru_cache:")
print(f"expensive_function(1) = {expensive_function(1)}")
print(f"expensive_function(2) = {expensive_function(2)}")
print(f"expensive_function(3) = {expensive_function(3)}")
print(f"expensive_function(1) = {expensive_function(1)}")  # 命中缓存
print(f"expensive_function(4) = {expensive_function(4)}")  # 淘汰最久未使用的
print(f"expensive_function(2) = {expensive_function(2)}")  # 可能已被淘汰

# 查看缓存信息
print(f"\n缓存信息: {expensive_function.cache_info()}")


# ============================================================
# 五、LRU 缓存的应用场景
# ============================================================

print("\n" + "=" * 50)
print("LRU 缓存的应用场景:")

print("""
1. 数据库查询缓存
   - 缓存常用的查询结果
   - 减少数据库访问

2. Web 页面缓存
   - 缓存渲染后的页面
   - 提高响应速度

3. 计算结果缓存
   - 缓存耗时计算的结果
   - 避免重复计算

4. 文件系统缓存
   - 缓存最近访问的文件
   - 减少磁盘 I/O

5. DNS 缓存
   - 缓存域名解析结果
   - 加快网络访问
""")


# ============================================================
# 六、实际应用示例
# ============================================================

print("=" * 50)
print("实际应用示例 - 斐波那契数列缓存:")


class FibonacciWithCache:
    """带 LRU 缓存的斐波那契计算"""

    def __init__(self, cache_size=10):
        self.cache = LRUCacheOrderedDict(cache_size)
        self.compute_count = 0

    def fib(self, n):
        """计算斐波那契数列第 n 项"""
        # 先检查缓存
        cached = self.cache.get(n)
        if cached != -1:
            return cached

        # 计算
        self.compute_count += 1
        if n <= 1:
            result = n
        else:
            result = self.fib(n - 1) + self.fib(n - 2)

        # 存入缓存
        self.cache.put(n, result)
        return result


print("\n计算斐波那契数列:")
fib_calc = FibonacciWithCache(cache_size=5)

for i in range(10):
    result = fib_calc.fib(i)
    print(f"F({i}) = {result}")

print(f"\n实际计算次数: {fib_calc.compute_count}")


# ============================================================
# 主程序入口
# ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("LRU 缓存综合练习")
    print("=" * 50)

    # 练习1：实现一个简单的网页缓存
    class WebPageCache:
        """简单的网页缓存"""

        def __init__(self, capacity):
            self.cache = LRUCacheOrderedDict(capacity)
            self.hit_count = 0
            self.miss_count = 0

        def get_page(self, url):
            """获取网页内容"""
            content = self.cache.get(url)
            if content != -1:
                self.hit_count += 1
                print(f"  缓存命中: {url}")
                return content
            else:
                self.miss_count += 1
                # 模拟从网络获取
                content = f"Content of {url}"
                self.cache.put(url, content)
                print(f"  缓存未命中，从网络获取: {url}")
                return content

        def stats(self):
            """显示统计信息"""
            total = self.hit_count + self.miss_count
            hit_rate = self.hit_count / total * 100 if total > 0 else 0
            print(f"  命中: {self.hit_count}, 未命中: {self.miss_count}")
            print(f"  命中率: {hit_rate:.1f}%")

    print("\n网页缓存示例:")
    web_cache = WebPageCache(3)

    urls = [
        "http://example.com/page1",
        "http://example.com/page2",
        "http://example.com/page3",
        "http://example.com/page1",  # 命中
        "http://example.com/page4",  # 淘汰 page2
        "http://example.com/page2",  # 未命中
        "http://example.com/page1",  # 命中
    ]

    for url in urls:
        web_cache.get_page(url)

    print("\n统计信息:")
    web_cache.stats()

    print("\n" + "=" * 50)
    print("本节学习完成！")
    print("=" * 50)


# ============================================================
# 本节小结
# ============================================================
#
# 1. LRU 缓存概念：
#    - Least Recently Used（最近最少使用）
#    - 淘汰最久未使用的数据
#
# 2. 核心操作：
#    - get(key)：获取数据，更新访问顺序
#    - put(key, value)：存入数据，可能触发淘汰
#
# 3. 实现方式：
#    - dict + list：简单但效率低 O(n)
#    - OrderedDict：高效 O(1)
#    - functools.lru_cache：装饰器方式
#
# 4. 应用场景：
#    - 数据库查询缓存
#    - Web 页面缓存
#    - 计算结果缓存
#
# 5. 本实现的目的：
#    - 理解 LRU 的思想
#    - 不是为了性能优化
#    - 实际应用使用内置工具
