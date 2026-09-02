import os
import sys

os.environ["SDL_VIDEODRIVER"] = "dummy"
sys.path.insert(0, "src")

import pygame
from game import CafeGame, MENU

pygame.init()
game = CafeGame()
assert game.state == "menu"
game.start_day()
assert game.state == "game"
assert game.customer is not None
expected = game.customer.order.name
game.serve(expected)
assert game.served == 1
assert game.money > 20
for _ in range(7):
    if game.state != "game":
        break
    game.serve(MENU[0].name)
assert game.state == "report"
game.running = False
pygame.quit()
print("smoke_test_ok")
