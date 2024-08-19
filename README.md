# Key-Door Maze Dynamic Programming 
We navigate towards a goal location in a grid-world with obstacles, keys and doors(which are opened by keys) <br>
We solve this problem by Dynamic Programming. <br>
We tackle the situations where the key locations and door locations are known and unknown both. <br>
The Goal is to : <br>
Navigate to a given goal position from a start position taking the shortest possible path. <br>
The path may involve opening some doors which lead to the goal position. <br>
These doors may be open or need to be opened using a key. <br>
Thus, we need to find the shortest path to the goal including our travel to the key loaction. <br>
Catch : Keys can be present at multiple locations (more than one keys possible). We need to choose the right key and door location to obtain the optimal path to our goal.<br>
The allowed actions that we can take are : MF, TL, TR, PK, UD -> which correspond to "Move Forward", "Turn Left", "Turn Right", "Pick Key", "Unlock Door" respectively. <br>
PK can only be done while "facing" the key from a neighbouring grid cell. UD performed on an open door locks the door again. UD can only be performed "facing" the door from a neighbouring location and having the key. <br>
We solve this problem for a 5x5, 6x6, 7x7 and 8x8 environment.
