'''
        SR3 Obj Models

Creado por:

    Juan Fernando De Leon Quezada   Carne 17822

Engine 3D

'''

from gl import *
from texture import Texture

bmp = Bitmap(1364,1020)

def glInit():
    return bmp

if __name__ == '__main__':
    '''Main Program'''

    bmp = glInit()
    bmp.glCreateWindow(1000,1000)
    bmp.glClear()
    bmp.glColor(1, 1, 1)

    backgorund = Texture('fondo.bmp')
    bmp.framebuffer = backgorund.pixels

    mapeoNormal = Texture('normalMapVidrio.bmp')

    bmp.lookAt(V3(-0.2,0,20),V3(0,0,0),norm(V3(0,1,0)))
    bmp.loadViewportMatrix(0, 0)

    bmp.glLoadObjModel("man.obj", mtl="man.mtl", scale=(0.09,0.09,0.09),translate=(-2.8,-7.0,10),rotate=(0,0,0),shader = 2)
    bmp.glLoadObjModel("oso.obj", mtl="oso.mtl", scale=(0.035,0.035,0.035),translate=(-1.8,-1.0,10),rotate=(0.5,0,0),shader = 5)
    bmp.glLoadObjModel("botella.obj", mtl="botella.mtl", scale=(0.03,0.03,0.03),translate=(-1.2,-0.5,0),rotate=(0.5,0,0),shader = 3)
    bmp.glLoadObjModel("lata.obj", mtl="lata.mtl", scale=(0.035,0.035,0.035),translate=(-1.2,-1.3,10),rotate=(0.5,0,0),shader = 4)
    bmp.glLoadObjModel("vino.obj", mtl="vino.mtl", scale=(0.04,0.04,0.04),translate=(1.7,-1.15,10),rotate=(-0.2,0,1.73), shader = 1)

    bmp.glLoadObjModel("copasRoja.obj", mtl="copasRoja.mtl", scale=(0.035,0.035,0.035),translate=(-0.65,-0.99,5),rotate=(0.5,0,0), shader = 5)

    bmp.glLoadObjModel("copasRoja.obj", mtl="copasRoja.mtl", scale=(0.035,0.035,0.035),translate=(-0.65,-0.99,5),rotate=(0.5,0,0), shader = 5)

    bmp.glWrite("output.bmp")
    