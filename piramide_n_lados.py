from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math


n = 8
raio = 2
angulo = (2 * math.pi)/n

def vertices():

   vertice = []
   
   for i in range(n+1):

       aux = []

       if(i == 0):
           aux.append(0)
           aux.append(3)
           aux.append(0)

           vertice.append(aux)

       else:
           x = raio * math.cos(i * angulo)
           z = raio * math.sin(i * angulo)

           aux.append(x)
           aux.append(0)
           aux.append(z)

           vertice.append(aux)

   return vertice

def linhas():

   linha = []
   getvertice = []
   getvertice = vertices()

   for i in range(n):    
       aux = []
       aux.append(getvertice[0])
       aux.append(getvertice[i+1])
       linha.append(aux)
   
   for i in range(1, n+1):
    
       aux = []

       if(i == n):
           aux.append(getvertice[i])
           aux.append(getvertice[1])
           linha.append(aux)

       else:
           aux.append(getvertice[i])
           aux.append(getvertice[i+1])
           linha.append(aux)

   return linha

def faces():

   face = []
   getvertice = []
   getvertice = vertices()

   for i in range(n):
       aux = []
       if(i == 0):
            aux.append(getvertice[0])
            aux.append(getvertice[n])
            aux.append(getvertice[1])
            face.append(aux)
       else:
            aux.append(getvertice[0])
            aux.append(getvertice[i])
            aux.append(getvertice[i+1])
            face.append(aux)

            if (i < n-1):
                aux.append(getvertice[1])
                aux.append(getvertice[i+1])
                aux.append(getvertice[i+2])
                face.append(aux)
            
   return face

def Piramide():
   getvertices = []
   getlinhas = []
   getfaces = []
   getvertices = vertices()
   getlinhas = linhas()
   getfaces = faces()
   
   glBegin(GL_TRIANGLES)
   for face in getfaces:
       glColor3fv((1,1,1))
       for vertex in face:
           glVertex3fv(vertex)
   glEnd()
 
   glColor3fv((0,0,0))
   glBegin(GL_LINES)
   for linha in getlinhas:
       for vertice in linha:
           glVertex3fv(vertice)
   glEnd()

a = 0
def desenha():
   global a
   glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
   glPushMatrix()
   glRotatef(-a,1,1,0)
   Piramide()
   glPopMatrix()
   glutSwapBuffers()
   a += 1
   
def timer(i):
   glutPostRedisplay()
   glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Piramide")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-12)
glutTimerFunc(50,timer,1)
glutMainLoop()