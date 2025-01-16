import pygame
import json


with open("config.json", "r") as config_file:
    config = json.load(config_file)

    width = config["window"]["width"]
    height = config["window"]["height"]
    caption = config["window"]["caption"]

    for_devs = config["for_devs"]

    if for_devs["print_debug"]:
        print("[DEBUG]", config)


