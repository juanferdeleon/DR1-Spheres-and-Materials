'''
        DR1 Spheres and Materials

Creado por:

    Juan Fernando De Leon Quezada   Carne 17822

Raytracer Engine 

'''
from gl import *
from texture import Texture
from obj import ObjReader
from sphere import Sphere, Material

if __name__ == '__main__':
    '''Main Program'''

    brick = Material(diffuse = color(204, 64, 64 ))
    stone = Material(diffuse = color(112, 112, 112 ))
    grass = Material(diffuse = color(128, 255, 0))


    width = 500
    height = 300
    r = Raytracer(width,height)

    r.scene.append( Sphere(V3(0, 0,  -7), 1, brick) )
    r.scene.append( Sphere(V3(1, 1, -10), 1, stone) )
    r.scene.append( Sphere(V3(-1.5, -1.5, -13), 1, grass) )
    
    r.rtRender()

    r.glFinish('output.bmp')