from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

quadric = 0
GLUquadricObj *quadric
quadric = gluNewQuadric()
pino1 = [8, 7, 6, 5, 4, 3, 2, 1]
def desenhaDiscos():
   z = 6.6
   glPushMatrix()
   glTranslatef(0,0,z)
   for i in pino1:
      
      gluCylinder(quadric,i/5,i/5,0.4,32,32)
      z += 0.4
   glPopMatrix()

def desenhaPinos():
   glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
   glPushMatrix()
   glRotatef(90,1,0,0)
   glTranslatef(0,0,-3)
   gluCylinder(quadric,0.1,0.1,7.0,32,32)
   glPopMatrix()
   glPushMatrix()
   glRotatef(90,1,0,0)
   glTranslatef(-5,0,-3)
   gluCylinder(quadric,0.1,0.1,7.0,32,32)
   desenhaDiscos()
   glPopMatrix()
   glPushMatrix()
   glRotatef(90,1,0,0)
   glTranslatef(5,0,-3)
   gluCylinder(quadric,0.1,0.1,7.0,32,32)
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