# Construçao parcial do prisma de n-lados
# O efeito foi criado por acidente ao listar
# fora de ordem os vértices das faces laterais
# Mas eu curti o resultado!

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math


n = 8
raio = 2
angulo = (2 * math.pi)/n

def vertices():
   vertice = []
   
   for i in range(2*n):
       
       x = raio * math.cos(i * angulo)
       z = raio * math.sin(i * angulo)
           
       if (i < n):
           vertice.append([x, 0, z])
        
       else:     
            vertice.append([x, 3, z])

   return vertice

def linhas():
   linha = []
   getvertice = []
   getvertice = vertices()

   for i in range(2*n):    
       aux = []
       # base inferior
       if (i < n):
           if(i == n-1):
               aux.append(getvertice[i])
               aux.append(getvertice[0])
               linha.append(aux)

           else:
                aux.append(getvertice[i])
                aux.append(getvertice[i+1])
                linha.append(aux)

       # base superior
       else:
           if(i == 2*n-1):
               aux.append(getvertice[i])
               aux.append(getvertice[n])
               linha.append(aux)

           else:
                aux.append(getvertice[i])
                aux.append(getvertice[i+1])
                linha.append(aux)

    # laterais
   for i in range(n):
        aux.append(getvertice[i])
        aux.append(getvertice[i+8])
        linha.append(aux)

   return linha

def faces():
   face = []
   getvertice = []
   getvertice = vertices()

   for i in range(n):
       aux = []
       if(i == n-1):
           aux.append(getvertice[i])
           aux.append(getvertice[0])
           aux.append(getvertice[i+n])
           aux.append(getvertice[n])
           face.append(aux)

       else:
           aux.append(getvertice[i])
           aux.append(getvertice[i+1])
           aux.append(getvertice[i+n])
           aux.append(getvertice[i+n+1])
           face.append(aux)

   return face

def Prisma():
   getvertices = []
   getlinhas = []
   getfaces = []
   getvertices = vertices()
   getlinhas = linhas()
   getfaces = faces()
  
   glBegin(GL_QUADS)
   for face in getfaces:
       for vertex in face:
           glColor3fv((1,1,1))
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
   Prisma()
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
glutCreateWindow("Prisma")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-12)
glutTimerFunc(50,timer,1)
glutMainLoop()