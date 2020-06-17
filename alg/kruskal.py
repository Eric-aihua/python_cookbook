# -*- coding:utf-8 -*-
# @Author：sunaihua

"""
Kruskal:最小生成树算法
本实现基于邻接矩阵存储结构
"""
import copy

MAX_VALUE = 65536

# 图结构的矩阵存储
graph = [
    [0, 10, MAX_VALUE, MAX_VALUE, MAX_VALUE, 11, MAX_VALUE, MAX_VALUE, MAX_VALUE],
    [10, 0, 18, MAX_VALUE, MAX_VALUE, MAX_VALUE, 16, MAX_VALUE, 12],
    [MAX_VALUE, MAX_VALUE, 0, 22, MAX_VALUE, MAX_VALUE, MAX_VALUE, MAX_VALUE, 8],
    [MAX_VALUE, MAX_VALUE, 22, 0, 20, MAX_VALUE, MAX_VALUE, 16, 21],
    [MAX_VALUE, MAX_VALUE, MAX_VALUE, 20, 0, 26, MAX_VALUE, 7, MAX_VALUE],
    [11, MAX_VALUE, MAX_VALUE, MAX_VALUE, 26, 0, 17, MAX_VALUE, MAX_VALUE],
    [MAX_VALUE, 16, MAX_VALUE, MAX_VALUE, MAX_VALUE, 17, 0, 19, MAX_VALUE],
    [MAX_VALUE, MAX_VALUE, MAX_VALUE, 16, 7, MAX_VALUE, 19, 0, MAX_VALUE],
    [MAX_VALUE, 12, 8, 21, MAX_VALUE, MAX_VALUE, MAX_VALUE, MAX_VALUE, 0],
]

new_v_array = []  # 最小生成树的vertex数组
edge_value_array = []  # 最小生成树的权值数组
new_e_array = []  # 最小生成树的edge数组


class Vertex:
    def __init__(self, distance, x, y):
        self.distance = distance
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.y and self.y == other.x
        else:
            return False

    def __hash__(self):
        m1 = min(self.x, self.y)
        m2 = max(self.x, self.y)
        return hash(("[%s,%s,%s]" % (m1, m2, self.distance)))

    def __repr__(self):
        return "[%s,%s,%s]" % (self.x, self.y, self.distance)


def find(parent, f):
    while parent[f] > 0:
        f = parent[f]
    return f


def kruskal():
    edge_with_distance = set()
    for i, v_net in enumerate(graph):
        for j, k in enumerate(v_net):
            if i != j and k != MAX_VALUE:
                edge_with_distance.add(Vertex(k, i, j))
    # 根据distance排序，并将利用set特性将相同的节点去掉
    sorted_graph = sorted(edge_with_distance, key=lambda x: x.distance, reverse=False)
    parent = [0 for _ in range(len(graph))]
    for ve in sorted_graph:
        if len(new_v_array) == (len(graph)):
            break
        n = find(parent, ve.x)
        m = find(parent, ve.y)
        # 如果n==m,则表明存在循环节点。
        if n != m:
            parent[n] = m
            print("parent2:", parent)
            new_v_array.append(ve)
            new_e_array.append((ve.x, ve.y))
            edge_value_array.append(ve.distance)

    print("V seq:", new_v_array)
    print("E seq:", new_e_array)
    print("sum value:", sum(edge_value_array))


if __name__ == '__main__':
    kruskal()
