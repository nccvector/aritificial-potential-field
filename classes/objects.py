import math
from cv2 import cv2
from classes.positional import Position

# Agent class for Agent attributes
class Agent:
    """
    Creates an Agent object
    
    Parameters
    ----------
    position : Position
        Position of agent in world
    scan_radius : int, optional
        Step size of agent, by default 1
    possible_moves : int, optional
        Number of point generated around agent, by default 6
    draw_radius : int, optional
        Radius for visualization, by default 5
    draw_color : tuple, optional
        Color for visulization, by default (255,0,0)

    """

    def __init__(self, position, scan_radius=1, possible_moves=6, draw_radius=5, draw_color=(255,0,0)):
        
        # Property attributes
        self.position = position
        self._scan_radius = scan_radius
        self._possible_moves = possible_moves

        # Visual attributes
        self._draw_radius = draw_radius
        self._draw_color = draw_color

    def draw(self, image):
        cv2.circle(image, (int(self.position.x), int(self.position.y)), 
            self._draw_radius, self._draw_color, -1)  # Fill

    def get_possible_moves(self):
        """
        Makes a list of points around agent
        
        Returns
        -------
        list
            List of points around agent

        """

        angle_increment = (2*math.pi)/self._possible_moves # 2pi/n
        angle = -angle_increment # Going one step negative to start from zero
        possible_moves_list = []
        for _ in range(self._possible_moves):
            # Starting from angle 0
            angle += angle_increment
            possible_moves_list.append(Position(self._scan_radius * math.cos(angle) + self.position.x,
                                                self._scan_radius * math.sin(angle) + self.position.y))

        return possible_moves_list

# Obstacle class for repulsion based objects
class Obstacle:
    """
    Creates an Obstacle object
    
    Parameters
    ----------
    position : Position
        Position of Obstacle in the world
    mu : int, optional
        Peak of distribution, by default 1
    sigma : int, optional
        Spread of distribution, by default 1
    draw_radius : int, optional
        Radius for visualization, by default 5
    draw_color : tuple, optional
        Color for visualization, by default (0,0,255)
        
    """

    def __init__(self, position, mu=1, sigma=1, draw_radius=5, draw_color=(0,0,255)):

        # Property attributes
        self.position = position
        self._mu = mu
        self._sigma = sigma
        
        # Visual attributes
        self._draw_radius = draw_radius
        self._draw_color = draw_color

    def draw(self, image):
        cv2.circle(image, (int(self.position.x), int(self.position.y)), 
            self._draw_radius, self._draw_color, -1)  # Fill

    # Attribute type function
    def get_repulsion_force(self, position):
        """
        Repulsion force calculation function
        
        Parameters
        ----------
        position : Position
            Position of cell to check force at
        
        Returns
        -------
        double
            The value of repulsion at cell

        """

        # Implementing repulsion equation
        dist_value = (1/(self._sigma*math.sqrt(2*math.pi))) * math.exp(-(Position.calculate_distance_squared(self.position,position)/(2*self._sigma*self._sigma)))
        return dist_value

# Goal class for Goal object
class Goal:
    """
    Creates a Goal object
    
    Parameters
    ----------
    position : Position
        Position of Goal in the world
    mu : int, optional
        Peak of distribution, by default 1
    sigma : int, optional
        Spread of distribution, by default 1
    draw_radius : int, optional
        Radius for visualization, by default 5
    draw_color : tuple, optional
        Color for visualization, by default (0,255,0)
        
    """

    def __init__(self, position, mu=1, sigma=1, draw_radius=5, draw_color=(0,255,0)):

        # Property attributes
        self.position = position
        self._mu = mu
        self._sigma = sigma

        # Visual attributes
        self._draw_radius = draw_radius
        self._draw_color = draw_color

    def draw(self, image):
        cv2.circle(image, (int(self.position.x), int(self.position.y)), 
            self._draw_radius, self._draw_color, -1)  # Fill

    # Attribute type function
    def get_attraction_force(self, position):
        """
        Attraction force calculation function
        
        Parameters
        ----------
        position : Position
            Position of cell to check force at
        
        Returns
        -------
        double
            The value of attraction at cell

        """

        # Implementing attraction equation
        dist_value = -(1/(self._sigma*math.sqrt(2*math.pi))) * math.exp(-(Position.calculate_distance_squared(self.position,position)/(2*self._sigma*self._sigma)))
        return dist_value
