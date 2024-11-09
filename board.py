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
        self.symbol = settings.TILE_EMPTY

    def draw(self, screen: pygame.Surface, color: pygame.Color):
        pygame.draw.rect(screen, color, self.rect)
        if self.symbol == settings.TILE_PLAYER_1:
            pygame.draw.line(
                screen,
                settings.COLOR_BOARD_4,
                (self.rect.left + 10, self.rect.top + 10),
                (self.rect.right - 10, self.rect.bottom - 10),
                4,
            )
            pygame.draw.line(
                screen,
                settings.COLOR_BOARD_4,
                (self.rect.right - 10, self.rect.top + 10),
                (self.rect.left + 10, self.rect.bottom - 10),
                4,
            )
        elif self.symbol == settings.TILE_PLAYER_2:
            pygame.draw.circle(
                screen,
                settings.COLOR_BOARD_4,
                (self.rect.centerx, self.rect.centery),
                (self.rect.width) / 4,
            )
