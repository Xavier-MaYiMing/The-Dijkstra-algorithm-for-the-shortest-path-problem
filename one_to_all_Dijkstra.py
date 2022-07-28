#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/20 19:31
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : one_to_all_Dijkstra.py
# @Statement : The Dijkstra algorithm for the one-to-all shortest path problem
# @Reference : Dijkstra E W. A note on two problems in connexion with graphs[M]//Edsger Wybe Dijkstra: His Life, Work, and Legacy. 2022: 287-290.
import copy
import heapq


def find_neighbor(network):
    """
    Find the neighbor of each node
    :param network:
    :return: {node 1: [the neighbor nodes of node 1], ...}
    """
    nn = len(network)
    neighbor = []
    for i in range(nn):
        neighbor.append(list(network[i].keys()))
    return neighbor


def main(network, source):
    """
    The Dijkstra algorithm for the shortest path problem
    :param network: {node1: {node2: length, node3: length, ...}, ...}
    :param source: the source node
    :return:
    """
    nn = len(network)  # node number
    neighbor = find_neighbor(network)
    dist = []
    path = []
    inf = 1e6
    queue = []
    for node in range(nn):
        if node == source:
            dist.append(0)
            path.append([source])
        else:
            dist.append(inf)
            path.append([])
    heapq.heappush(queue, (dist[source], source))
    searched_node = []
    while queue:
        dis, temp_node = heapq.heappop(queue)
        if temp_node not in searched_node:
            searched_node.append(temp_node)
            for node in neighbor[temp_node]:
                alt = dis + network[temp_node][node]
                if alt < dist[node]:
                    dist[node] = alt
                    temp_path = copy.deepcopy(path[temp_node])
                    temp_path.append(node)
                    path[node] = temp_path
                    heapq.heappush(queue, (alt, node))
    result = {}
    for node in range(nn):
        if node != source:
            result[node] = {
                'path': path[node],
                'length': dist[node],
            }
    return result


if __name__ == '__main__':
    test_network = {
        0: {1: 62, 2: 44, 3: 67},
        1: {0: 62, 2: 32, 4: 52},
        2: {0: 44, 1: 33, 3: 32, 4: 52},
        3: {0: 67, 2: 32, 4: 54},
        4: {1: 52, 2: 52, 3: 54}
    }
    source = 0
    print(main(test_network, source))
