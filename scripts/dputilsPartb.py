import numpy as np
import random
## state : x, y, theta, key_status, door1 current, door2 current, key_loc_num, goal_loc_num
## state : 0, 1, 2----, 3---------, 4------------, 5------------, 6----------, 7-----------

def getNeighbours(s, key_list, door1_loc, door2_loc):
  key_loc = key_list[s[6]]
  key_neighbors = [[key_loc[0],key_loc[1]+1,'L',1], [key_loc[0],key_loc[1]-1,'R',1],[key_loc[0]+1,key_loc[1],'U',1],[key_loc[0]-1,key_loc[1],'D',1]]
  door1_neighbors = [[door1_loc[0],door1_loc[1]+1,'L'], [door1_loc[0],door1_loc[1]-1,'R'],[door1_loc[0]+1,door1_loc[1],'U'],[door1_loc[0]-1,door1_loc[1],'D']]
  door2_neighbors = [[door2_loc[0],door2_loc[1]+1,'L'], [door2_loc[0],door2_loc[1]-1,'R'],[door2_loc[0]+1,door2_loc[1],'U'],[door2_loc[0]-1,door2_loc[1],'D']]

  if s[0:4] in key_neighbors:
    # print('Key')
    sr = s[4:]
    if s[2]=='L':
      s1 = [s[0],s[1],'U',1]; s2 = [s[0],s[1],'D',1]; s3 = [s[0],s[1]+1,'L',1]; s4 = [s[0],s[1],'L',0]
    if s[2]=='R':
      s1 = [s[0],s[1],'U',1]; s2 = [s[0],s[1],'D',1]; s3 = [s[0],s[1]-1,'R',1]; s4 = [s[0],s[1],'R',0]
    if s[2]=='D':
      s1 = [s[0],s[1],'L',1]; s2 = [s[0],s[1],'R',1]; s3 = [s[0]-1,s[1],'D',1]; s4 = [s[0],s[1],'D',0]
    if s[2]=='U':
      s1 = [s[0],s[1],'L',1]; s2 = [s[0],s[1],'R',1]; s3 = [s[0]+1,s[1],'U',1]; s4 = [s[0],s[1],'U',0]
    ss = [s1+sr,s2+sr,s3+sr,s4+sr]
    return ss
  #----------------------------------------------------------------------------------------------------------

  if s[0:3] in door1_neighbors:
    # print('Door1')
    if s[3] == 0 :
      if s[2]=='L':
        s1 = [s[0],s[1],'U',0,s[4],s[5],s[6],s[7]]; s2 = [s[0],s[1],'D',0,s[4],s[5],s[6],s[7]]; s3 = [s[0],s[1]+1,'L',0,s[4],s[5],s[6],s[7]]
      if s[2]=='R':
        s1 = [s[0],s[1],'U',0,s[4],s[5],s[6],s[7]]; s2 = [s[0],s[1],'D',0,s[4],s[5],s[6],s[7]]; s3 = [s[0],s[1]-1,'R',0,s[4],s[5],s[6],s[7]]
      if s[2]=='D':
        s1 = [s[0],s[1],'L',0,s[4],s[5],s[6],s[7]]; s2 = [s[0],s[1],'R',0,s[4],s[5],s[6],s[7]]; s3 = [s[0]-1,s[1],'D',0,s[4],s[5],s[6],s[7]]
      if s[2]=='U':
        s1 = [s[0],s[1],'L',0,s[4],s[5],s[6],s[7]]; s2 = [s[0],s[1],'R',0,s[4],s[5],s[6],s[7]]; s3 = [s[0]+1,s[1],'U',0,s[4],s[5],s[6],s[7]]
      ss = [s1,s2,s3]
      return ss
    if s[3] == 1 :
      if s[2]=='L':
        s1 = [s[0],s[1],'U',1,s[4],s[5],s[6],s[7]]; s2 = [s[0],s[1],'D',1,s[4],s[5],s[6],s[7]]; s3 = [s[0],s[1]+1,'L',1,s[4],s[5],s[6],s[7]]; s4 = [s[0],s[1],'L',1,int(not s[4]),s[5],s[6],s[7]]
      if s[2]=='R':
        s1 = [s[0],s[1],'U',1,s[4],s[5],s[6],s[7]]; s2 = [s[0],s[1],'D',1,s[4],s[5],s[6],s[7]]; s3 = [s[0],s[1]-1,'R',1,s[4],s[5],s[6],s[7]]; s4 = [s[0],s[1],'R',1,int(not s[4]),s[5],s[6],s[7]]
      if s[2]=='D':
        s1 = [s[0],s[1],'L',1,s[4],s[5],s[6],s[7]]; s2 = [s[0],s[1],'R',1,s[4],s[5],s[6],s[7]]; s3 = [s[0]-1,s[1],'D',1,s[4],s[5],s[6],s[7]]; s4 = [s[0],s[1],'D',1,int(not s[4]),s[5],s[6],s[7]]
      if s[2]=='U':
        s1 = [s[0],s[1],'L',1,s[4],s[5],s[6],s[7]]; s2 = [s[0],s[1],'R',1,s[4],s[5],s[6],s[7]]; s3 = [s[0]+1,s[1],'U',1,s[4],s[5],s[6],s[7]]; s4 = [s[0],s[1],'U',1,int(not s[4]),s[5],s[6],s[7]]
      ss = [s1,s2,s3,s4]
      return ss
  #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  if s[0:3] in door2_neighbors:
    # print("Door2")
    if s[3] == 0 :
      if s[2]=='L':
        s1 = [s[0],s[1],'U',0,s[4],s[5],s[6],s[7]]; s2 = [s[0],s[1],'D',0,s[4],s[5],s[6],s[7]]; s3 = [s[0],s[1]+1,'L',0,s[4],s[5],s[6],s[7]]
      if s[2]=='R':
        s1 = [s[0],s[1],'U',0,s[4],s[5],s[6],s[7]]; s2 = [s[0],s[1],'D',0,s[4],s[5],s[6],s[7]]; s3 = [s[0],s[1]-1,'R',0,s[4],s[5],s[6],s[7]]
      if s[2]=='D':
        s1 = [s[0],s[1],'L',0,s[4],s[5],s[6],s[7]]; s2 = [s[0],s[1],'R',0,s[4],s[5],s[6],s[7]]; s3 = [s[0]-1,s[1],'D',0,s[4],s[5],s[6],s[7]]
      if s[2]=='U':
        s1 = [s[0],s[1],'L',0,s[4],s[5],s[6],s[7]]; s2 = [s[0],s[1],'R',0,s[4],s[5],s[6],s[7]]; s3 = [s[0]+1,s[1],'U',0,s[4],s[5],s[6],s[7]]
      ss = [s1,s2,s3]
      return ss
    if s[3] == 1 :
      if s[2]=='L':
        s1 = [s[0],s[1],'U',1,s[4],s[5],s[6],s[7]]; s2 = [s[0],s[1],'D',1,s[4],s[5],s[6],s[7]]; s3 = [s[0],s[1]+1,'L',1,s[4],s[5],s[6],s[7]]; s4 = [s[0],s[1],'L',1,s[4],int(not s[5]),s[6],s[7]]
      if s[2]=='R':
        s1 = [s[0],s[1],'U',1,s[4],s[5],s[6],s[7]]; s2 = [s[0],s[1],'D',1,s[4],s[5],s[6],s[7]]; s3 = [s[0],s[1]-1,'R',1,s[4],s[5],s[6],s[7]]; s4 = [s[0],s[1],'R',1,s[4],int(not s[5]),s[6],s[7]]
      if s[2]=='D':
        s1 = [s[0],s[1],'L',1,s[4],s[5],s[6],s[7]]; s2 = [s[0],s[1],'R',1,s[4],s[5],s[6],s[7]]; s3 = [s[0]-1,s[1],'D',1,s[4],s[5],s[6],s[7]]; s4 = [s[0],s[1],'D',1,s[4],int(not s[5]),s[6],s[7]]
      if s[2]=='U':
        s1 = [s[0],s[1],'L',1,s[4],s[5],s[6],s[7]]; s2 = [s[0],s[1],'R',1,s[4],s[5],s[6],s[7]]; s3 = [s[0]+1,s[1],'U',1,s[4],s[5],s[6],s[7]]; s4 = [s[0],s[1],'U',1,s[4],int(not s[5]),s[6],s[7]]
      ss = [s1,s2,s3,s4]
      return ss
  #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  if (s[0:2] == door1_loc and s[4]==1) or (s[0:2]==door2_loc and s[5]==1):
    return []
  if (s[0:2] == key_loc) and (s[3]==0):
    return []
  # print("Nowhere")
  if s[2] == 'L':
    s1 = [s[0],s[1],'D']; s2 = [s[0],s[1],'U']; s3 = [s[0],s[1]+1,'L']
  elif s[2] == 'R':
    s1 = [s[0],s[1],'D']; s2 = [s[0],s[1],'U']; s3 = [s[0],s[1]-1,'R']
  elif s[2] == 'D':
    s1 = [s[0],s[1],'L']; s2 = [s[0],s[1],'R']; s3 = [s[0]-1,s[1],'D']
  elif s[2] == 'U':
    s1 = [s[0],s[1],'L']; s2 = [s[0],s[1],'R']; s3 = [s[0]+1,s[1],'U']
  sr = s[3:]
  ss = [s1+sr,s2+sr,s3+sr]
  for s_ in ss:
    # print('h1')
    if (s_[0:2] == key_loc) and (s_[3] == 0) :
      # print('h2')
      ss.pop(ss.index(s_))
    elif (s_[0:2] == door1_loc) and (s[4]==1):
      # print('h3')
      ss.pop(ss.index(s_))
    elif (s_[0:2] == door2_loc) and (s[5]==1):
      # print('h4')
      ss.pop(ss.index(s_))
  return ss

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def runDynamicProgram(env_graph, all_states, Vcost, parent_state_list, key_list, door_1_loc,door_2_loc):
  parent_prev = []
  Vprev = []
  i = 0
  while (Vcost != Vprev):
    # parent_prev = parent_state_list.copy()
    Vprev = Vcost.copy()
    for s_ in all_states:
      if env_graph[s_[0],s_[1]] == 0:
        slist = getNeighbours(s_, key_list, door_1_loc, door_2_loc)
        # print(slist)
        for ss in slist:
          if (ss in all_states) and (env_graph[ss[0],ss[1]] == 0):
            vnew = Vcost[all_states.index(s_)] + 1
            if vnew < Vcost[all_states.index(ss)]:
              parent_state_list[all_states.index(ss)] = all_states.index(s_)
              Vcost[all_states.index(ss)] = vnew      
    i = i+1
    if i%1 == 0:
      print(i)
  return parent_state_list

