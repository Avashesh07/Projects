import torch
import random
import numpy as np
from collections import deque
from flappybird import FlappyBirdAI, Point, BLOCK_SIZE
from model import Linear_QNet,QTrainer
from helper import plot

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.01

class Agent:

    def __init__(self):
        self.n_games = 0
        self.epsilon = 0
        self.gamma = 0.9
        self.memory = deque(maxlen=MAX_MEMORY)
        self.model = Linear_QNet(8,256,2)
        self.trainer = QTrainer(self.model, lr = LR, gamma= self.gamma)

    def get_state(self, game):
        # Vertical position of the bird relative to the next pipe opening
        bird_vertical_position = game.bird.y
        top_pipe_bottom_y = game.pipe['top_height']
        bottom_pipe_top_y = game.h - game.pipe['bottom_height']
        pipe_horizontal_distance = game.pipe['x'] - game.bird.x
        
        # Bird's vertical velocity
        bird_velocity = game.velocity
        
        # Whether the bird is in danger (too high or too low)
        danger_top = bird_vertical_position < top_pipe_bottom_y + BLOCK_SIZE  # Adjust BLOCK_SIZE as needed
        danger_bottom = bird_vertical_position > bottom_pipe_top_y - BLOCK_SIZE  # Adjust BLOCK_SIZE as needed
        danger_close = pipe_horizontal_distance < BLOCK_SIZE  # Adjust BLOCK_SIZE as needed
        
        state = [
            bird_vertical_position < top_pipe_bottom_y,  # Bird is below top pipe
            bird_vertical_position > bottom_pipe_top_y,  # Bird is above bottom pipe
            abs(bird_vertical_position - top_pipe_bottom_y),  # Distance to top pipe
            abs(bird_vertical_position - bottom_pipe_top_y),  # Distance to bottom pipe
            bird_velocity,  # Bird's vertical velocity
            pipe_horizontal_distance,  # Horizontal distance to the next pipe
            danger_top or danger_bottom,  # Immediate danger
            danger_close  # Danger due to being too close to the next pipe
        ]
        
        return np.array(state, dtype=int)

    
    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done)) # pop left if MAX_MEMORY is reached

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE) # list of tuples
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)

    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self,state):
        # random moves: tradeoff exploration / exploitation
        self.epsilon = 80 - self.n_games
        final_move = [0,0]
        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0, 1)
            final_move[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1

        return final_move


def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = FlappyBirdAI()
    while True:
        # get the current state
        state_old = agent.get_state(game)

        # get move
        final_move = agent.get_action(state_old)

        # perform move and get new state
        reward, done, score = game.play_step(final_move)
        state_new = agent.get_state(game)

        # train short memory
        agent.train_short_memory(state_old, final_move, reward, state_new, done)

        # remember
        agent.remember(state_old, final_move, reward, state_new, done)

        if done:
            # train long memory
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()
            
            if score > record:
               record = score
               agent.model.save()

            print('Game', agent.n_games, 'Score', score, 'Record:', record)

            plot_scores.append(score)
            total_score += score
            mean_score = total_score / agent.n_games
            plot_mean_scores.append(mean_score)
            plot(plot_scores,plot_mean_scores)


if __name__ == '__main__':
    train()
