"""
Positional script

Contains:
    Position class

Author: Faizan Ali(nccvector)

"""

import math

# Position class for position based calculations
class Position:
    """
    Creates a position type object
        
    Arguments:
        x {double} -- x coordinate
        y {double} -- y coordinate

    Contains functions:
        calculate_distance(position_A, position_B)
        calculate_distance_squared(position_A, position_B)

    """

    def __init__(self, x, y):

        self.x = x
        self.y = y
    
    # General type function
    def calculate_distance(self, other):
        """
        Calculates distance between two positions
        
        Arguments:
            position_A {Position} -- position of first object
            position_B {Position} -- position of second object
        
        Returns:
            double -- distance between two positions

        """

        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    # General type function
    def calculate_distance_squared(self, other):
        """
        Calculates squared distance between two positions
        
        Arguments:
            position_A {Position} -- position of first object
            position_B {Position} -- position of second object
        
        Returns:
            double -- squared distance between two positions
            
        """

        return (self.x - other.x)**2 + (self.y - other.y)**2
