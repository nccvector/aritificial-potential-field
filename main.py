import numpy as np 
from cv2 import cv2
import math

from classes.positional import Position
from classes.objects import *

# Main
if __name__ == '__main__':
    # Defining world dimensions
    world_size = (640, 480)
    # Initializing blank canvas with white color
    image = np.ones((world_size[1],world_size[0],3),dtype=np.uint8) * 255

    # Defining agent and goal
    agent = Agent(Position(50, 50), scan_radius=10, possible_moves=30)
    goal = Goal(Position(450, 450), sigma=math.sqrt(world_size[0]**2 + world_size[1]**2))

    # Defining obstacles in a list
    sigma_obstacles = 5
    obstacles = [Obstacle(Position(250, 180), sigma=sigma_obstacles, draw_radius=4*sigma_obstacles), 
                Obstacle(Position(250, 280), sigma=sigma_obstacles, draw_radius=4*sigma_obstacles),
                Obstacle(Position(250, 380), sigma=sigma_obstacles, draw_radius=4*sigma_obstacles), 
                Obstacle(Position(350, 180), sigma=sigma_obstacles, draw_radius=4*sigma_obstacles), 
                Obstacle(Position(350, 280), sigma=sigma_obstacles, draw_radius=4*sigma_obstacles), 
                Obstacle(Position(350, 380), sigma=sigma_obstacles, draw_radius=4*sigma_obstacles)]

    # Drawing objects
    agent.draw(image)
    goal.draw(image)
    for obstacle in obstacles:
        obstacle.draw(image)

    # Displaying initial frame and wait for intial key press
    cv2.imshow('Output', image)
    cv2.waitKey(1000)

    while Position.calculate_distance(agent.position, goal.position) > 10:
        possible_moves = agent.get_possible_moves()
        min_value = math.inf
        best_move = possible_moves[0] # initializing best move with first move
        # Finding move with the least value
        for move in possible_moves:
            move_value = goal.get_attraction_force(move)
            for obstacle in obstacles:
                move_value += obstacle.get_repulsion_force(move)

            if move_value < min_value:
                min_value = move_value
                best_move = move
        
        # Setting best move as agent's next position
        agent.position = best_move

        '''
        As we are not clearing up the initial frame at every iteration
        so we do not need to draw static objects again and again

        '''
        agent.draw(image)

        # Displaying updated frame
        cv2.imshow('Output', image)
        cv2.waitKey(20)
    
    # Hold on last frame
    cv2.waitKey(0)
        
        