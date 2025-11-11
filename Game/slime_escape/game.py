import pgzrun
import random
import math
from pygame import Rect

WIDTH = 800
HEIGHT = 480

STATE_MENU = "menu"
STATE_PLAYING = "playing"
STATE_GAMEOVER = "gameover"
state = STATE_MENU

music_on = True

class AnimatedActor(Actor):
    def __init__(self, frames, pos, speed=0.15):
        super().__init__(frames[0], pos)
        self.frames = frames
        self.frame_index = 0
        self.speed = speed
        self.timer = 0

    def animate(self):
        self.timer += self.speed
        if self.timer >= 1:
            self.timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.image = self.frames[self.frame_index]

class Player(AnimatedActor):
    def __init__(self, pos):
        super().__init__(["slime_idle1", "slime_idle2"], pos)
        self.walk_frames = ["slime_walk1", "slime_walk2"]
        self.vy = 0
        self.on_ground = False

    def update(self):
        keys = keyboard
        moving = False

        if keys.left:
            self.x -= 3
            self.image = self.walk_frames[int(self.frame_index) % 2]
            self.flip_x = True
            moving = True
        elif keys.right:
            self.x += 3
            self.image = self.walk_frames[int(self.frame_index) % 2]
            self.flip_x = False
            moving = True

        if keys.space and self.on_ground:
            self.vy = -8
            sounds.jump.play()
            self.on_ground = False

        self.vy += 0.4
        self.y += self.vy

        if self.y > 400:
            self.y = 400
            self.vy = 0
            self.on_ground = True

        if not moving:
            self.animate()

class Enemy(AnimatedActor):
    def __init__(self, pos, left, right):
        super().__init__(["enemy1", "enemy2"], pos, 0.1)
        self.left = left
        self.right = right
        self.speed = 2

    def move(self):
        self.x += self.speed
        if self.x > self.right or self.x < self.left:
            self.speed *= -1
        self.animate()

player = Player((100, 400))
enemies = [
    Enemy((300, 400), 250, 400),
    Enemy((600, 400), 550, 700)
]
portal = Actor("portal", (750, 390))
background = Actor("bg", (400, 240))

buttons = {
    "start": Rect((320, 200), (160, 40)),
    "music": Rect((320, 260), (160, 40)),
    "exit": Rect((320, 320), (160, 40))
}

def start_game():
    global state
    state = STATE_PLAYING
    if music_on:
        music.play("bg_music")

def draw_menu():
    screen.blit("bg", (0, 0))
    screen.draw.text("SLIME ESCAPE", center=(400, 120), fontsize=60, color="white")
    for name, rect in buttons.items():
        screen.draw.filled_rect(rect, (0, 0, 0))
        screen.draw.text(name.upper(), center=rect.center, color="white")

def draw_game():
    background.draw()
    portal.draw()
    player.draw()
    for e in enemies:
        e.draw()

def draw_gameover():
    screen.fill("black")
    screen.draw.text("GAME OVER", center=(400, 200), fontsize=60, color="red")
    screen.draw.text("Press ENTER to return to menu", center=(400, 300), fontsize=30, color="white")

def update():
    global state
    if state == STATE_PLAYING:
        player.update()
        for e in enemies:
            e.move()
        for e in enemies:
            if player.colliderect(e):
                sounds.hit.play()
                state = STATE_GAMEOVER
        if player.colliderect(portal):
            state = STATE_GAMEOVER
    elif state == STATE_GAMEOVER:
        if keyboard.RETURN:
            reset_game()

def draw():
    if state == STATE_MENU:
        draw_menu()
    elif state == STATE_PLAYING:
        draw_game()
    elif state == STATE_GAMEOVER:
        draw_gameover()

def on_mouse_down(pos):
    global music_on
    if state == STATE_MENU:
        if buttons["start"].collidepoint(pos):
            start_game()
        elif buttons["music"].collidepoint(pos):
            music_on = not music_on
            if music_on:
                music.play("bg_music")
            else:
                music.stop()
        elif buttons["exit"].collidepoint(pos):
            exit()

def reset_game():
    global player, state
    player.x, player.y = 100, 400
    state = STATE_MENU

pgzrun.go()
