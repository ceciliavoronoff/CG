from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

resolucao = 100
raio = 4

def vertices(i,j):
    theta = i * math.pi/resolucao
    phi = j * 2 * math.pi/resolucao
    x = raio * math.sin(theta) * math.cos(phi)
    y = raio * math.cos(theta) * math.cos(phi)
    z = raio * math.sin(phi)
    return x,y,z

def Esfera():
   glBegin(GL_QUAD_STRIP)
   for i in range(resolucao+1):
      for j in range(resolucao+1):
         glColor3f(0,i,1+i)
         glVertex3fv(vertices(i,j))
         glVertex3fv(vertices(i+1,j))
   glEnd()
 
  
def desenha():
   glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
   #glPushMatrix()
   glRotatef(10,1,1,1)
   Esfera()
   #glPopMatrix()
   glutSwapBuffers()


def timer(i):
   glutPostRedisplay()
   glutTimerFunc(50,timer,1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Esfera")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-12)
glutTimerFunc(50,timer,1)
glutMainLoop()