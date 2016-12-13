import pygame
from pygame.locals import*
from Stage import Stage

class App:
    """This is the base app for runing a 2D version of the game using pygame. It is self initializing through Python3, but has not been packaged to run independently, yet. It creates the pygame screen, and the session, and currently controls the update (event, loop, render) cycle. It is separate from the logic code in as many ways as possible, and is intended as a display parameter only."""
    bg = 0

    def __init__(self):
        # Initializes the game and several necessaries. Changing the values here will alter the game's sizing and looks.
        self._running = True
        self.screen = None
        self.size = self.width, self.height = 640, 400
        self.scale = 8 
        self.stage = Stage(40,600,self.scale)

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.bg = pygame.image.load('assets/starsBKG.png')

    def tileImage(self, tileType):
        # TODO: Clean this up to Sprite loads
        tileName = 'assets/' + tileType + '.png'
        thisTile = pygame.image.load(tileName)
        return thisTile

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass
    def on_render(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.bg, (0,0))
        # FIXME: this needs to be Sprites
        for tile in self.stage.tiles:
            thisTile = self.tileImage(tile.tileType)
            self.screen.blit(thisTile, tile.getTileLocation())
        pygame.transform.scale(self.screen, (1280,720))
        pygame.display.flip()
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
