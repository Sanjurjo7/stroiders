from Tile import Tile
from random import choice

class Stage(object):
    """ This is the abstract stage generation class. The stage is stored in the array called 'stage'. """
    # Calls for location should be made against this array using Tile's
    # get_tile_location() method.
    tiles = []
    tile_list = ('empty', 'regolith', 'stone') 

    def __init__(self, width=100, height=100, scale=1):
        self.width = width
        self.height = height
        self.scale = scale
            
        for x in range(width):
            for y in range(height):
                tile = Tile(self, x*self.scale, y*self.scale)
                self.tiles.append(tile)

    def tile_types(self):
        tile_type = choice(self.tile_list)
        return tile_type

