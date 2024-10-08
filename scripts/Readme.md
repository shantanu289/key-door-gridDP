# ECE276B SP24 Project 1



## Overview
In this assignment, you are required to implement dynammic programming for the Door-Key problems.
<p align="center">
<img src="gif/doorkey.gif" alt="Door-key Problem" width="500"/></br>
</p>

There are 7 test scenes you have to test and include in the report.

|           doorkey-5x5-normal            |
| :-------------------------------------: |
| <img src="envs/known_envs/doorkey-5x5-normal.png"> |

|           doorkey-6x6-normal            |            doorkey-6x6-direct            |            doorkey-6x6-shortcut            |
| :-------------------------------------: | :--------------------------------------: | :----------------------------------------: |
| <img src="envs/known_envs/doorkey-6x6-normal.png"> | <img src="envs/known_envs/doorkey-6x6-direct.png" > | <img src="envs/known_envs/doorkey-6x6-shortcut.png" > |

|           doorkey-8x8-normal            |            doorkey-8x8-direct            |            doorkey-8x8-shortcut            |
| :-------------------------------------: | :--------------------------------------: | :----------------------------------------: |
| <img src="envs/known_envs/doorkey-8x8-normal.png"> | <img src="envs/known_envs/doorkey-8x8-direct.png" > | <img src="envs/known_envs/doorkey-8x8-shortcut.png" > |

## Installation

- Install Python version `3.8 ~ 3.10`
- Install dependencies
```bash
pip install -r requirements.txt
```

## Instruction
### 1. doorkey.py
You will need to modify **doorkey.py** as the main entrance.

### 2. utils.py
You might find some useful tools in utils.py
- **step()**: Move your agent
- **generate_random_env()**: Generate a random environment for debugging
- **load_env()**: Load the test environments
- **save_env()**: Save the environment for reproducing results
- **plot_env()**: For a quick visualization of your current env, including: agent, key, door, and the goal
- **draw_gif_from_seq()**: Draw and save a gif image from a given action sequence.

### 3. example.py
The example.py shows you how to interact with the utilities in utils.py, and also gives you some examples of interacting with gym-minigrid directly.


# Instructions to run the Code <br>
Ensure that **dputilsParta.py** and **dputilsPartb.py** are present in the same working directory at the same level as **doorkey.py**. 
Having installed all requirements, run **doorkey.py** by commenting out or uncommenting the appropriate line from 155-156 to run the desired part of the project. The output will be the Vcost, policies and GIFs stored in the appropriate folders. 
