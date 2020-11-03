# polygon.py

import math

'''
TODO:
Objective 1 [pts:400]:
Create a Polygon Class:
where initializer takes in:
number of edges/vertices
circumradius
that can provide these properties:
# edges
# vertices
interior angle
edge length
apothem
area
perimeter
that has these functionalities:
a proper __repr__ function
implements equality (==) based on # vertices and circumradius (__eq__)
implements > based on number of vertices only (__gt__)
'''


class Polygon:
    """Simple polygon class for stricly convex polygons
    """

    def __init__(self, n: int, r: float) ->None:
        
        if not isinstance(n, int):
            raise ValueError(f'Number of sides n must be an integer and not {n}')        
        elif n < 3:
            raise ValueError('Number of sides must be greater than 2')
        elif r <= 0:
            raise ValueError('Minimum radius of circumcircle is 0')
        else:
            self.num_sides = n
            self.cir_radius = r

    @property
    def edges(self) -> str:
        "Returns Number of edges"
        return self.num_sides

    @property
    def vertices(self) -> str:
        "Returns number of vertices"
        return self.num_sides

    @property
    def interior_angle(self) -> float:
        "Returns Interior angle"
        return (self.num_sides-2)*180/self.num_sides

    @property
    def edge_length(self) -> float:
        """ Return Edge Length """
        return 2 * self.cir_radius * math.sin(math.pi/self.num_sides)

    @property
    def apothem(self) -> float:
        """ Returns Apothem """
        return self.cir_radius * math.cos(math.pi/self.num_sides)

    @property
    def area(self) -> float:
        """Return Area """
        return .5 * self.num_sides * self.apothem

    @property
    def perimeter(self) -> float:
        """ Return perimeter """
        return self.edge_length * self.num_sides

    def __repr__(self) -> str:
        return f"Polygon(sides={self.num_sides}, edge={round(self.edge_length, 3)}, circumradius={self.cir_radius}, area={round(self.area, 3)}, perimeter={round(self.perimeter, 3)})"

    def __eq__(self, other) -> bool:
        "Checks equality of two polygon objects using num_sides and circumradius"
        if not isinstance(other, Polygon):
            raise TypeError(f"{other} isn't a polygon")
        else:
            return self.vertices == other.vertices and self.cir_radius == other.cir_radius

    def __gt__(self, other) -> bool:
        "Checks greater of two polygon objects by num_sides "
        if not isinstance(other, Polygon):
            raise TypeError(f"{other} isn't a polygon")
        else:
            return self.vertices > other.vertices
