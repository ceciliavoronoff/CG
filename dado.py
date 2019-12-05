from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import png
 
xrot = yrot = zrot = 0.0
texture = []
 
def LoadTextures():
    global texture
    texture = glGenTextures(2)
 
    glBindTexture(GL_TEXTURE_2D, texture[0])
    reader = png.Reader(filename='dado.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
 
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
    glTranslatef(0.0,0.0,-8.0)            
    glRotatef(zrot,1.0,1.0,0.0) 
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glBegin(GL_QUADS)              
     
    # Front Face 
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)    
    glTexCoord2f(1.0/3.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)   
    glTexCoord2f(1.0/3.0, 0.5); glVertex3f( 1.0,  1.0,  1.0)   
    glTexCoord2f(0.0, 0.5); glVertex3f(-1.0,  1.0,  1.0)  
     
    # Back Face
    glTexCoord2f(1.0/3.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)    
    glTexCoord2f(2.0/3.0, 0.0); glVertex3f(-1.0,  1.0, -1.0)    
    glTexCoord2f(2.0/3.0, 0.5); glVertex3f( 1.0,  1.0, -1.0)    
    glTexCoord2f(1.0/3.0, 0.5); glVertex3f( 1.0, -1.0, -1.0)   
     
    # Top Face
    glTexCoord2f(2.0/3.0, 0.0); glVertex3f(-1.0,  1.0, -1.0)   
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0,  1.0,  1.0)    
    glTexCoord2f(1.0, 0.5); glVertex3f( 1.0,  1.0,  1.0)    
    glTexCoord2f(2.0/3.0, 0.5); glVertex3f( 1.0,  1.0, -1.0)   
 
    # Bottom Face       
    glTexCoord2f(0.0, 0.5); glVertex3f(-1.0, -1.0, -1.0)   
    glTexCoord2f(1.0/3.0, 0.5); glVertex3f( 1.0, -1.0, -1.0)   
    glTexCoord2f(1.0/3.0, 1.0); glVertex3f( 1.0, -1.0,  1.0)   
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0, -1.0,  1.0)    
     
    # Right face
    glTexCoord2f(1.0/3.0, 0.5); glVertex3f( 1.0, -1.0, -1.0)    
    glTexCoord2f(2.0/3.0, 0.5); glVertex3f( 1.0,  1.0, -1.0)   
    glTexCoord2f(2.0/3.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)    
    glTexCoord2f(1.0/3.0, 1.0); glVertex3f( 1.0, -1.0,  1.0)  
     
    # Left Face
    glTexCoord2f(2.0/3.0, 0.5); glVertex3f(-1.0, -1.0, -1.0)  
    glTexCoord2f(1.0, 0.5); glVertex3f(-1.0, -1.0,  1.0)    
    glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)   
    glTexCoord2f(2.0/3.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)   
     
    glEnd()                # Done Drawing The Cube
     
    xrot  = xrot + 0.2                # X rotation
    yrot = yrot + 0.2                 # Y rotation
    zrot = zrot + 0.2                 # Z rotation
 
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