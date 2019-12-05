from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import sys
import png
 
xrot = yrot = zrot = 0.0
texture = []

resolucao = 50
raio = 3

def vertices(i,j):
    theta = i * math.pi/resolucao
    phi = j * 2 * math.pi/resolucao
    x = raio * math.sin(theta) * math.cos(phi)
    y = raio * math.cos(theta) * math.cos(phi)
    z = raio * math.sin(phi)
    return x,y,z
 
def LoadTextures():
    global texture
    texture = glGenTextures(2)
 
    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[0])
    reader = png.Reader(filename='terra_baixa.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################
 
def InitGL(Width, Height):             
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)    
    glClearDepth(1.0)                  
    glDepthFunc(GL_LESS)               
    glEnable(GL_DEPTH_TEST)            
    glShadeModel(GL_SMOOTH)            
     
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
 
    glMatrixMode(GL_MODELVIEW)
 
def DrawGLScene():
    global xrot, yrot, zrot, texture
 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()                   
    glClearColor(0.5,0.5,0.5,1.0)            
    glTranslatef(0.0,0.0,-10.0)            
    glRotatef(zrot,1.0,1.0,0.0) 
    glBindTexture(GL_TEXTURE_2D, texture[0])
 
    for i in range(0,resolucao):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(0,resolucao+1):
            glTexCoord2f(float (i)/resolucao,float (j)/resolucao)
            glVertex3fv(vertices(i,j))
            glTexCoord2f(float(i+1)/resolucao,float (j)/resolucao)
            glVertex3fv(vertices(i+1,j))
        glEnd()              
     
    xrot  = xrot + 1                # X rotation
    yrot = yrot + 1                 # Y rotation
    zrot = zrot + 1                 # Z rotation
 
    glutSwapBuffers()

def main():
    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutCreateWindow("Textura")
    glutIdleFunc(DrawGLScene)
    InitGL(640, 480)
    glutMainLoop()
 
main()