def getPath(all_states, parent_state_list, initial_state):
  curr_node = initial_state
  path_list = [initial_state]
  while parent_state_list[all_states.index(curr_node)] != None:
    curr_node = all_states[parent_state_list[all_states.index(curr_node)]]
    path_list.append(curr_node)
  return path_list


def getActions(path_list):
  action_list = []
  for ind in range(len(path_list)-1) :
    x1, y1, d1, k1, do11, do21, key_l1, goal_l1 = path_list[ind]
    x2, y2, d2, k2, do12, do22, key_l2, goal_l2 = path_list[ind+1]
    if (x1 != x2) or (y1 != y2):
      action_list.append('MF')
    elif (d1 == d2) and (k1 == 0) and (k2 == 1):
      action_list.append('PK')
    elif (d1 == d2) and (do12 == int(not do11)):
      action_list.append('UD')
    elif (d1 == d2) and (do22 == int(not do21)):
      action_list.append('UD')
    elif (d1=='L' and d2=='U') or (d1=='U' and d2=='R') or (d1=='R' and d2=='D') or (d1=='D' and d2=='L') :
      action_list.append('TR')
    else:
      action_list.append('TL')
  return action_list

def buildDPEnv(env_graph, goal_list):
  all_states = []
  parent_state_list = []
  Vcost = []
  for i in range(env_graph.shape[0]):
    for j in range(env_graph.shape[1]):
      if env_graph[i,j] == 0:
        for dir in ['L','R','D','U']:
          for key_status in [0,1]:
            for door1 in [0,1]:
              for door2 in [0,1]:
                for key_l in [0,1,2]:
                  for goal_l in [0,1,2]:
                    state_ = [i,j,dir,key_status,door1,door2,key_l,goal_l]
                    all_states.append(state_)
                    if [i,j] == goal_list[goal_l]:
                      Vcost.append(0)
                      parent_state_list.append(None)
                    else:
                      Vcost.append(np.inf)
                      parent_state_list.append(None)
  return all_states, parent_state_list, Vcost


