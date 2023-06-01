#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/1 13:34
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : m2mDijkstra.py
# @Statement : The Dijkstra's algorithm for the many-to-many shortest path problem (m2mSPP)
# @Statement : The m2mSPP aims to find the shortest path from any source to any destination.
from numpy import inf
from pqdict import PQDict


def find_neighbors(network):
    # find the neighbors of each node
    neighbor = {}
    for i in network.keys():
        neighbor[i] = list(network[i].keys())
    return neighbor


def main(network, sources, destinations):
    """
    The main function
    :param network: {node1: {node2: length, node3: length, ...}, ...}
    :param sources: the source nodes
    :param destinations: the destination nodes
    :return:
    """
    # Step 1. Add dummy source and dummy destination
    source = 'dummy source'
    destination = 'dummy destination'
    network[source] = {}
    network[destination] = {}
    for s in sources:
        network[source][s] = 0
    for d in destinations:
        network[d][destination] = 0

    # Step 2. Initialization
    neighbor = find_neighbors(network)
    omega = []  # the list of explored labels
    queue = PQDict({})  # priority queue
    queue[source] = 0
    p_list = {source: [source]}  # path label

    # Step 3. The main loop
    while queue:

        # Step 3.1. Select the label with the minimum length
        (n1, length) = queue.popitem()
        path = p_list[n1]
        omega.append(n1)
        if n1 == destination:
            path.pop()
            path.pop(0)
            return {'path': path, 'length': length}

        # Step 3.2. Extend labels
        for n2 in neighbor[n1]:
            if n2 not in omega:
                temp_length = length + network[n1][n2]
                if temp_length < queue.get(n2, inf):
                    temp_path = path.copy()
                    temp_path.append(n2)
                    queue[n2] = temp_length
                    p_list[n2] = temp_path

    return {}
