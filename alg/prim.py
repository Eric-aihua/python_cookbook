# -*- coding:utf-8 -*-
# @Author：sunaihua
"""
普里姆算法（Prim算法）:最小生成树算法
本实现基于邻接矩阵存储结构
"""
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

start_node = 0  # 0节点为初始节点

new_v_array = [] #最小生成树的vertex数组
edge_value_array = [] #最小生成树的权值数组
new_e_array = [] #最小生成树的edge数组


def prim():
    v_number = len(graph)
    latest_edge_target = -1
    new_v_array.append(start_node)
    while True:
        if len(new_v_array) < v_number:
            smallest_value = MAX_VALUE
            for n_index in new_v_array:
                cur_net = graph[n_index]
                for index, value in enumerate(cur_net): # 选出new_v_array中所有边的最小值
                    if index not in new_v_array:
                        if (value != 0) and (value <= smallest_value):
                            smallest_value = value
                            latest_edge_target = index
                            latest_edge_src = n_index
                    else:
                        continue
                    print(new_v_array, n_index, index, value, smallest_value, latest_edge_target)
            if latest_edge_target not in new_v_array:
                print("merge:", latest_edge_src, latest_edge_target, smallest_value)
                new_e_array.append([latest_edge_src, latest_edge_target])
                new_v_array.append(latest_edge_target)
                edge_value_array.append(smallest_value)
        else:
            break

    print("V seq:", new_v_array)
    print("E seq:", new_e_array)
    print("sum value:", sum(edge_value_array))


if __name__ == '__main__':
    prim()
