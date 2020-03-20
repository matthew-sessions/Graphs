from collections import deque
import random

class MoveGraph:
    def __init__(self):
        self.storage = {}
    def add_room(self, room):
        room_id = room.id
        roomdata = room.get_exits()
        exits = {}
        for i in roomdata:
            exits[i] = "?"
        self.storage[room_id] = exits
    def update_direction(self, room, direction, id):
        self.storage[room.id][direction] = id
    def get_data(self, room):
        room_id = room.id
        return self.storage[room_id]
    def print_rooms(self):
        print(self.storage)

data = {
    0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
    1: [(3, 6), {'s': 0, 'n': 2, 'e': 12, 'w': 15}],
    2: [(3, 7), {'s': 1}],
    3: [(4, 5), {'w': 0, 'e': 4}],
    4: [(5, 5), {'w': 3}],
    5: [(3, 4), {'n': 0, 's': 6}],
    6: [(3, 3), {'n': 5, 'w': 11}],
    7: [(2, 5), {'w': 8, 'e': 0}],
    8: [(1, 5), {'e': 7}],
    9: [(1, 4), {'n': 8, 's': 10}],
    10: [(1, 3), {'n': 9, 'e': 11}],
    11: [(2, 3), {'w': 10, 'e': 6}],
    12: [(4, 6), {'w': 1, 'e': 13}],
    13: [(5, 6), {'w': 12, 'n': 14}],
    14: [(5, 7), {'s': 13}],
    15: [(2, 6), {'e': 1, 'w': 16}],
    16: [(1, 6), {'n': 17, 'e': 15}],
    17: [(1, 7), {'s': 16}]
    }


class NodeGraph:
    def __init__(self):
        self.storage = {}
        self.dict = {}
    def load_node(self, data):
        for i in data:
            self.storage[i] = set()
            self.dict[i] = {v: k for k, v in data[i][1].items()}
            for a in data[i][1]:
                self.storage[i].add(data[i][1][a])
    def print_nodes(self):
        print(self.storage)
    def get_all_moves(self, id):
        return self.dict[id]

    def get_move(self, current_id, target_id):
        return self.dict[current_id][target_id]

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = deque()
        # Push the starting vertex
        s.append([starting_vertex])
        # Create a set()set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.__len__() > 0:
            # Pop the first vertex
            lastst = s.pop()
            v = lastst[-1]
            # Check if it's been visited
            # If it hasn't been visited...
            if v == destination_vertex:
                return(lastst)
            else:
                if v not in visited:
                    # Mark it as visited
                    
                    visited.add(v)
                    # Push all it's neighbors onto the stack
                    for neighbor in self.storage[v]:
                        temp = lastst.copy()
                        temp.append(neighbor)
                        s.append(temp)
    def closest_unvisited(self, starting_vertex, arr):

        dist = []
        for i in arr:
            dist.append(self.dfs(starting_vertex, i))
        overlap = -1
        shortest = None

        for i in dist:
            inter = set(arr) & set(i)
           
            
            if len(inter) / len(arr) > overlap:
                overlap = len(inter)/ len(arr)
                shortest = i
        
        return(shortest)
                         
a = NodeGraph()
a.load_node(data)
print(a.get_all_moves(0))


