import pygame

class Spritesheet (object):

    sheet_map = {
        'empty':(24,24,8,8),
        'regolith':(16,0,8,8),
        'stone':(24,8,8,8),
        'platinum':(0,0,8,8)
    }

    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error:
            print('Unable to load spritesheet image: ' + filename + '.')
            raise

    def image_by_type(self, tile_type, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(self.sheet_map[tile_type])
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0,0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list

    def images_tile_list(self, tile_types, colorkey = None):
        "Loads multiple images, supply a list of coordinates"
        return [self.image_by_type(tile_type, colorkey) for tile_type in tile_types]

    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)

