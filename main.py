"""
Main script

Contains:
    draw function and __main__

Author: Faizan Ali(nccvector)

"""

import numpy as np 
from cv2 import cv2
import math

from positional import Position
from objects import *

# draw function
def draw(image, agent=None, goal=None, obstacles=None):
    """
    Draws passed objects on the image
    
    Arguments:
        image {numpy array (dtype=np.uint8)} -- numpy array of uint8 type
    
    Keyword Arguments:
        agent {Agent} -- Agent type object (default: {None})
        goal {Goal} -- Goal type object (default: {None})
        obstacles {Obstacle} -- Obstacle type object (default: {None})
    
    Returns:
        image {numpy array (dtype=np.uint8)} -- numpy array of uint8 type

    Note: You can draw objects optionally
    specify None in place of object you dont want to draw

    """

    # You can draw optionally
    if agent is not None:
        display = cv2.circle(image, (int(agent.position.x), int(agent.position.y)), agent.draw_radius, agent.draw_color, -1)  # Fill
    if goal is not None:
        display = cv2.circle(image, (int(goal.position.x), int(goal.position.y)), goal.draw_radius, goal.draw_color, -1)
    if obstacles is not None:
        for obstacle in obstacles:
            display = cv2.circle(image, (int(obstacle.position.x), int(obstacle.position.y)), obstacle.draw_radius, obstacle.draw_color, -1)
    
    return image


# Main
if __name__ == '__main__':
    # Defining world dimensions
    world_size = (640, 480)

    # Defining agent and goal
    agent = Agent(Position(50, 50), scan_radius=10, possible_moves=30)
    goal = Goal(Position(450, 450), sigma=world_size[0]*world_size[1])

    # Defining obstacles in a list
    sigma_obstacles = 5
    obstacles = [Obstacle(Position(250, 180), sigma=sigma_obstacles), 
                Obstacle(Position(250, 280), sigma=sigma_obstacles),
                Obstacle(Position(250, 380), sigma=sigma_obstacles), 
                Obstacle(Position(350, 180), sigma=sigma_obstacles), 
                Obstacle(Position(350, 280), sigma=sigma_obstacles), 
                Obstacle(Position(350, 380), sigma=sigma_obstacles)]

    # Initializing display with white background and objeccts with their own color
    display = draw(np.ones((world_size[1],world_size[0],3),dtype=np.uint8)*255, agent, goal, obstacles)

    # Displaying initial frame and wait for intial key press
    cv2.imshow('Output', display)
    cv2.waitKey(0)

    while Position.calculate_distance(agent.position, goal.position) > 10:
        possible_moves = agent.get_possible_moves()
        min_value = math.inf
        best_move = None
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
        display = draw(display, agent, None, None)

        # Displaying updated frame
        cv2.imshow('Output', display)
        cv2.waitKey(20)
    
    # Hold on last frame
    cv2.waitKey(0)
        
        