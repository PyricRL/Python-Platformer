import os
import pygame

BASE_IMAGE_PATH = 'data/images/'

def load_image(path):
    img = pygame.image.load(BASE_IMAGE_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

# Maybe work on func which can load all folders for data instead of one each
# pretty much just use os.listdir to pull all folders and go in each folder and do it
def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMAGE_PATH + path)):
        images.append(load_image(path + '/' + img_name))
    return images

# use this but take path function here and just combine the 2 upper functions into this one
def load_images1():
    images = []
    for root, dir, files in os.walk(BASE_IMAGE_PATH):
        root = root.replace('\\', '/')
        for file_name in files:
            if file_name.lower().endswith(".png"):
                full_path = root + '/' + file_name
                print(full_path)
                images.append(full_path)
    return images