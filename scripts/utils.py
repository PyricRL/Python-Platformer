import os
import pygame

BASE_IMAGE_PATH = 'data/images/'

# If its just a one image, itll just return that, but if its a directory, will return a list
def load_image(path):
    images = []

    if path.endswith('.png'):
        img = pygame.image.load(BASE_IMAGE_PATH + path).convert()
        img.set_colorkey((0, 0, 0))
        return img
    else:
        for img_name in sorted(os.listdir(BASE_IMAGE_PATH + path)):
            img = pygame.image.load(BASE_IMAGE_PATH + path + '/' + img_name).convert()
            img.set_colorkey((0, 0, 0))
            images.append(img)
        return images