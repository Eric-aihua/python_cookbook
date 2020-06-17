# -*- coding:utf-8 -*-
# @Author：sunaihua
# 深度优先算法

# 边节点
class EdgeNode:
    def __init__(self, adjvex, weight=0):
        self.adjvex = adjvex
        self.weight = weight;

    def __str__(self):
        return '%s-%s' % (self.adjvex, self.weight)


# 顶点节点
class VertexNode:
    def __init__(self, data, adjvex, edge_list=None):
        self.adjvex = adjvex
        self.data = data
        self.edge_list = edge_list

    def __str__(self):
        edge_str = '_'.join([edge.adjvex.data for edge in self.edge_list])
        # print edge_str
        # print [edge.adjvex for edge in self.edge_list]
        return "%s-%s-(%s)" % (self.adjvex, self.data, edge_str)


class GraphAdjList:
    def __init__(self):
        self.adj_list = []

    def add_vertex(self, vertex_node):
        self.adj_list.append(vertex_node)


graph_data = {'A': ['B', 'G', 'F'], 'B': ['C', 'I', 'G', 'A'], 'C': ['D', 'I', 'B'], 'D': ['E', 'H', 'G', 'I', 'C'],
              'E': ['F', 'H', 'D'], 'F': ['A', 'G', 'E'], 'G': ['F', 'B', 'D', 'H'], 'H': ['D', 'E', 'G'],
              'I': ['B', 'C', 'D']}
visited_vertex_list = []
vertex_size = 9


# 根据数据初始化图
def create_al_graph():
    graph_adjvex_list = GraphAdjList()
    adjvex_map = {}

    for i, data in enumerate(graph_data.iterkeys()):
        vertex_node = VertexNode(data, i)
        adjvex_map[data] = vertex_node
        graph_adjvex_list.add_vertex(vertex_node)

    for vertex_node in graph_adjvex_list.adj_list:
        adjvex_list = graph_data[vertex_node.data]
        vertex_node.edge_list = [EdgeNode(adjvex_map[adjvex]) for adjvex in adjvex_list]

    return graph_adjvex_list

# 深度优先遍历
def dfs(adjvex):
    if len(visited_vertex_list) <= vertex_size:
        # 处理顶点信息
        if adjvex.data not in visited_vertex_list:
            visited_vertex_list.append(adjvex.data)
            print adjvex.data
        # 处理边
        for edge in adjvex.edge_list:
            if edge.adjvex.data not in visited_vertex_list:
                visited_vertex_list.append(edge.adjvex.data)
                print edge.adjvex.data
                dfs(edge.adjvex)
    else:
        return


if __name__ == '__main__':
    graph = create_al_graph()  # 创建图
    dfs(graph.adj_list[0])  # 从第一个节点开始遍历
