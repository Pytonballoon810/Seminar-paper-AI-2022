"""learner module of "AI training python"

Returns:
    None
Exports:
    "dqn_weights.h5f.index" exports an index file for the calculated weights
"""
# My standard linting settings
# pylint: disable=trailing-whitespace
# pylint: disable=logging-fstring-interpolation
# pylint: disable=line-too-long

import random
import os
# Import the Sequential model from keras 
# as well as the flatten node to flatten out the 2-dimensional inputs and 
# dense nodes as the default tensorflow deep leaning node
from keras.models import Sequential
from keras.layers import Dense, Flatten # Flatten import unused for personal environment
from keras.optimizers import Adam

import pandas # for reading csv files

from gym import Env # for creating our own environment with gym
from gym.spaces import Discrete, Box

from rl.agents import DQNAgent # Multiple agents possible (see https://keras-rl.readthedocs.io/en/latest/) [DQN, NAF, DDPG, SARSA, CEM]
from rl.policy import BoltzmannGumbelQPolicy # Value or policy based reinforcement learning -> here: policy (BoltzmannGumbelQPolicy)
from rl.memory import SequentialMemory # To maintain memory

import numpy as np

#Custom imports:
import create_environments

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # fixing the "Could not load dynamic library 'cudnn64_8.dll'; dlerror: cudnn64_8.dll not found" error, but also disables the option to run from the GPU

# Possible to use one or multiple lines from the "training_data.csv"
TRAINING_DATA_FILE = create_environments.FILENAME
LINE_FROM_ENVIRONMENT_FILE = 1

# User specific configuration
TESTING = True # should the neural network be tested after it is finished with training?
SHOW_NET_STRUCT = True # prints out the net structure on initialization of the learning process
SAVE_WEIGHTS = True # should the weights be saved after the training is finished?
SAVE_WEIGHTS_AS = "dqn_weights.h5f" # if the weights are saved, this is the filename 

def point_in_rectangle(point:tuple[int, int], rect:tuple[int, int, int, int]) -> bool:
    """Global function/
    Calculate if point is in the area of a rectangle

    Args:
        point (tuple[int, int]): x, y of the point that is given
        rect (tuple[int, int, int, int]): x1, y1, x2, y2 of the rectangle to test for

    Returns:
        bool: true if point is inside, false if it is not inside
    """
    x, y = point
    x_1, y_1, x_2, y_2 = rect
    if (x_1 < x and x < x_2):
        if (y_1 < y and y < y_2):
            return True
    return False
        
def point_in_circle(point:tuple[int, int], circle:tuple[int, int, int]) -> bool:
    """Global function/
    Calculate if point is in the area of a circle

    Args:
        point (tuple[int, int]): x, y of the point that is given
        circle (tuple[int, int, int]): x1, y1, radius of the circle to test for

    Returns:
        bool: true if point is inside, false if it is not inside
    """
    x, y = point
    x_1, y_1, rad = circle
    if (x-x_1)**2 + (y-y_1)**2 < rad**2:
        return True
    return False

def calculate_aoe_hit(action_id:int, target:tuple[int, int]) -> bool:
    """Global function/
    Calculate if the action belonging to the action id would hit the target

    Args:
        action_id (int): action_id converted to an action with Move.moves[action_id]
        target (tuple[int, int]): the point trying to be hit

    Returns:
        bool: true if point is hit, false if it is not hit
    """
    action = Move.moves[action_id]
    square_moves = [Move.b_l, Move.b_r, Move.t_l, Move.t_r]
    if action in square_moves:
        return point_in_rectangle(target, Move.aoe[action])
    else:
        return point_in_circle(target, Move.aoe[Move.shockwave])

class Environment(Env):
    """Gym Env Inheritance of the object of the OpenAI gym environment

    Args:
        Env (gym.Env): inheriting the gym.Env properties
    """
    def __init__(self, player_pos:tuple[int, int]) -> None:
        """The constructor function for an custom Environment

        Args:
            player_pos (tuple[int, int]): the player position for which the environment is set up
        """
        # Inherit from Env
        super().__init__()
        # self.observation_space = Box(low=np.array(playfield_zeros, dtype=np.float32), high=np.array(playfield_max, dtype=np.float32), dtype=np.float32) # action array
        self.observation_space = Box(low=0, high=1, shape=(410, 410), dtype=np.uint8)
        self.action_space = Discrete(5) # actions we can take (Move.moves)
        # LEGACY: using indexed state variable
        # self.state = random.choice([Move.shockwave, Move.b_l, Move.b_r, Move.t_l, Move.t_r]) # set start action
        self.state = random.randint(0, 4)
        self.player_position = player_pos
        self.player_position_move = 10
        
    def step(self, action:int) -> tuple[int, int, bool, dict]:
        """overwriting the step function from the gym.Env class
        # would be possible to user super().__ini__() for perfect implementation, but is simply not required here

        Args:
            action (int): action index for the self.state variable

        Returns:
            tuple[int, int, bool, dict]: current state, reward (either -1 or 1), done (true when player movement was simulated 10 times)
        """
        # LEGACY: using indexed state variable
        # self.state = Move.moves[action]
        self.state = [[0 for x in range(410)] for y in range(410)]
        self.state[self.player_position[0]][self.player_position[1]] = 1
        self.player_position_move -= 1
        # print(self.state, self.player_position) # DEBUGGING
        # Add player move noise
        self.player_position = self.player_position[0]+random.randint(-self.player_position_move, self.player_position_move), self.player_position[1]+random.randint(-self.player_position_move, self.player_position_move)
        print(action)
        if calculate_aoe_hit(action, self.player_position):
            self.state = [[0 for x in range(410)] for y in range(410)]
            self.state[self.player_position[0]][self.player_position[1]] = 1
            reward = 1
        else:
            reward = -1
        if self.player_position_move <= 0:
            done = True
        else: 
            done = False
            
        info = {} # placeholder (required by OpenAI)
        
        return self.state, reward, done, info
        
    def render(self):
        """placeholder for a possible implementation with pygame or tkinter. Not done for time reasons and the non necessity
        """
        
    def reset(self) -> int:
        # Number of parameters was 3 in 'Env.reset' and is now 1 in overridden 'Environment.reset' method
        """called periodically after each iteration of the specified step amount

        Returns:
            int: current state to pass onto the next interval
        """
        # LEGACY: using indexed state variable
        # self.state = random.choice([Move.shockwave, Move.b_l, Move.b_r, Move.t_l, Move.t_r]) # set start action (same as above)
        self.state = random.randint(0, 4)
        self.player_position_move = 10 # Reset player move noise
        return self.state

