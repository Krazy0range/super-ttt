import pygame

import settings


class Board:

    def __init__(self, rect: pygame.Rect):
        self.rect = rect
        self.tiles = []

    def draw(self, screen: pygame.Surface, color: pygame.Color):
        pygame.draw.rect(screen, color, self.rect)

    def winner_boards(self):
        for player in range(1, settings.NUM_PLAYERS + 1):
            vertical_left = (
                self.tiles[0].winner_tiles() == player
                and self.tiles[3].winner_tiles() == player
                and self.tiles[6].winner_tiles() == player
            )
            vertical_middle = (
                self.tiles[1].winner_tiles() == player
                and self.tiles[4].winner_tiles() == player
                and self.tiles[7].winner_tiles() == player
            )
            vertical_right = (
                self.tiles[2].winner_tiles() == player
                and self.tiles[5].winner_tiles() == player
                and self.tiles[8].winner_tiles() == player
            )
            horizontal_top = (
                self.tiles[0].winner_tiles() == player
                and self.tiles[1].winner_tiles() == player
                and self.tiles[2].winner_tiles() == player
            )
            horizontal_middle = (
                self.tiles[3].winner_tiles() == player
                and self.tiles[4].winner_tiles() == player
                and self.tiles[5].winner_tiles() == player
            )
            horizontal_bottom = (
                self.tiles[6].winner_tiles() == player
                and self.tiles[7].winner_tiles() == player
                and self.tiles[8].winner_tiles() == player
            )
            diagonal_topleft_bottomright = (
                self.tiles[0].winner_tiles() == player
                and self.tiles[4].winner_tiles() == player
                and self.tiles[8].winner_tiles() == player
            )
            diagonal_topright_bottomleft = (
                self.tiles[2].winner_tiles() == player
                and self.tiles[4].winner_tiles() == player
                and self.tiles[6].winner_tiles() == player
            )
            if (
                vertical_left
                or vertical_middle
                or vertical_right
                or horizontal_top
                or horizontal_middle
                or horizontal_bottom
                or diagonal_topleft_bottomright
                or diagonal_topright_bottomleft
            ):
                return player
        return None

    def winner_tiles(self):
        for player in range(1, settings.NUM_PLAYERS + 1):
            vertical_left = (
                self.tiles[0].player == player and self.tiles[3].player == player and self.tiles[6].player == player
            )
            vertical_middle = (
                self.tiles[1].player == player and self.tiles[4].player == player and self.tiles[7].player == player
            )
            vertical_right = (
                self.tiles[2].player == player and self.tiles[5].player == player and self.tiles[8].player == player
            )
            horizontal_top = (
                self.tiles[0].player == player and self.tiles[1].player == player and self.tiles[2].player == player
            )
            horizontal_middle = (
                self.tiles[3].player == player and self.tiles[4].player == player and self.tiles[5].player == player
            )
            horizontal_bottom = (
                self.tiles[6].player == player and self.tiles[7].player == player and self.tiles[8].player == player
            )
            diagonal_topleft_bottomright = (
                self.tiles[0].player == player and self.tiles[4].player == player and self.tiles[8].player == player
            )
            diagonal_topright_bottomleft = (
                self.tiles[2].player == player and self.tiles[4].player == player and self.tiles[6].player == player
            )
            if (
                vertical_left
                or vertical_middle
                or vertical_right
                or horizontal_top
                or horizontal_middle
                or horizontal_bottom
                or diagonal_topleft_bottomright
                or diagonal_topright_bottomleft
            ):
                return player
        return None


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
