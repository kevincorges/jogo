# menu.py
from pygame import Rect
from pgzero.builtins import Actor

WIDTH = 800
HEIGHT = 600

# Estados do jogo
game_state = "menu"  # "menu" ou "playing"

# Controle de som
sound_on = True

# Botões (retângulos para detectar cliques)
start_button = Rect((WIDTH // 2 - 100, 200, 200, 50))
sound_button = Rect((WIDTH // 2 - 100, 300, 200, 50))
exit_button = Rect((WIDTH // 2 - 100, 400, 200, 50))

def draw():
    screen.clear()

    if game_state == "menu":
        screen.fill((30, 30, 30))
        screen.draw.text("PACMAN-LIKE GAME", center=(WIDTH//2, 100), fontsize=50, color="yellow")

        draw_button(start_button, "Start Game")
        draw_button(sound_button, f"Sound: {'On' if sound_on else 'Off'}")
        draw_button(exit_button, "Exit")

    elif game_state == "playing":
        screen.clear()
        screen.draw.text("Game started!", center=(WIDTH//2, HEIGHT//2), fontsize=40, color="white")

def draw_button(rect, text):
    screen.draw.filled_rect(rect, (50, 50, 150))
    screen.draw.rect(rect, (255, 255, 255))
    screen.draw.text(text, center=rect.center, fontsize=30, color="white")

def on_mouse_down(pos):
    global game_state, sound_on

    if game_state == "menu":
        if start_button.collidepoint(pos):
            game_state = "playing"
        elif sound_button.collidepoint(pos):
            sound_on = not sound_on
        elif exit_button.collidepoint(pos):
            quit()

