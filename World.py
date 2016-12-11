from Tile import Tile

class World(object):
    """ This is the abstract stage generation class. The stage is stored in the array called world. """
    # Calls for location should be made against this array using Tile's
    # getTileLocation() method.
    world = []

    def __init__(self, width=100, height=100):
        for x in range(width):
            for y in range(height):
                tile = Tile(self, x, y)
                self.world.append(tile)
