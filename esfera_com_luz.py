from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
#import sys
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
   for i in range(resolucao):
      glBegin(GL_TRIANGLE_STRIP)
      for j in range(resolucao+1):
         glColor3f(1,0,(1+math.sin(j*2*math.pi/resolucao))/2)
         glVertex3fv(vertices(i,j))
         glVertex3fv(vertices(i+1,j))
      glEnd()
 
def display():
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
    mat_diffuse = (1.0, 0.0, 0.0, 1.0)
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
    glutDisplayFunc(display)
    glutTimerFunc(50,timer,1)
    glutMainLoop()
 
main()