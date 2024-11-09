import pygame

import settings


class Board:

    def __init__(self, rect: pygame.Rect):
        self.rect = rect
        self.tiles = []

    def draw(self, screen: pygame.Surface, color: pygame.Color):
        pygame.draw.rect(screen, color, self.rect)


class Tile:

    def __init__(self, rect: pygame.Rect):
        self.rect = rect
        self.player = 0
        self.font = pygame.font.SysFont("3270 Nerd Font Mono", 32)

    def draw(self, screen: pygame.Surface, color: pygame.Color):
        pygame.draw.rect(screen, color, self.rect)

        letter = settings.PLAYER_SYMBOLS[self.player]

        surf = self.font.render(letter, True, settings.COLOR_MARK)
        screen.blit(surf, (self.rect.centerx - 8, self.rect.centery - 18))
