import pygame
from pygame.locals import*
from Stage import Stage

class App:
    bg = 0
    tileImage = 0

    def __init__(self):
        self._running = True
        self.screen = None
        self.size = self.width, self.height = 640, 400
        self.stage = Stage(64,40)
        self.scale = 10

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.bg = pygame.image.load('assets/starsBKG.png')
        self.tileImage = pygame.image.load('assets/tileSample.png')
        

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass
    def on_render(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.bg, (0,0))
        for tile in self.stage.stage:
            self.screen.blit(self.tileImage, tile.getTileLocation()*self.scale)
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
