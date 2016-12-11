from Tile import Tile

class Stage(object):
    """ This is the abstract stage generation class. The stage is stored in the array called 'stage'. """
    # Calls for location should be made against this array using Tile's
    # getTileLocation() method.
    stage = []

    def __init__(self, width=100, height=100):
        for x in range(width):
            for y in range(height):
                tile = Tile(self, x, y)
                self.world.append(tile)
