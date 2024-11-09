import pygame

import settings


class MetaBoard:

    def __init__(self, rect: pygame.Rect):
        self.rect: pygame.Rect = rect
        self.boards: list[Board] = []

    def draw(self, screen: pygame.Surface, color: pygame.Color):
        pygame.draw.rect(screen, color, self.rect)

    def winner(self):
        for player in range(1, settings.NUM_PLAYERS + 1):
            vertical_left = (
                self.boards[0].winner() == player
                and self.boards[3].winner() == player
                and self.boards[6].winner() == player
            )
            vertical_middle = (
                self.boards[1].winner() == player
                and self.boards[4].winner() == player
                and self.boards[7].winner() == player
            )
            vertical_right = (
                self.boards[2].winner() == player
                and self.boards[5].winner() == player
                and self.boards[8].winner() == player
            )
            horizontal_top = (
                self.boards[0].winner() == player
                and self.boards[1].winner() == player
                and self.boards[2].winner() == player
            )
            horizontal_middle = (
                self.boards[3].winner() == player
                and self.boards[4].winner() == player
                and self.boards[5].winner() == player
            )
            horizontal_bottom = (
                self.boards[6].winner() == player
                and self.boards[7].winner() == player
                and self.boards[8].winner() == player
            )
            diagonal_topleft_bottomright = (
                self.boards[0].winner() == player
                and self.boards[4].winner() == player
                and self.boards[8].winner() == player
            )
            diagonal_topright_bottomleft = (
                self.boards[2].winner() == player
                and self.boards[4].winner() == player
                and self.boards[6].winner() == player
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


class Board:

    def __init__(self, rect: pygame.Rect):
        self.rect: pygame.Rect = rect
        self.tiles: list[Tile] = []

    def draw(self, screen: pygame.Surface, color: pygame.Color):
        pygame.draw.rect(screen, color, self.rect)

    def winner(self):
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
        self.rect: pygame.Rect = rect
        self.player: int = 0
        self.font: pygame.font.SysFont = pygame.font.SysFont("3270 Nerd Font Mono", 32)

    def draw(self, screen: pygame.Surface, color: pygame.Color):
        pygame.draw.rect(screen, color, self.rect)

        letter = settings.PLAYER_SYMBOLS[self.player]

        surf = self.font.render(letter, True, settings.COLOR_MARK)
        screen.blit(surf, (self.rect.centerx - 8, self.rect.centery - 18))
