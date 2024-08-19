from utils import *
from dputilsParta import *
from dputilsPartb import *
from example import example_use_of_gym_env

MF = 0  # Move Forward
TL = 1  # Turn Left
TR = 2  # Turn Right
PK = 3  # Pickup Key
UD = 4  # Unlock Door


def doorkey_problem(env,info):
    m = info["height"]
    n = info["width"]
    key_pos = info["key_pos"]
    goal_pos = info["goal_pos"]
    door_pos = info["door_pos"]
    start_pos = info["init_agent_pos"]
    start_dir = info["init_agent_dir"]
    if list(start_dir) == [1,0]:
        sd = 'R'
    elif list(start_dir) == [-1,0]:
        sd = 'L'
    elif list(start_dir) == [0,1]:
        sd = 'D'
    elif list(start_dir) == [0,-1]:
        sd = 'U'
    obs_list = info["obs_list"]    

    map_matrix = np.zeros((m,n)) 
    for i in range(m):        
        for j in range(n):
            if [j,i] in obs_list :
                map_matrix[i,j] = 1
      
    initial_state = [start_pos[1], start_pos[0], sd, 0, 1]
    all_states, parent_state_list, Vcost = buildDPEnvParta(map_matrix, [goal_pos[1],goal_pos[0]])
    parent_state_list = runDynamicProgramParta(map_matrix, all_states, Vcost, parent_state_list, [key_pos[1],key_pos[0]], [door_pos[1],door_pos[0]])
    path_ = getPathParta(all_states, parent_state_list, initial_state)
    actions_ = getActionsParta(path_)      
    """
    You are required to find the optimal path in
        doorkey-5x5-normal.env
        doorkey-6x6-normal.env
        doorkey-8x8-normal.env
        doorkey-6x6-direct.env
        doorkey-8x8-direct.env
        doorkey-6x6-shortcut.env
        doorkey-8x8-shortcut.env
    Feel Free to modify this fuction
    """
    print(actions_)
    print("----------------------------------------")
    # optim_act_seq = [TL, MF, PK, TL, UD, MF, MF, MF, MF, TR, MF]
    for i in range(len(actions_)):
        if actions_[i] == 'TL':
            actions_[i] = TL
        elif actions_[i] == 'MF':
            actions_[i] = MF
        elif actions_[i] == 'TR':
            actions_[i] = TR
        elif actions_[i] == 'PK':
            actions_[i] = PK
        elif actions_[i] == 'UD':
            actions_[i] = UD
    optim_act_seq = actions_       
    return optim_act_seq

def partBdp():   
   key_list = [[1,1],[3,2],[6,1]]
   goal_list = [[1,5],[3,6],[6,5]]
   door_1_loc = [2,4]
   door_2_loc = [5,4] 
   env_graph = np.array([[0,0,0,0,1,0,0,0], 
                         [0,0,0,0,1,0,0,0], 
                         [0,0,0,0,0,0,0,0], 
                         [0,0,0,0,1,0,0,0], 
                         [0,0,0,0,1,0,0,0], 
                         [0,0,0,0,0,0,0,0], 
                         [0,0,0,0,1,0,0,0], 
                         [0,0,0,0,1,0,0,0]])
   # The above info is known info
   # We're not using any info from the environment as of now
   all_states, parent_state_list, Vcost = buildDPEnv(env_graph, goal_list)
   parent_state_list = runDynamicProgram(env_graph, all_states, Vcost, parent_state_list, key_list, door_1_loc, door_2_loc)
   return all_states, parent_state_list, Vcost

def doorkey_problem_partb(env,info, all_states, parent_state_list, Vcost):
    #from the incoming info, make the initial state and query the path to goal     
    key_list = [[1,1],[2,3],[1,6]]
    goal_list = [[5,1],[6,3],[5,6]]    
    key_pos = info["key_pos"]
    goal_pos = info["goal_pos"]    
    door_open = info["door_open"]    
    start_pos = info["init_agent_pos"]
    start_dir = info["init_agent_dir"]
    if list(start_dir) == [1,0]:
        sd = 'R'
    elif list(start_dir) == [-1,0]:
        sd = 'L'
    elif list(start_dir) == [0,1]:
        sd = 'D'
    elif list(start_dir) == [0,-1]:
        sd = 'U'    
    door1stat = int(not door_open[0])
    door2stat = int(not door_open[1])
    key_ind = key_list.index(list(key_pos))
    goal_ind = goal_list.index(list(goal_pos))
    initial_state = [start_pos[1],start_pos[0],sd, 0, door1stat, door2stat, key_ind, goal_ind]
    vcost = Vcost[all_states.index(initial_state)]    
    print("Initial State = ", initial_state, " | Vcost = ", vcost)  

    path_ = getPath(all_states, parent_state_list, initial_state)
    actions_ = getActions(path_)           
       
    for i in range(len(actions_)):
        if actions_[i] == 'TL':
            actions_[i] = TL
        elif actions_[i] == 'MF':
            actions_[i] = MF
        elif actions_[i] == 'TR':
            actions_[i] = TR
        elif actions_[i] == 'PK':
            actions_[i] = PK
        elif actions_[i] == 'UD':
            actions_[i] = UD
    optim_act_seq = actions_
    # print(optim_act_seq)
    return optim_act_seq

def partA():
    lsp = ["doorkey-5x5-normal", "doorkey-6x6-normal", "doorkey-8x8-normal", "doorkey-6x6-direct", "doorkey-8x8-direct", "doorkey-6x6-shortcut", "doorkey-8x8-shortcut"]
    for i in lsp:
        print(i) 
        env_path = "./envs/known_envs/"+i+".env"
        env, info = load_env(env_path)  # load an environment    
        seq = doorkey_problem(env,info)  # find the optimal action sequence           
        draw_gif_from_seq(seq, load_env(env_path)[0], "./gif/Parta/"+i+".gif")  # draw a GIF & save


def partB():
    # run general dp without any info from the env
    all_states, parent_state_list, Vcost = partBdp()
    # import a random map and query the optimal path from the parent state list 
    env_folder = "./envs/random_envs"
    for i in range(36):
        env, info, env_path = load_random_env(env_folder,i)
        seq  = doorkey_problem_partb(env, info, all_states, parent_state_list, Vcost)
        draw_gif_from_seq(seq, load_env(env_path)[0],"./gif/Partb/Partb_"+str(i)+".gif")  # draw a GIF & save


if __name__ == "__main__":
    # example_use_of_gym_env()
    partA()
    # partB()

