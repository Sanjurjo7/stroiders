from random import choice

class Tile (object):
    """ This is the abstract representation of Tiles, the building blocks of the world."""

    def __init__ (self, stage, x, y):
        self.stage = stage
        self.x = x
        self.y = y

        "initializes the tile with a random type from the types list"
        self.tile_type = choice(self.stage.tile_types)

    def get_tile_location (self):
        "Returns a tile's x,y tuple for the tile."
        return (self.x, self.y)

    def set_tile_type (self, target_type):
        if target_type in self.stage.tile_types:
            self.tile_type = target_type
        else:
            print("Not a valid tile type.")
