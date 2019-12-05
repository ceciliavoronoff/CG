from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import sys
 
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
 
#https://www.opengl.org/wiki/Calculating_a_Surface_Normal
#Begin Function CalculateSurfaceNormal (Input Triangle) Returns Vector
#  Set Vector U to (Triangle.p2 minus Triangle.p1)
#  Set Vector V to (Triangle.p3 minus Triangle.p1)
#  Set Normal.x to (multiply U.y by V.z) minus (multiply U.z by V.y)
#  Set Normal.y to (multiply U.z by V.x) minus (multiply U.x by V.z)
#  Set Normal.z to (multiply U.x by V.y) minus (multiply U.y by V.x)
#  Returning Normal
#End Function
 
def calculaNormalFace(face):
    x = 0
    y = 1
    z = 2
    v0 = vertices[face[0]]
    v1 = vertices[face[1]]
    v2 = vertices[face[2]]
    U = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
    V = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
    N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
    NLength = sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
    return ( N[x]/NLength, N[y]/NLength, N[z]/NLength)
 
def Piramide():
   getvertices = []
   getlinhas = []
   getfaces = []
   getvertices = vertices()
   getlinhas = linhas()
   getfaces = faces()
   
   glBegin(GL_TRIANGLES)
   for face in getfaces:
       #glColor3fv((1,1,1))
       glNormal3fv(calculaNormalFace(face))
       for vertex in face:
           glVertex3fv(vertex)
   glEnd()
 
   glColor3fv((1,1,1))
   glBegin(GL_LINES)
   for linha in getlinhas:
       for vertice in linha:
           glVertex3fv(vertice)
   glEnd()
 
def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Piramide()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,1,10,0,0,0,0,1,0)
 
def init():
#    mat_ambient = (0.0, 0.0, 0.5, 1.0)
    mat_ambient = (0.8, 0.0, 0.0, 1.0)
    mat_diffuse = (1.0, 0.0, 0.0, 1.0)
    mat_specular = (1.0, 1.0, 1.0, 1.0)
    mat_shininess = (100,)
    light_position = (0, 8, 0)
    glClearColor(0.0,0.0,0.0,0.0)
    glShadeModel(GL_SMOOTH)
 
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)
 
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Piramide")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutTimerFunc(50,timer,1)
    init()
    glutMainLoop()
 
main()