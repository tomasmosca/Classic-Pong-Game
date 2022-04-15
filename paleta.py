from ursina import *

class Paleta(Entity):
    def __init__(self, position = (0,0), **kwargs):
        super().__init__(
            model='quad',
            position = position,
            color = color.white,
            scale_y = 1,
            scale_x = 0.2,
            collision = True,
            collider = 'box',
            puntuacion = 0)