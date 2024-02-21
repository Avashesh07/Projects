import pygame
import random
from collections import namedtuple
import numpy as np

pygame.init()
font = pygame.font.Font(None, 25)

Point = namedtuple('Point', 'x, y')

# rgb colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

BLOCK_SIZE = 50
SPEED = 30

class FlappyBirdAI:
    
    def __init__(self, w=400, h=600):
        self.w = w
        self.h = h
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Flappy Bird')
        self.clock = pygame.time.Clock()
        
        self.bird = Point(self.w // 3, self.h // 2)
        self.velocity = 0
        self.gravity = 0.7
        self.pipe = self._generate_pipe()
        self.score = 0
        self.game_over = False

    def _generate_pipe(self):
        pipe_height = random.randint(150, 450)
        return {'x': self.w, 'top_height': pipe_height, 'bottom_height': self.h - pipe_height - 100}

    def play_step(self, action):
        # 1. collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        self._move(action) 

        # 2. move bird and pipes
        self.velocity += self.gravity
        self.bird = Point(self.bird.x, self.bird.y + self.velocity)
        self.pipe['x'] -= 5
        
        # 3. check if game over
        reward = 0
        collision_info = self.is_collision()
        if collision_info['collision']:
            self.game_over = True
            reward = collision_info['penalty']  # Use the penalty as the reward
            return reward, self.game_over, self.score
            
        # 4. check for score
        if not self.game_over and self.pipe['x'] < self.bird.x:
            self.score += 1
            self.pipe = self._generate_pipe()
            reward = 10

        # 5. update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)
        
        return reward, self.game_over, self.score

    def is_collision(self, pt=None):
        if pt is None:
            pt = self.bird
        
        # Define different collision types with corresponding penalties
        collision_type = {'collision': False, 'penalty': 0}
        
        # hits the top or bottom of the screen
        if pt.y < 0 or pt.y > self.h - BLOCK_SIZE + 10:
            collision_type['collision'] = True
            collision_type['penalty'] = -100  # More severe penalty for hitting screen boundaries
        
        # hits the pipes closer to the gap
        elif self.pipe['x'] - BLOCK_SIZE/2 + 5 <= pt.x < self.pipe['x'] + BLOCK_SIZE - 10:
            if pt.y < self.pipe['top_height'] or pt.y > self.pipe['top_height'] + 100:
                collision_type['collision'] = True
                collision_type['penalty'] = -50  # Less severe penalty for hitting near the gap
        
        
        return collision_type
    
    def _move(self, action):
            
        if np.array_equal(action, [1, 0]):
            self.velocity = -10  # Flap
        elif np.array_equal(action, [0, 1]):
            pass

    def _update_ui(self):
        self.display.fill(WHITE)
    
        # Draw bird
        pygame.draw.rect(self.display, GREEN, pygame.Rect(self.bird.x, self.bird.y, BLOCK_SIZE-10, BLOCK_SIZE-10)) 
        # Draw pipes
        pygame.draw.rect(self.display, BLACK, pygame.Rect(self.pipe['x'], 0, BLOCK_SIZE, self.pipe['top_height']))
        pygame.draw.rect(self.display, BLACK, pygame.Rect(self.pipe['x'], self.h - self.pipe['bottom_height'], BLOCK_SIZE, self.pipe['bottom_height']))
        
        # Render the score
        score_surface = font.render(f'Score: {self.score}', True, BLACK)
        self.display.blit(score_surface, (self.w - 120, 10))
        
        # Update the display
        pygame.display.flip()

    def reset(self):

        self.bird = Point(self.w // 3, self.h // 2)
        self.velocity = 0
        self.gravity = 0.7
        self.pipe = self._generate_pipe()
        self.score = 0
        self.game_over = False