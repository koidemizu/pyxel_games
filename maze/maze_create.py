# -*- coding: utf-8 -*-

import random
import numpy as np
import sys
 
sys.setrecursionlimit(10**6)
 
maze_width, maze_height = 21, 21
random_seed = 4
start_pos = (1, 1)
direction = [(0, -2), (0, 2), (-2, 0), (2, 0)]
 
maze_array = np.ones((maze_height, maze_width))
 
maze_array[start_pos] = 0 # 初期位置設定
        
 
def fn_create_maze(updX, updY):
    rnd_array = list(range(random_seed))
    random.shuffle(rnd_array)
    
    for index in rnd_array:
        if updY + direction[index][1] < 1 or updY + direction[index][1] > maze_height-1:
            continue
        elif updX + direction[index][0] < 1 or updX + direction[index][0] > maze_width-1:
            continue
        elif maze_array[updY+direction[index][1]][updX+direction[index][0]] == 0:
            continue
        else:
            pass
            
        maze_array[updY+direction[index][1]][updX+direction[index][0]] = 0
        if index == 0:
            maze_array[updY+direction[index][1]+1][updX+direction[index][0]] = 0
        elif index == 1:
            maze_array[updY+direction[index][1]-1][updX+direction[index][0]] = 0
        elif index == 2:
            maze_array[updY+direction[index][1]][updX+direction[index][0]+1] = 0
        elif index == 3:
            maze_array[updY+direction[index][1]][updX+direction[index][0]-1] = 0
        else:
            pass
        
        print(maze_array)        
        fn_create_maze(updX+direction[index][0], updY+direction[index][1])
 
 
if __name__ == '__main__':
    fn_create_maze(start_pos[0], start_pos[1])
    maze_array[start_pos] = 2
 
    print("result")
    print(maze_array)
