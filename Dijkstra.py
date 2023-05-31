#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/13 16:14
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : Dijkstra.py
# @Statement : The Dijkstra's algorithm for the shortest path problem (SPP)
# @Reference : Dijkstra E W. A note on two problems in connexion with graphs[M]//Edsger Wybe Dijkstra: His Life, Work, and Legacy. 2022: 287-290.
from numpy import inf
from pqdict import PQDict


def find_neighbors(network):
    # find the neighbors of each node
    neighbor = {}
    for i in network.keys():
        neighbor[i] = list(network[i].keys())
    return neighbor


def main(network, source, destination):
    """
    The main function
    :param network: {node1: {node2: length, node3: length, ...}, ...}
    :param source: the source node
    :param destination: the destination node
    :return:
    """
    # Step 1. Initialization
    neighbor = find_neighbors(network)
    omega = []  # the list of explored labels
    queue = PQDict({})  # priority queue
    queue[source] = 0
    p_list = {source: [source]}  # path label

    # Step 2. The main loop
    while queue:

        # Step 2.1. Select the label with the minimum length
        (n1, length) = queue.popitem()
        path = p_list[n1]
        omega.append(n1)
        if n1 == destination:
            return {'path': path, 'length': length}

        # Step 2.2. Extend labels
        for n2 in neighbor[n1]:
            if n2 not in omega:
                temp_length = length + network[n1][n2]
                if temp_length < queue.get(n2, inf):
                    temp_path = path.copy()
                    temp_path.append(n2)
                    queue[n2] = temp_length
                    p_list[n2] = temp_path

    return {}


if __name__ == '__main__':
    test_network = {
        0: {1: 62, 2: 44, 3: 67},
        1: {0: 62, 2: 32, 4: 52},
        2: {0: 44, 1: 33, 3: 32, 4: 52},
        3: {0: 67, 2: 32, 4: 54},
        4: {1: 52, 2: 52, 3: 54}
    }
    s = 0
    d = 4
    print(main(test_network, s, d))
