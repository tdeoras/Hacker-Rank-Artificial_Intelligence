# https://www.hackerrank.com/challenges/saveprincess?hr_b=1
import numpy as np
import copy

def machine_pos(state,n):
    for i in range(n):
        for k in range(n):
            if state[i,k] == 109:
                return int(i),int(k)
            
def istarget(state,n,target):
    l1, l2 = machine_pos(state[0],n)
    m1 = target[0]
    m2 = target[1]
    if l1 + 1 == m1 and l2 == m2:
        return 1, state[1] + " DOWN"
    if l1 - 1 == m1 and l2 == m2:
        return 1, state[1] + " UP"
    if l1 == m1 and l2 + 1 == m2:
        return 1 , state[1] + " RIGHT"
    if l1 == m1 and l2 - 1 == m2:
        return 1 , state[1] + " LEFT"
    
    return 0, state[1]

def moves(state,n):
    moves = []
    t1, t2 = machine_pos(state[0],n)   
    loc = [t1, t2]
    if (loc[0] + 1) < n and loc[1] < n and state[0][loc[0] + 1,loc[1]] == 45:
        temp_grid = copy.deepcopy(state[0])
        mlog = copy.deepcopy(state[1])
        temp = temp_grid[(loc[0] + 1),(loc[1])]
        temp_grid[(loc[0] + 1),(loc[1])] = temp_grid[loc[0],loc[1]]
        temp_grid[loc[0],loc[1]] = temp
        mlog = mlog + " DOWN"
        moves.append([temp_grid,mlog])
    if (loc[0] - 1) < n and loc[1] < n and state[0][loc[0] - 1,loc[1]] == 45:
        temp_grid = copy.deepcopy(state[0])
        mlog = copy.deepcopy(state[1])
        temp = temp_grid[(loc[0] - 1),(loc[1])]
        temp_grid[(loc[0] - 1),(loc[1])] = temp_grid[loc[0],loc[1]]
        temp_grid[loc[0] ,loc[1]] = temp
        mlog = mlog + " UP"
        moves.append([temp_grid,mlog]) 
    if loc[0] < n and loc[1] + 1 < n and state[0][loc[0],loc[1] + 1] == 45:
        temp_grid = copy.deepcopy(state[0])
        mlog = copy.deepcopy(state[1])
        temp = temp_grid[(loc[0]),(loc[1] + 1)]
        temp_grid[(loc[0]),(loc[1] + 1)] = temp_grid[loc[0],loc[1]]
        temp_grid[loc[0],loc[1]] = temp
        mlog = mlog + " RIGHT"
        moves.append([temp_grid,mlog])
    if loc[0] < n and loc[1] - 1 < n and state[0][loc[0],loc[1] - 1] == 45:
        temp_grid = copy.deepcopy(state[0])
        mlog = copy.deepcopy(state[1])
        temp = temp_grid[(loc[0]),(loc[1] - 1)]
        temp_grid[(loc[0]),(loc[1] - 1)] = temp_grid[loc[0],loc[1]]
        temp_grid[loc[0],loc[1]] = temp
        mlog = mlog + " LEFT"
        moves.append([temp_grid,mlog])
    return moves
        

def solver(initial, target, n):
    fringe = []
    temp1 = copy.deepcopy(initial)
    fringe.append(temp1)
    while(len(fringe) > 0):
#        print (fringe)
#        print (moves(fringe[0],n))
        for elem in moves(fringe.pop(0),n):
            status, end = istarget(elem,n,target)
#            print (elem)
#            print (status)
#            print (end)
            if status == 1:
                return (end.strip().split())
            else:
                fringe.append(elem)
    


def displayPathtoPrincess(n,grid):
    n = int(n)
    tgrid = np.empty((n,n))
    for i in range(n):
        for k in range(n):
            tgrid[i,k] = int(ord(list(grid[i])[k]))
            if (int(ord(list(grid[i])[k]))) == 109:
                pos_machine = [i,k]
            if (int(ord(list(grid[i])[k]))) == 112:
                target = [i,k]    
            
    grid = tgrid
    initial = [grid,""]
    answer = solver(initial, target, n)
    for elem in answer:
        print (elem)
    
        
            
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())
    

displayPathtoPrincess(m,grid)
