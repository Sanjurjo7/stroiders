from random import choice

class Tile (object):
    """ This is the abstract representation of Tiles, the building blocks of the world."""

    tileTypes = ('Empty', 'Floor', 'Wall')

    def __init__ (self, stage, x, y):
        self.stage = stage
        self.x = x
        self.y = y

        # initializes the tile with a random type from the types list
        self.tileType = choice(self.tileTypes)

    def getTileLocation (self):
        return [self.x, self.y]

    def setTileType (self):
        return
