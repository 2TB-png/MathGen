import pygame
import json
from sys import exit

#  import settings from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

    width = config["window"]["width"]
    height = config["window"]["height"]
    caption = config["window"]["caption"]

    bg = config["style"]["bg"]

    for_devs = config["for_devs"]

    if for_devs["print_debug"]:
        print("[DEBUG]", config)


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(caption)


def main():
    while True:

        # check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill(bg)

        pygame.display.update()


if __name__ == '__main__':
    main()
