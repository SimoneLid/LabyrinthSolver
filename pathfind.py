import math


def A_star(labyrinth,start,end,muro=1):
    '''
    Applica l'algoritmo di A* per trovare il percorso più veloce(senza diagonali) dall'inizio alla fine del labirinto(matrice)
    prendendo in input anche una codifica per riconoscere i muri
    '''
    visited_list=[[False for i in range(len(labyrinth))] for j in range(len(labyrinth))]
    open_list=[]
    closed_list=[]
    open_list.append([start,0,0,0])
    while open_list:
        open_list.sort(key=lambda x:x[3])
        curr_node=open_list[0]
        open_list.pop(0)
        closed_list.append(curr_node)
        if curr_node[0]==end:
            break
        children=get_children(curr_node[0],labyrinth,muro)
        for child in children:
            distance=math.sqrt(abs(child[0]-end[0])**2+abs(child[1]-end[1])**2)
            child=[child,curr_node[1]+1,distance,curr_node[1]+1+distance]
            if visited_list[child[0][0]][child[0][1]]:
                if child[1]<visited_list[child[0][0]][child[0][1]][0]:
                    visited_list[child[0][0]][child[0][1]]=child[1:]
            else:
                open_list.append(child)
                visited_list[child[0][0]][child[0][1]]=child[1:]
    path,resolved=backtrack_win(closed_list,end,labyrinth,muro,visited_list)
    return path,resolved



def get_children(position,labyrinth,muro):
    '''
    Genera le posizioni delle caselle adiacenti percorribili rispetto alla posizione in input
    '''
    directions=[[position[0],position[1]+1],[position[0],position[1]-1],[position[0]-1,position[1]],[position[0]+1,position[1]]]
    output=[]
    for dir in  directions:
        if dir[0]>=0 and dir[0]<len(labyrinth) and dir[1]>=0 and dir[1]<len(labyrinth[0]) and labyrinth[dir[0]][dir[1]]!=muro:
            output.append(dir)
    return output



def backtrack_win(closed_list,end,labyrinth,muro,visited_list):
    '''
    Data la closed list delle posizioni controllate fa backtracking dalla fine all'inizio
    per vedere il percorso migliore
    Nel caso in cui il labirinto non sia risolvibile ritorna la lista di caselle che si
    possono raggiungere dall'inizio
    '''
    if visited_list[end[0]][end[1]]==False:
        path=[node[0] for node in closed_list[1:]]
        return path,False
    curr_pos=[list(end)]+visited_list[end[0]][end[1]]
    path=[]
    while curr_pos[1]>1:
        children=get_children(curr_pos[0],labyrinth,muro)
        for child in children:
            if visited_list[child[0]][child[1]]:
                if visited_list[child[0]][child[1]][0]<curr_pos[1]:
                    child_pos=[child[0],child[1]]
                    curr_pos=[list(child_pos)]+visited_list[child[0]][child[1]]
        path.append(curr_pos[0])
    return path,True
