import math

# Position class for position based calculations
class Position:
    """
    Creates a Position object
    
    Parameters
    ----------
    x : double
        x coordinate
    y : double
        y coordinate
        
    """

    def __init__(self, x, y):

        self.x = x
        self.y = y
    
    # General type function
    def calculate_distance(self, other):
        """
        Calculates distance between current position and the position passed as parameter
        It can also be usedd as static function by specifying class name and giving two parameters
        
        Parameters
        ----------
        other : Position
            Position to check distance against
        
        Returns
        -------
        double
            Distance value

        """

        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    # General type function
    def calculate_distance_squared(self, other):
        """
        Calculates squared distance between current position and the position passed as parameter
        It can also be usedd as static function by specifying class name and giving two parameters
        
        Parameters
        ----------
        other : Position
            Position to check squared distance against
        
        Returns
        -------
        double
            Distance value squared

        """

        return (self.x - other.x)**2 + (self.y - other.y)**2
