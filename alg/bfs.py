# -*- coding:utf-8 -*-
# @Author：sunaihua 
from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = ["bob"]

# 节点对象，用来标识各个节点之间的父子关系
# name:字符串类型，代表节点名称
# parent:Node类型
class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

    def __str__(self):
        return self.name


def is_seller(friend):
    return friend.name[-1] == 'm'

# 通过bfs找到最近的节点
def bfs_search():
    search_queue = deque()
    # 初始化任务队列
    search_queue += [Node(name=friend, parent=Node(name='you', parent=None)) for friend in graph['you']]
    searchrd = []
    while search_queue:
        # 每次都弹出队列最左面的元素，且是关系最亲密的。
        friend = search_queue.popleft()
        # 防止重复搜索
        if friend not in searchrd:
            if is_seller(friend):
                print "has seller,%s is seller" % (friend)
                return friend

            else:
                # 将当前friend的所有friend添加到队列的最右面
                search_queue += [Node(name=f, parent=friend) for f in graph[friend.name]]
    return None

# 根据超找到的对象，打印路径
def print_path(node):
    node_name_stack = []
    node_name_stack.append(node.name)
    parent_node = node.parent
    # 生成节点名称列表
    while parent_node:
        node_name_stack.append(parent_node.name)
        parent_node = parent_node.parent
    # 反转列表
    node_name_stack.reverse()
    # 打印路径
    print "friends path:","--->".join(node_name_stack)


if __name__ == '__main__':
    target = bfs_search()
    print_path(target)
