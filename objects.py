"""
Objects script

Contains:
    object classes: Agent, Obstacle and Goal

Author: Faizan Ali(nccvector)

"""

import math
from positional import Position

# Agent class for Agent attributes
class Agent:
    """
    Creates an Agent object
        
    Arguments:
        position {Position} -- position of agent in the world
    
    Keyword Arguments:
        scan_radius {int} -- step size (default: {1})
        possible_moves {int} -- number of points generated around agent (default: {6})
        draw_radius {int} -- radius for visualization (default: {5})
        draw_color {tuple} -- color for visualization (default: {(255,0,0)})

    Contains function:
        get_possible_moves(self)

    """

    def __init__(self, position, scan_radius=1, possible_moves=6, draw_radius=5, draw_color=(255,0,0)):
        
        # Property attributes
        self.position = position
        self.scan_radius = scan_radius
        self.possible_moves = possible_moves

        # Visual attributes
        self.draw_radius = draw_radius
        self.draw_color = draw_color

    def get_possible_moves(self):
        """
        Makes a list of points around the agent
        
        Returns:
            List -- list of the points around agent

        """

        angle_increment = (2*math.pi)/self.possible_moves # 2pi/n
        angle = -angle_increment # Going one step negative to start from zero
        possible_moves_list = []
        for _ in range(self.possible_moves):
            # Starting from angle 0
            angle += angle_increment
            possible_moves_list.append(Position(self.scan_radius * math.cos(angle) + self.position.x,
                                                self.scan_radius * math.sin(angle) + self.position.y))

        return possible_moves_list

# Obstacle class for repulsion based objects
class Obstacle:
    """
    Creates an Obstacle object
        
    Arguments:
        position {Position} -- position of the goal in world
    
    Keyword Arguments:
        mu {int} -- peak of distribution (default: {1})
        sigma {int} -- spread of distribution (default: {1})
        draw_radius {int} -- radius for visualization (default: {5})
        draw_color {tuple} -- color for visualization (default: {(0,255,0)})

    Contains function:
        get_repulsion_force(self, position)

    """

    def __init__(self, position, mu=1, sigma=1, draw_radius=5, draw_color=(0,0,255)):

        # Property attributes
        self.position = position
        self.mu = mu
        self.sigma = sigma
        
        # Visual attributes
        self.draw_radius = draw_radius
        self.draw_color = draw_color

    # Attribute type function
    def get_repulsion_force(self, position):
        """
        Repulsion force calculation function
        
        Arguments:
            position {Position} -- position of the cell to check force at
        
        Returns:
            double -- the value of repulsion at cell

        """

        # Implementing repulsion equation
        dist_value = (1/(self.sigma*math.sqrt(2*math.pi))) * math.exp(-(Position.calculate_distance_squared(self.position,position)/(2*self.sigma*self.sigma)))
        return dist_value

# Goal class for Goal object
class Goal:
    """
    Creates a Goal object
        
    Arguments:
        position {Position} -- position of the goal in world
    
    Keyword Arguments:
        mu {int} -- peak of distribution (default: {1})
        sigma {int} -- spread of distribution (default: {1})
        draw_radius {int} -- radius for visualization (default: {5})
        draw_color {tuple} -- color for visualization (default: {(0,255,0)})

    Contains function:
        get_attraction_force(self, position)

    """

    def __init__(self, position, mu=1, sigma=1, draw_radius=5, draw_color=(0,255,0)):

        # Property attributes
        self.position = position
        self.mu = mu
        self.sigma = sigma

        # Visual attributes
        self.draw_radius = draw_radius
        self.draw_color = draw_color

    # Attribute type function
    def get_attraction_force(self, position):
        """
        Attraction force calculation function
        
        Arguments:
            position {Position} -- position of the cell to check force at
        
        Returns:
            double -- the value of attraction at cell

        """

        # Implementing attraction equation
        dist_value = -(1/(self.sigma*math.sqrt(2*math.pi))) * math.exp(-(Position.calculate_distance_squared(self.position,position)/(2*self.sigma*self.sigma)))
        return dist_value
