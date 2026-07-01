import pygame

class Button:
    def __init__(self, image, pos_x, pos_y):
        self.image = image
        self.pos_x = pos_x
        self.pos_y = pos_y

        try:
            self.rect = self.image.get_rect()
        except AttributeError:
            print("Image failed to load", AttributeError)

if __name__ == '__main__':
    btn = Button(None, 20, 10)

    print(btn.pos_x, btn.pos_y)
