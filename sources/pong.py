import sys, pygame
from sources.settings import Settings
from sources.object import Objects

class PongGame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.objects = Objects()
        self.points_p1 = 0
        self.points_p2 = 0
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Pong")

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if (self.points_p1 == 8):
            print("Player 1 wins!")
            sys.exit()
        if (self.points_p2 == 8):
            print("Player 2 wins!")
            sys.exit()
    
    def _update_screen(self):
        pygame.display.flip()
        self.screen.blit(self.settings.bg_color, (0, 0))
        self.objects.sprite_group.draw(self.screen)
        pygame.draw.line(self.settings.bg_color, (255, 255, 255), (self.settings.screen_width/2, 0), (self.settings.screen_width/2, self.settings.screen_height), 10)
        self.objects.sprite_group.update(self)
        self.clock.tick(60)