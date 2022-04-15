from ursina import *

class Pelota(Entity):
    def __init__(self, position=(0,0)):
        super().__init__(
            model= 'circle',
            position= position,
            color= color.white,
            scale= .15,
            collider= 'box',
            collision=True,
            direccionX = 0,
            direccionY = 0,
            velocidad = 0)
    