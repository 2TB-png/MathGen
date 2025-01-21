import pygame

class Hitbox:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def update(self):
        pass

    def change_pos(self, x, y):
        pass

    def change_size(self, width, height):
        pass

    def is_pressed(self):
        pass

    def is_released(self, func, args=()):
        pass

    def is_activated(self, func, args=()):
        pass

    def on_press(self, func, args=()):
        pass

    def on_release(self, func, args=()):
        pass

    def on_activation(self, func, args=()):
        pass

    def set_debug(self, screen):
        pass
