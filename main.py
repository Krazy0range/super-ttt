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
        self.font_big = pygame.font.SysFont("3270 Nerd Font Mono", 24)
        self.font_bigger = pygame.font.SysFont("3270 Nerd Font Mono", 36)

        big_board_rect = pygame.Rect(
            settings.BOARD_PADDING,
            settings.BOARD_PADDING,
            settings.SCREEN_WIDTH / 2,
            settings.SCREEN_WIDTH / 2,
        )
        self.big_board = board.MetaBoard(big_board_rect)

        self.current_move_player = 1
        self.current_move_i = -1

        self.quit = False
        self.won = False
        self.god = True

    def _valid_move(self, i, j) -> bool:
        return (
            not self.won
            and (i == self.current_move_i or self.current_move_i == -1)
            and self.big_board.boards[i].tiles[j].player == 0
            and self.big_board.boards[i].winner() == 0
        ) or self.god

    def run(self):
        while not self.quit:
            self.update()
            self.render()

    def update(self):
        self.handle_events()

        if self.big_board.winner():
            self.won = True

    def render(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_tile_i, mouse_tile_j = -1, -1
        for i, mini_board in enumerate(self.big_board.boards):
            for j, tile in enumerate(mini_board.tiles):
                if tile.rect.collidepoint(mouse_x, mouse_y):
                    mouse_tile_i, mouse_tile_j = i, j

        self.screen.fill(settings.COLOR_BOARD_0)

        hints = []

        self.big_board.draw(self.screen, settings.COLOR_BOARD_1)

        for i, mini_board in enumerate(self.big_board.boards):

            if mini_board.winner():
                surf = self.font_bigger.render(
                    settings.PLAYER_SYMBOLS[mini_board.winner()],
                    True,
                    settings.COLOR_MARK,
                    settings.COLOR_BOARD_2,
                )
                pygame.draw.rect(self.screen, settings.COLOR_BOARD_2, mini_board.rect)
                self.screen.blit(
                    surf,
                    (
                        mini_board.rect.centerx - surf.get_rect().width / 2,
                        mini_board.rect.centery - surf.get_rect().height / 2,
                    ),
                )
                continue

            is_next_move = self._valid_move(mouse_tile_i, mouse_tile_j) and i == mouse_tile_j

            if self.won:
                mini_board.draw(self.screen, settings.COLOR_BOARD_2)
            elif i == self.current_move_i:
                mini_board.draw(self.screen, settings.COLOR_BOARD_4)
                if is_next_move:
                    hint_rect = mini_board.rect
            elif is_next_move:
                mini_board.draw(self.screen, settings.COLOR_BOARD_4)
                hints.append({"rect": mini_board.rect, "msg": "next move"})
            else:
                mini_board.draw(self.screen, settings.COLOR_BOARD_2)

            almost_winners = mini_board.almost_winners()

            for j, tile in enumerate(mini_board.tiles):

                if self.won:
                    tile.draw(self.screen, settings.COLOR_BOARD_3)
                elif i == mouse_tile_i and j == mouse_tile_j and self._valid_move(i, j):
                    tile.draw(self.screen, settings.COLOR_BOARD_1)
                elif j in [v for values in almost_winners.values() for v in values]:
                    tile.draw(self.screen, settings.COLOR_BOARD_ALERT_1)
                elif self.big_board.boards[j].winner():
                    tile.draw(self.screen, settings.COLOR_BOARD_ALERT_0)
                else:
                    tile.draw(self.screen, settings.COLOR_BOARD_3)

        for hint in hints:
            hint_rect = hint["rect"]
            surf = self.font.render(hint["msg"], True, settings.COLOR_BOARD_1, settings.COLOR_BOARD_4)
            x = (
                hint_rect.right
                if hint_rect.right + surf.get_rect().width <= self.big_board.rect.right
                else hint_rect.left - surf.get_rect().width
            )
            self.screen.blit(surf, (x, hint_rect.top))

        if not self.won:
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
        for i, mini_board in enumerate(self.big_board.boards):
            for j, tile in enumerate(mini_board.tiles):
                if tile.rect.collidepoint(mouse_x, mouse_y):
                    mouse_tile_i, mouse_tile_j, mouse_tile = i, j, tile

        if mouse_tile and self._valid_move(mouse_tile_i, mouse_tile_j):
            mouse_tile.set_player(self.current_move_player)
            if self.big_board.boards[mouse_tile_j].winner():
                self.current_move_i = -1
            else:
                self.current_move_i = mouse_tile_j
            self.current_move_player = 1 + (self.current_move_player % settings.NUM_PLAYERS)


if __name__ == "__main__":
    main = Main()
    main.run()
