import math
import random
from pygame import Rect
from pgzero.builtins import Actor, keyboard

WIDTH = 800
HEIGHT = 600
TILE_SIZE = 40

# Estado inicial
sound_on = True
game_state = "menu"

# Botões do menu
start_button = Rect((WIDTH // 2 - 100, 200, 200, 50))
sound_button = Rect((WIDTH // 2 - 100, 300, 200, 50))
exit_button = Rect((WIDTH // 2 - 100, 400, 200, 50))

# Mapa do jogo
game_map = [
    "WWWWWWWWWWWWWWWWWW",
    "W........WW......W",
    "W.WWWW.WW.WWWW.W.W",
    "W.W...........W..W",
    "W.W.WW.WWW.WW.WW.W",
    "W...E....P....E..W",
    "WWWWWWWWWWWWWWWWWW",
]

# Herói
hero = Actor("hero_walk1")
hero.grid_x = 8
hero.grid_y = 5
hero.pos = (hero.grid_x * TILE_SIZE + TILE_SIZE // 2,
            hero.grid_y * TILE_SIZE + TILE_SIZE // 2)
hero_dir = (0, 0)
animation_frame = 0

# Objetos do mundo
dots = []
walls = []
enemies = []

class Enemy:
    def __init__(self, x, y):
        self.grid_x = x
        self.grid_y = y
        self.pos = (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2)
        self.actor = Actor("enemy_walk1", pos=self.pos)
        self.dir = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        self.animation_frame = 0

    def update(self):
        if self.at_grid_center():
            next_x = self.grid_x + self.dir[0]
            next_y = self.grid_y + self.dir[1]
            if not is_wall(next_x, next_y):
                self.grid_x = next_x
                self.grid_y = next_y
            else:
                self.dir = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

        target_pos = (self.grid_x * TILE_SIZE + TILE_SIZE // 2,
                      self.grid_y * TILE_SIZE + TILE_SIZE // 2)
        dx = target_pos[0] - self.actor.x
        dy = target_pos[1] - self.actor.y
        self.actor.x += dx * 0.2
        self.actor.y += dy * 0.2

        self.animation_frame = (self.animation_frame + 1) % 20
        self.actor.image = "enemy_walk1" if self.animation_frame < 10 else "enemy_walk2"

    def at_grid_center(self):
        return abs(self.actor.x - (self.grid_x * TILE_SIZE + TILE_SIZE // 2)) < 2 and \
               abs(self.actor.y - (self.grid_y * TILE_SIZE + TILE_SIZE // 2)) < 2

def create_world():
    for y, row in enumerate(game_map):
        for x, cell in enumerate(row):
            pos = (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2)
            if cell == "W":
                walls.append(Actor("wall", pos=pos))
            elif cell == ".":
                dots.append(Actor("dot", pos=pos))
            elif cell == "P":
                hero.grid_x = x
                hero.grid_y = y
                hero.pos = pos
                hero.x, hero.y = pos
            elif cell == "E":
                enemies.append(Enemy(x, y))

create_world()

def draw():
    screen.clear()

    if game_state == "menu":
        screen.fill((30, 30, 30))
        screen.draw.text("PACMAN LITE EDITION", center=(WIDTH//2, 100), fontsize=50, color="yellow")
        draw_button(start_button, "Start Game")
        draw_button(sound_button, f"Sound: {'On' if sound_on else 'Off'}")
        draw_button(exit_button, "Exit")

    elif game_state == "playing":
        for wall in walls:
            screen.draw.filled_rect(
                Rect((wall.x - TILE_SIZE // 2, wall.y - TILE_SIZE // 2),
                     (TILE_SIZE, TILE_SIZE)), "darkblue")

        for dot in dots:
            dot.draw()

        for enemy in enemies:
            enemy.actor.draw()

        hero.draw()

    elif game_state == "win":
        screen.draw.text("YOU WIN!", center=(WIDTH // 2, HEIGHT // 2),
                     fontsize=60, color="green")


    elif game_state == "game_over":
        screen.draw.text("GAME OVER", center=(WIDTH // 2, HEIGHT // 2),
                         fontsize=60, color="red")

def draw_button(rect, text):
    screen.draw.filled_rect(rect, (50, 50, 150))
    screen.draw.rect(rect, (255, 255, 255))
    screen.draw.text(text, center=rect.center, fontsize=30, color="white")

def update():
    global animation_frame, game_state

    if game_state == "playing":
        move_hero()
        collect_dots()

        for enemy in enemies:
            enemy.update()
            if hero.colliderect(enemy.actor):
                game_over()
                return

        animation_frame = (animation_frame + 1) % 20
        hero.image = "hero_walk1" if animation_frame < 10 else "hero_walk2"

def move_hero():
    if at_grid_center():
        next_x = hero.grid_x + hero_dir[0]
        next_y = hero.grid_y + hero_dir[1]
        if not is_wall(next_x, next_y):
            hero.grid_x = next_x
            hero.grid_y = next_y

    target_pos = (hero.grid_x * TILE_SIZE + TILE_SIZE // 2,
                  hero.grid_y * TILE_SIZE + TILE_SIZE // 2)
    dx = target_pos[0] - hero.x
    dy = target_pos[1] - hero.y
    hero.x += dx * 0.2
    hero.y += dy * 0.2

def at_grid_center():
    return abs(hero.x - (hero.grid_x * TILE_SIZE + TILE_SIZE // 2)) < 2 and \
           abs(hero.y - (hero.grid_y * TILE_SIZE + TILE_SIZE // 2)) < 2

def is_wall(x, y):
    if y < 0 or y >= len(game_map) or x < 0 or x >= len(game_map[y]):
        return True
    return game_map[y][x] == "W"

def check_win():
    global game_state
    if not dots and game_state == "playing":
        game_state = "win"
        clock.schedule(return_to_menu, 3.0)

def collect_dots():
    for dot in dots:
        if hero.colliderect(dot):
            dots.remove(dot)
            break
    check_win()

def on_key_down(key):
    global hero_dir
    if key == keys.UP:
        hero_dir = (0, -1)
    elif key == keys.DOWN:
        hero_dir = (0, 1)
    elif key == keys.LEFT:
        hero_dir = (-1, 0)
    elif key == keys.RIGHT:
        hero_dir = (1, 0)

def on_mouse_down(pos):
    global game_state, sound_on

    if game_state == "menu":
        if start_button.collidepoint(pos):
            game_state = "playing"
            if sound_on:
                music.play("background")
        elif sound_button.collidepoint(pos):
            sound_on = not sound_on
            if sound_on:
                music.play("background")
            else:
                music.stop()
        elif exit_button.collidepoint(pos):
            quit()


def game_over():
    global game_state
    game_state = "game_over"
    clock.schedule(return_to_menu, 2.0)




def return_to_menu():
    global game_state, dots, enemies, walls, hero_dir
    game_state = "menu"
    dots = []
    enemies = []
    walls = []
    hero_dir = (0, 0)
    create_world()
    music.stop()
