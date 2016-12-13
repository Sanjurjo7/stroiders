import pygame
from pygame.locals import*
from Stage import Stage

class App:
    bg = 0

    def __init__(self):
        self._running = True
        self.screen = None
        self.size = self.width, self.height = 640, 400
        self.scale = 8
        self.stage = Stage(40,600,8)

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
