import pygame

import settings
import board


class Main:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("super-ttt")

        self.font = pygame.font.SysFont("3270 Nerd Font Mono", 20)
        self.font_big = pygame.font.SysFont("3270 Nerd Font Mono", 29)

        self.big_board = board.Board(self._rect_pad(self.screen_rect, settings.BOARD_PADDING))
        for i in range(9):
            rect = self._rect_grid(self.big_board.rect, settings.BOARD_PADDING, i)
            mini_board = board.Board(rect)
            for j in range(9):
                rect = self._rect_grid(mini_board.rect, settings.BOARD_PADDING, j)
                mini_board_tile = board.Tile(rect)
                mini_board.tiles.append(mini_board_tile)
            self.big_board.tiles.append(mini_board)

        self.current_move_player = 1
        self.current_move_i = -1

        self.quit = False

    def _rect_pad(self, rect: pygame.Rect, padding: int) -> pygame.Rect:
        return pygame.Rect(
            rect.left + padding,
            rect.top + padding,
            rect.width - padding * 2,
            rect.height - padding * 2,
        )

    def _rect_grid(self, big_rect: pygame.Rect, padding: int, i: int) -> pygame.Rect:
        return pygame.Rect(
            big_rect.left + (i % 3) * (big_rect.width - settings.BOARD_PADDING) / 3 + settings.BOARD_PADDING,
            big_rect.top + (i // 3) * (big_rect.height - settings.BOARD_PADDING) / 3 + settings.BOARD_PADDING,
            (big_rect.width - settings.BOARD_PADDING * 4) / 3,
            (big_rect.height - settings.BOARD_PADDING * 4) / 3,
        )

    def _get_all_tiles(self) -> list[board.Tile]:
        tiles = []
        for mini_board in self.big_board.tiles:
            for tile in mini_board.tiles:
                tiles.append(tile)
        return tiles

    def _right_tile_i(self, i) -> bool:
        return i == self.current_move_i or self.current_move_i == -1

    def _valid_move(self, i, j) -> bool:
        return self._right_tile_i(i) and self.big_board.tiles[i].tiles[j].player == 0

    def run(self):
        while not self.quit:
            self.update()
            self.render()

    def update(self):
        self.handle_events()

    def render(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_tile_i, mouse_tile_j = -1, -1
        for i, mini_board in enumerate(self.big_board.tiles):
            for j, tile in enumerate(mini_board.tiles):
                if tile.rect.collidepoint(mouse_x, mouse_y):
                    mouse_tile_i, mouse_tile_j = i, j

        self.screen.fill(settings.COLOR_BOARD_0)

        hint_rect = None

        self.big_board.draw(self.screen, settings.COLOR_BOARD_1)

        for i, mini_board in enumerate(self.big_board.tiles):

            is_next_move = self._valid_move(mouse_tile_i, mouse_tile_j) and i == mouse_tile_j

            if i == self.current_move_i:
                mini_board.draw(self.screen, settings.COLOR_BOARD_4)
                if is_next_move:
                    hint_rect = mini_board.rect
            elif is_next_move:
                mini_board.draw(self.screen, settings.COLOR_BOARD_4)
                hint_rect = mini_board.rect
            else:
                mini_board.draw(self.screen, settings.COLOR_BOARD_2)

            for j, tile in enumerate(mini_board.tiles):

                if self._right_tile_i(i) and i == mouse_tile_i and j == mouse_tile_j and tile.player == 0:
                    tile.draw(self.screen, settings.COLOR_BOARD_1)
                else:
                    tile.draw(self.screen, settings.COLOR_BOARD_3)

        if hint_rect:
            surf = self.font.render("next move", True, settings.COLOR_BOARD_2, settings.COLOR_BOARD_4)
            x = (
                hint_rect.right
                if hint_rect.right + surf.get_rect().width <= settings.SCREEN_WIDTH
                else hint_rect.left - surf.get_rect().width
            )
            self.screen.blit(surf, (x, hint_rect.top))

        surf = self.font_big.render(
            settings.PLAYER_SYMBOLS[self.current_move_player], True, settings.COLOR_BOARD_1, settings.COLOR_BOARD_4
        )
        rect = pygame.Rect(mouse_x, mouse_y, 32, 32)
        pygame.draw.rect(self.screen, settings.COLOR_BOARD_4, rect)
        self.screen.blit(surf, (mouse_x + 8, mouse_y))

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == pygame.KEYDOWN:
                self.handle_keypress(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.handle_click(event)

    def handle_keypress(self, event: pygame.event.Event):
        if event.key == pygame.K_q:
            self.quit = True

    def handle_click(self, event: pygame.event.Event):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        mouse_tile_i, mouse_tile_j, mouse_tile = -1, -1, None
        for i, mini_board in enumerate(self.big_board.tiles):
            for j, tile in enumerate(mini_board.tiles):
                if tile.rect.collidepoint(mouse_x, mouse_y):
                    mouse_tile_i, mouse_tile_j, mouse_tile = i, j, tile

        if mouse_tile and self._valid_move(mouse_tile_i, mouse_tile_j):
            mouse_tile.player = self.current_move_player
            self.current_move_i = mouse_tile_j
            self.current_move_player = 1 + (self.current_move_player % settings.NUM_PLAYERS)


if __name__ == "__main__":
    main = Main()
    main.run()
