### The Dijkstra Algorithm for the Shortest Path Problem

##### Reference: Dijkstra E W. A note on two problems in connexion with graphs[M]//Edsger Wybe Dijkstra: His Life, Work, and Legacy. 2022: 287-290.

| Variables     | Meaning                                                      |
| ------------- | ------------------------------------------------------------ |
| network       | Dictionary, {node1: {node2: length, node3: length, ...}, ...} |
| source        | The source node                                              |
| destination   | The destination node                                         |
| nn            | The number of nodes                                          |
| neighbor      | Dictionary, {node1: [the neighbor nodes of node1], ...}      |
| dist          | List, the length label associated with each node             |
| path          | List, the path label associated with each node               |
| searched_node | List, the nodes that have already been searched              |
| queue         | The priority queue that output the label with the minimum length at each iteration |

#### Example

![image](https://github.com/Xavier-MaYiMing/The-Dijkstra-algorithm-for-the-shortest-path-problem/blob/main/SPP_example.png)

#### Dijkstra (one-to-one version)

```python
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
```

##### Output: 

```python
{'path': [0, 2, 4], 'length': 96}
```



#### Dijkstra (one-to-all version)

```python
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
```

##### Output: 

```python
{
    'path': [0, 2, 4], 
    'length': 96
}
```

