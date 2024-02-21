# Flappy Bird AI

## Overview
This repository contains a Python project that implements an AI agent to play the Flappy Bird game. The project uses reinforcement learning, specifically Q-learning, to train the agent to navigate through pipes by learning the optimal actions based on the game's state.

The project is structured into several key components:
- `flappybird.py`: The main game logic for Flappy Bird, including rendering the game environment and defining the game dynamics.
- `agent.py`: Defines the AI agent, including the decision-making process using the trained model to determine when to jump.
- `model.py`: Contains the neural network model that approximates the Q-value function, trained to predict the expected rewards for different actions in given game states.
- `helper.py`: Utility functions that assist in the game's execution and the agent's learning process.

## Getting Started

### Prerequisites
Ensure you have Python 3.6+ installed on your system. Additionally, you will need the following packages:
- `pygame` for the game environment
- `numpy` for numerical computations
- `torch` for the neural network model

You can install these packages using pip:
pip install pygame numpy torch


### Running the Game
To start the game and observe the AI agent in action, run the `flappybird.py` script:
python flappybird.py


### Training the Model
The AI model can be trained by running the `agent.py` script. This process involves the agent playing the game multiple times, gradually improving its performance as it learns from its actions:
python agent.py

## How It Works

### Game Environment (`flappybird.py`)
The game environment simulates the Flappy Bird game, where the player controls a bird attempting to fly between columns of green pipes without hitting them.

### AI Agent (`agent.py`)
The AI agent uses a reinforcement learning model to decide when to jump to avoid obstacles. It learns from the game's state, which includes the bird's position, velocity, and the distance to the next obstacle.

### Neural Network Model (`model.py`)
The neural network model predicts the expected rewards for different actions in a given state. It uses this information to choose the action that maximizes the expected reward.

### Training Process
During training, the agent plays the game repeatedly, updating the model's weights based on the reward received for its actions. The goal is to maximize the score by avoiding obstacles for as long as possible.

## Contributing
Contributions to improve the project are welcome. This can include enhancements to the game's logic, the AI model, or the training process.
