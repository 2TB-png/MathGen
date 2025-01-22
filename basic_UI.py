import pygame

class ButtonHitbox:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.debug_mode = False
        self.screen = None

        self.is_down = False
        self.was_down = False
        self.is_active = False

    def update(self, mouse):

        mouse = pygame.mouse


    def __handle_activation__(self, mouse):

        mouse_pos = mouse.get_pos()
        mouse_pressed = mouse.get_pressed()
        self.is_active = False

        if

        if not self.is_down and self.was_down:
            self.is_active =True

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

    def set_debug(self, screen, activate=True):
        self.debug_mode = activate
        self.screen = screen
