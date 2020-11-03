from polygon import Polygon
from numbers import Real
import typing


class PolygonSequence():
    """Generates a sequence of Polygon Objects with given max number of vertices and common \
        circumscribing radius.
        It also implents:
        indexing and slicing within the sequence,
        finding and returning max efficinecy polygon from the sequence.
        
    """

    def __init__(self, num_vertices: int, cir_radius: Real) -> None:
        self.polygons = [Polygon(i, cir_radius)
                         for i in range(3, num_vertices+1)]
        self._num_vertices = num_vertices
        self._cir_radius = cir_radius

    def __len__(self) -> int:
        """Returns the max. number of sides from the sequence."""
        return self._num_vertices

    def __repr__(self) -> str:
        return f'PolygonSequence(max_vertices={self._num_vertices}, \
circumradius={self._cir_radius}) has actual {len(self.polygons)} \
polygons in the lot'

    def __getitem__(self, s: typing.Union[int, slice]) -> typing.Union[Polygon, list]:
        if isinstance(s, int):
            if s-3 > self._num_vertices or 3-s < -self._num_vertices:
                return IndexError
            else:
                return self.polygons[s]

        elif isinstance(s, slice):
            start, stop, step = s.indices(self._num_vertices)
            return [self.polygons[i] for i in range(start, stop, step)]
        else:
            raise ValueError(f'Invalid input {s}')

    @property
    def max_eff_polygon(self):
        "Returns polygon with max. efficiency ie highest area to perimeter ratio."
        return sorted(self.polygons, 
                      key=lambda x: x.area/x.perimeter,
                      reverse=True)[0]
