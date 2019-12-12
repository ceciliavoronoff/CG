from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import math

resolucao = 100
raio = 2

def calculaNormalFace(vertices):
    v0 = vertices[x]
    v1 = vertices[y]
    v2 = vertices[z]
    U = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
    V = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
    N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
    NLength = sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
    return ( N[x]/NLength, N[y]/NLength, N[z]/NLength)

def vertices(i,j):
    theta = i * math.pi/resolucao
    phi = j * 2 * math.pi/resolucao
    x = raio * math.sin(theta) * math.cos(phi)
    y = raio * math.cos(theta) * math.cos(phi)
    z = raio * math.sin(phi)
    return x,y,z
 
def Esfera():
   c0 = []
   c1 = []
   for i in range(resolucao):
      glBegin(GL_TRIANGLE_STRIP)
      for j in range(resolucao+1):
         c0 = vertices(i,j)
         cx0 = c0[0]
         cy0 = c0[1]
         cz0 = c0[2]
         glNormal3f(cx0,cy0,cz0)
         glVertex3fv(vertices(i,j))
         c1 = vertices(i+1,j)
         cx1 = c1[0]
         cy1 = c1[1]
         cz1 = c1[2]
         glNormal3f(cx1,cy1,cz1)
         glVertex3fv(vertices(i+1,j))
      glEnd()

def desenha():
   glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
   glRotatef(10,1,1,1)
   Esfera()
   glutSwapBuffers()
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,1,10,0,0,0,0,1,0)
 
def init():
    mat_ambient = (0.6, 0.0, 0.0, 1.0)
    mat_diffuse = (0.4, 0.0, 0.0, 1.0)
    mat_specular = (1.0, 1.0, 1.0, 1.0)
    mat_shininess = (50,)
    light_position = (5.0, 5.0, 5.0, 0.0)
    glClearColor(0.0,0.0,0.0,0.0)
    glShadeModel(GL_SMOOTH)
 
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)
 
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Esfera")
    init()
    glutReshapeFunc(reshape)
    glutDisplayFunc(desenha)
    glutTimerFunc(50,timer,1)
    glutMainLoop()
 
main()