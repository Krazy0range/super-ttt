import pygame

import settings
import board


class Main:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("super-ttt")

        self.big_board = board.Board(self._rect_pad(self.screen_rect, settings.BOARD_PADDING))
        for i in range(9):
            rect = self._rect_grid(self.big_board.rect, settings.BOARD_PADDING, i)
            mini_board = board.Board(rect)
            for j in range(9):
                rect = self._rect_grid(mini_board.rect, settings.BOARD_PADDING, j)
                mini_board_tile = board.Tile(rect)
                mini_board.tiles.append(mini_board_tile)
            self.big_board.tiles.append(mini_board)

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

    def run(self):
        while not self.quit:
            self.update()
            self.render()

    def update(self):
        self.handle_events()

    def render(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        self.screen.fill(settings.COLOR_BOARD_0)

        self.big_board.draw(self.screen, settings.COLOR_BOARD_1)
        for mini_board in self.big_board.tiles:
            mini_board.draw(self.screen, settings.COLOR_BOARD_2)
            for tile in mini_board.tiles:
                if tile.rect.collidepoint(mouse_x, mouse_y):
                    tile.draw(self.screen, settings.COLOR_BOARD_1)
                else:
                    tile.draw(self.screen, settings.COLOR_BOARD_3)

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

        tile = None
        for t in self._get_all_tiles():
            if t.rect.collidepoint(mouse_x, mouse_y):
                tile = t

        if tile:
            tile.symbol += 1
            tile.symbol %= 3


if __name__ == "__main__":
    main = Main()
    main.run()