#Dataclass
class Move():
    """dataclass for specifying the possible moves and packing them into lists and dictionaries
    @dataclass decorator not used since it would be overkill
    """
    shockwave = "shockwave"
    b_l = "bottom_left"
    b_r = "bottom_right"
    t_l = "top_left"
    t_r = "top_right"
    
    moves = [shockwave, b_l, b_r, t_l, t_r]
    
    aoe = {"bottom_left":(0, 0, 205, 205),        # define the area of effect to calculate if a non-perfect move would still succeed
           "bottom_right":(205, 0, 410, 205),      # point defined like (x_1, y_1, x_2, y_2)
           "top_left":(0, 205, 205, 410),
           "top_right":(205, 205, 410, 410),
           "shockwave":(205, 205, create_environments.RADIUS)}    # circle defined like (middle_x, middle_y, radius)

class Agent():
    """agent class used to build a custom agent object
    """
    def __init__(self) -> None:
        """self.env creates our custom environment for the specified x, y start position of the player.
        Also possible to iterate over them using a for loop, for utilizing the generated training_data in the training_data.csv
        """
        self.training_data = pandas.read_csv(TRAINING_DATA_FILE)
        
        self.env = Environment((254, 82))
        # print(self.env.step(4)) # DEBUGGING
            
            
    def build_model(self) -> Sequential: # actions:int
        """function for building a keras model

        Args:
            actions (int): amount of actions to build the model for (in this case 5)

        Returns:
            Sequential: returns the Sequential class of the model created by the keras module
        """
        states = self.env.observation_space.shape
        actions = self.env.action_space.n
        # print(states, actions) # DEBUGGING
        model = Sequential()
        # LEGACY: no need to flatten out the custom env with an input_shape before usage # TODO
        # model.add(Flatten(input_shape=states))
        model.add(Dense(8, activation="relu", input_shape=states)) # Dense node layer as standard keras neuron to generate deep reinforcement learning algorithms
        model.add(Dense(8, activation="relu"))
        model.add(Dense(8, activation="relu"))
        model.add(Dense(8, activation="relu"))
        model.add(Dense(8, activation="relu"))
        model.add(Dense(actions, activation="softmax"))
        model.summary()
        return model

    def build_agent(self, model:Sequential) -> DQNAgent:
        """function for building a keras model

        Args:
            model (Sequential): _description_

        Returns:
            DQNAgent: personal DQNAgent (see line 20 for more info "from rl.agents import DQNAgent")
        """
        actions = self.env.action_space.n # = 5
        policy = BoltzmannGumbelQPolicy()
        memory = SequentialMemory(limit=50_000, window_length=1)
        print(model.output_shape)
        dqn = DQNAgent(model=model, memory=memory, policy=policy, nb_actions=actions, nb_steps_warmup=20_000, target_model_update=1e-2)
        return dqn
            
            
if __name__ == "__main__":
    # All personal objects are labeled with the prefix "my_"
    my_agent = Agent()
    # LEGACY: env is created in the __init__ of Agent
    # env = agent.create_environment("(254, 82)","shockwave")
    my_model = my_agent.build_model()
    # my_model.summary()
    print("here")
    my_dqn = my_agent.build_agent(my_model)
    
    my_dqn.compile(Adam(learning_rate=0.01), metrics=["mae"]) # mae = mean absolute error
    my_dqn.fit(my_agent.env, nb_steps=50_000)
    if TESTING:
        scores = my_dqn.test(my_agent.env, nb_episodes=100, visualize=False) #nb_episodes = amount of testing episodes to run
        print(np.mean(scores.history["episode_reward"]))
    if SAVE_WEIGHTS:
        my_dqn.save_weights(SAVE_WEIGHTS_AS, overwrite=True)
        