"""

env_graph = np.array([[0,0,0,0,1,0,0,0], [0,0,0,0,1,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,1,0,0,0], [0,0,0,0,1,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,1,0,0,0], [0,0,0,0,1,0,0,0]])

goal_list = [[1,5],[3,6],[6,5]]
key_list = [[1,1],[3,2],[6,1]]
door_1_loc = [2,4]
door_2_loc = [5,4]

all_states, parent_state_list, Vcost = buildDPEnv(env_graph, goal_list)
print(len(all_states))
parent_state_list = runDynamicProgram(env_graph, all_states, Vcost, parent_state_list, key_list, door_1_loc, door_2_loc)
list_of_paths = []
list_of_V = []
for d1 in [0,1]:
  for d2 in [0,1]:
    for kk in [0,1,2]:
      for gg in [0,1,2]:
        initial_state = [5,3,'U',0,d1,d2,kk,gg]
        path_ = getPath(all_states, parent_state_list,initial_state)
        actions_ = getActions(path_)
        list_of_paths.append(path_)
        list_of_V.append(Vcost[all_states.index(initial_state)])
        print("Initial State : ", initial_state, "V Cost : ", Vcost[all_states.index(initial_state)], "Actions : ", actions_)


path_list = getPath(all_states, parent_state_list, initial_state)
print(path_list)
print(Vcost[all_states.index(initial_state)])

print(env_graph)
# print(getNeighbours(initial_state,key_list, door_1_loc, door_2_loc))
# print(getNeighbours([3, 2, 'R', 1, 1, 1, 0, 0], key_list, door_1_loc, door_2_loc))
# print(getNeighbours([5, 2, 'R', 1, 0, 1, 0, 0], key_list, door_1_loc, door_2_loc))
"""