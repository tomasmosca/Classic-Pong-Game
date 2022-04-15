from ursina import *
from paleta import *
from pelota import *

paleta = Paleta(position = (-6,0))
paleta2 = Paleta(position = (6,0))

paredIzq = Entity(model='quad', position=(-7.3,0), collider='box', scale=(0.1,8.2), visible=False, collision=True)
paredDer = duplicate(paredIzq, position=(7.3,0), visible=False)
piso = duplicate(paredIzq, position=(2,-4.1), rotation_z=90, scale=(0.1,20), visible=False)
techo = duplicate(paredIzq, position=(2,4.1), rotation_z=90, scale=(0.1,20), visible=False)

for y in range(1,5):
    linea = Paleta(position = (0,y*2-5))
    linea.scale = (0.1,1)

pelota = Pelota()

pelota.direccionX = 3
pelota.direccionY = 3


def update():

    intersecPaleta = paleta.intersects()
    intersecPaleta2 = paleta2.intersects()

    if(not intersecPaleta.hit):
        paleta.y+=held_keys['w'] * time.dt * 5
        paleta.y-=held_keys['s'] * time.dt * 5
    else:
        if(intersecPaleta.entity == techo):
            paleta.y-=held_keys['s'] * time.dt * 5
        elif(intersecPaleta.entity == piso):
            paleta.y+=held_keys['w'] * time.dt * 5

    if(not intersecPaleta2.hit):
        paleta2.y+=held_keys['up arrow'] * time.dt * 5
        paleta2.y-=held_keys['down arrow'] * time.dt * 5
    else:
        if(intersecPaleta2.entity == techo):
            paleta2.y-=held_keys['down arrow'] * time.dt * 5
        elif(intersecPaleta2.entity == piso):
            paleta2.y+=held_keys['up arrow'] * time.dt * 5

    pelota.x+=pelota.direccionX* time.dt
    pelota.y+=pelota.direccionY* time.dt
    interseca = pelota.intersects()
    if(interseca.hit):
        if(interseca.entity == paleta):
            pelota.direccionX = 4
        elif(interseca.entity == paleta2):
            pelota.direccionX = -4
        elif(interseca.entity == paredIzq):
            pelota.position = (0,0)
            pelota.direccionX = 4
            paleta2.puntuacion+=1
            texto2.text = str(paleta2.puntuacion)
        elif(interseca.entity == paredDer):
            pelota.position = (0,0)
            pelota.direccionX = -4
            paleta.puntuacion+=1
            texto.text = str(paleta.puntuacion)
        elif(interseca.entity == piso):
            pelota.direccionY = 4
        elif(interseca.entity == techo):
            pelota.direccionY = -4

app = Ursina()

Text.size = 0.10
Text.default_resolution = 1080 * Text.size

texto = Text(origin=(5,-4), text=str(paleta.puntuacion))
texto2 = Text(origin=(-5,-4), text=str(paleta2.puntuacion))

app.set_background_color(0, 0, 0)
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.title = 'Pong'

app.run()