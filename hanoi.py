from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

quadric = 0
GLUquadricObj *quadric
quadric = gluNewQuadric()
pino1 = [8, 7, 6, 5, 4, 3, 2, 1]
pino2 = []
pino3 = []

def desenhaDiscosA():
   z = 4.5
   for i in pino1:
      glPushMatrix()
      glTranslatef(0,0,z)
      glColor3f(0.5,0,1/i)
      gluCylinder(quadric,i/4,i/4,0.5,32,32)
      z -= 0.5
      glPopMatrix()

def desenhaDiscosB():   
   z = 4.5
   for i in pino2:
      glPushMatrix()
      glTranslatef(0,0,z)
      glColor3f(0.5,0,1/i)
      gluCylinder(quadric,i/4,i/4,0.5,32,32)
      z -= 0.5
      glPopMatrix()
   
def desenhaDiscosC():   
   z = 4.5
   for i in pino3:
      glPushMatrix()
      glTranslatef(0,0,z)
      glColor3f(0.5,0,1/i)
      gluCylinder(quadric,i/4,i/4,0.5,32,32)
      z -= 0.5
      glPopMatrix()

def desenhaPinos():
   glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
   glPushMatrix()
   glRotatef(90,1,0,0)
   glTranslatef(0,0,-3)
   glColor3f(1,1,1)
   gluCylinder(quadric,0.1,0.1,5.0,32,32)
   desenhaDiscosB()
   glPopMatrix()
   glPushMatrix()
   glRotatef(90,1,0,0)
   glTranslatef(-5,0,-3)
   glColor3f(1,1,1)
   gluCylinder(quadric,0.1,0.1,5.0,32,32)
   desenhaDiscosA()
   glPopMatrix()
   glPushMatrix()
   glRotatef(90,1,0,0)
   glTranslatef(5,0,-3)
   glColor3f(1,1,1)
   gluCylinder(quadric,0.1,0.1,5.0,32,32)
   desenhaDiscosC()
   glPopMatrix()
   glutSwapBuffers()

def desenha():
    desenhaPinos()
   
def timer(i):
   glutPostRedisplay()
   glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Hanoi")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-20)
glutTimerFunc(50,timer,1)
glutMainLoop()