#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/1 9:35
# @Author  : Xavier Ma
# @Email   : xavier_mayiming.com
# @File    : Dijkstra.py
# @Statement : The Dijkstra's algorithm (with Priority queue)
# @Reference : The pseudocode on wikipedia
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


def main(network, source, destination):
    """
    The Dijkstra algorithm for the shortest path problem
    :param network: {node1: {node2: length, node3: length, ...}, ...}
    :param source: the source node
    :param destination: the destination node
    :return:
    """
    nn = len(network)  # node number
    neighbor = find_neighbor(network)
    dist = []
    prev = []
    path = []
    inf = 1e6
    queue = []
    for node in range(nn):
        if node == source:
            dist.append(0)
            prev.append(-1)
            path.append([source])
        else:
            dist.append(inf)
            prev.append(-2)
            path.append([])
    heapq.heappush(queue, (dist[source], source))
    searched_node = []
    while queue:
        dis, temp_node = heapq.heappop(queue)
        if temp_node == destination:
            break
        if temp_node not in searched_node:
            searched_node.append(temp_node)
            for node in neighbor[temp_node]:
                alt = dis + network[temp_node][node]
                if alt < dist[node]:
                    dist[node] = alt
                    prev[node] = temp_node
                    temp_path = copy.deepcopy(path[temp_node])
                    temp_path.append(node)
                    path[node] = temp_path
                    heapq.heappush(queue, (alt, node))
    result = {
        'path': path[destination],
        'length': dist[destination],
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
    destination = 4
    print(main(test_network, source, destination))
