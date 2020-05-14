"""Module for project hyper parameters"""

BUFFER_SIZE = int(1e5)  # replay buffer size
BATCH_SIZE = 64         # minibatch size
GAMMA = 0.99            # discount factor
TAU = 1e-3              # for soft update of target parameters
LR = 5e-4               # learning rate 
UPDATE_EVERY = 4        # how often to update the network
NETWORK_LINEAR_SIZES = "1024,512,256" # dimension for every layer in Q network
BANANA_FILE_PATH = "./data/Banana.app"