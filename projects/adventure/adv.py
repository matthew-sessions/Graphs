from room import Room
from player import Player
from world import World
from move_graph import MoveGraph, NodeGraph

import random
from ast import literal_eval

from collections import deque


# Load world
world = World()

move_map = {'s':'n', 'n':'s', 'e':'w', 'w':'e'}
# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()


traversal_path = []

player = Player(world.starting_room)

# current_room = player.current_room
# movegraph = MoveGraph()
# movegraph.add_room(current_room)
# moves = movegraph.get_data(current_room)

nodegraph = NodeGraph()
nodegraph.load_node(room_graph)

# options = []
# for i in moves:
#     move = moves[i]
#     if '?' == move:
#         options.append(i)

# move_direction = random.choice(options)
# player.travel(move_direction)
# traversal_path.append(move_direction)
# movegraph.add_room(player.current_room)

# movegraph.update_direction(current_room, move_direction, player.current_room.id)

# movegraph.update_direction(player.current_room, move_map[move_direction], current_room.id)

# que = [current_room.id]
# print(que)
need_to_visit = [i for i in range(len(room_graph))]
tots = 0
while len(need_to_visit) > 0:
    tots += 1
    if tots < 2:
        print('here')
        target = random.choice(need_to_visit)
        path = nodegraph.dfs(player.current_room.id, target)
        for i in path[1:]:
            
            move = nodegraph.get_move(player.current_room.id, i)
            player.travel(move)
            #print('here')
            traversal_path.append(move)
            if i in need_to_visit:
                need_to_visit.remove(i)
    else:
        path = nodegraph.closest_unvisited(player.current_room.id, need_to_visit)
        for i in path[1:]:
            
            move = nodegraph.get_move(player.current_room.id, i)
            player.travel(move)
            #print('here')
            traversal_path.append(move)
            if i in need_to_visit:
                need_to_visit.remove(i)        

   
    # can_move = movegraph.get_data(player.current_room)
    # move_options = []
    # for i in can_move:
    #     move = can_move[i]
    #     if '?' == move:
    #         move_options.append(i)
    # if len(move_options) == 1:
    #     current_room = player.current_room
        
    #     move_direction = move_options[0]
    #     player.travel(move_direction)
    #     traversal_path.append(move_direction)
    #     movegraph.add_room(player.current_room)

    #     movegraph.update_direction(current_room, move_direction, player.current_room.id)

    #     movegraph.update_direction(player.current_room, move_map[move_direction], current_room.id) 
    #     if player.current_room.id in need_to_visit:
    #         need_to_visit.remove(player.current_room.id)


    # elif len(move_options) > 1:
        
    #     current_room = player.current_room
    #     que.append(current_room.id)
        
    #     move_direction = move_options[0]
    #     player.travel(move_direction)
    #     traversal_path.append(move_direction)
    #     movegraph.add_room(player.current_room)        
    #     movegraph.update_direction(current_room, move_direction, player.current_room.id)

    #     movegraph.update_direction(player.current_room, move_map[move_direction], current_room.id)
     
    #     if player.current_room.id in need_to_visit:
    #         need_to_visit.remove(player.current_room.id)        
    # else:
    #     print(que)
    #     target = que.pop()
    #     print(target)
    #     path = nodegraph.dfs(player.current_room.id, target)
    #     print(path)

    #     for i in path[1:]:
            
    #         move = nodegraph.get_move(player.current_room.id, i)
    #         player.travel(move)
    #         #print('here')
    #         traversal_path.append(move)
    #         if i in need_to_visit:
    #             need_to_visit.remove(i)
    #         if i in que:
    #             pass #que.remove(i)

#     # if there are more than options to move add a new array to que
#     if len(move_options) > 1:
#         current_room = player.current_room
#         que.append(qrray_que)
#         move_direction = random.choice(move_options)
#         player.travel(move_direction)
#         traversal_path.append(move_direction)
#         movegraph.add_room(player.current_room)

#         movegraph.update_direction(current_room, move_direction, player.current_room.id)

#         movegraph.update_direction(player.current_room, move_map[move_direction], current_room.id)    
#         que.append([move_direction])   
#         print('here') 
    

#     # if there are less than two options move and add to the last array
#     elif len(move_options) == 1:
#         current_room = player.current_room
#         move_direction = move_options[0]
#         player.travel(move_direction)
#         traversal_path.append(move_direction)
#         movegraph.add_room(player.current_room)

#         movegraph.update_direction(current_room, move_direction, player.current_room.id)

#         movegraph.update_direction(player.current_room, move_map[move_direction], current_room.id) 

#         qrray_que.append(move_direction)   
#         que.append(qrray_que)    
#         print('there')   


#     # if there are no valid moves pop the que and move back on the array
#     else:
#         for i in reversed(qrray_que):
#             current_room = player.current_room
#             move_direction = move_map[i]
#             player.travel(move_direction)
#             traversal_path.append(move_direction)
          



# print(movegraph.print_rooms())

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# traversal_path = []

# need_to_visit = [i for i in room_graph]

# nodes = NodeGraph()
# nodes.load_node(room_graph)

# movegraph = MoveGraph()

# que = []

# while len(need_to_visit) > 0:

#     all_moves = nodes.get_all_moves(player.current_room.id)
#     need_move = []
#     for i in all_moves:
#         if i in need_to_visit:
#             need_move.append(i)
#     if len(need_move) > 2:
#         move = need_move[0]
#         move_d = nodes.get_move(player.current_room.id, move)
#         print('here')
#         player.travel(move_d)
#         traversal_path.append(move)
#         if move in need_to_visit:
#             need_to_visit.remove(move)
#         for i in need_move[1:]:
#             if i not in que:
#                 que.append(i)

#     elif len(need_move) == 1:
        
#         move = need_move[0]
#         move_d = nodes.get_move(player.current_room.id, move)
#         player.travel(move_d)
#         traversal_path.append(move)
#         if move in need_to_visit:
#             need_to_visit.remove(move)
    
#     else:
#         current_room = player.current_room.id
        

#         if len(que) > 0:
#             target = que[-1]
#             que.remove(target)
#             path = nodes.dfs(current_room, target)
#             for i in path[1:]:
                
#                 move = nodes.get_move(player.current_room.id, i)
#                 player.travel(move)
#                 traversal_path.append(move)
#                 if move in need_to_visit:
#                     need_to_visit.remove(move)
#                 if move in que:
#                     que.remove(move)
#         else:

#             path = nodes.closest_unvisited(player.current_room.id, need_to_visit)
            
#             for i in path[1:]:
                
#                 move = nodes.get_move(player.current_room.id, i)
#                 player.travel(move)
#                 print('here')
#                 traversal_path.append(move)
#                 if i in need_to_visit:
#                     need_to_visit.remove(i)
#                 if i in que:
#                     que.remove(i)


print(traversal_path)



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
