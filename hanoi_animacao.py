from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
# animação para simular uma função auto complete
pino1 = [8,7,6,5,4,3,2,1]
pino2 = []
pino3 = []
pinos = [[8,7,6,5,4,3,2,1],[],[]]
a = len(pino1)
jogadas = 3
contador = 0

def moveTorre(altura,origem, destino, aux):
    if (altura > 0):
       moveTorre(altura-1,origem,aux,destino)
       moveDisk(origem,destino,altura)
       moveTorre(altura-1,aux,destino,origem)
    
def moveDisk(origem,destino,altura):
    global pino1
    global pino2
    global pino3
    global jogadas
    destino.append(altura)
    origem.pop()
    pinos.append(pino1[:])
    pinos.append(pino2[:])
    pinos.append(pino3[:])
    jogadas += 3

def criaLog():
   while (pino1 or pino2):
      moveTorre(a,pino1,pino3,pino2)

def desenhaDiscosA():
   z = 4.5
   for i in pino1:
      glPushMatrix()
      glTranslatef(0,0,z)
      glColor3f(1,0,1/i)
      glutSolidCylinder(i/4,0.5,32,32)
      z -= 0.5
      glPopMatrix()

def desenhaDiscosB():   
   z = 4.5
   for i in pino2:
      glPushMatrix()
      glTranslatef(0,0,z)
      glColor3f(1,0,1/i)
      glutSolidCylinder(i/4,0.5,32,32)
      z -= 0.5
      glPopMatrix()
   
def desenhaDiscosC():   
   z = 4.5
   for i in pino3:
      glPushMatrix()
      glTranslatef(0,0,z)
      glColor3f(1,0,1/i)
      glutSolidCylinder(i/4,0.5,32,32)
      z -= 0.5
      glPopMatrix()

def desenha():
   global pino1
   global pino2
   global pino3
   global contador
   pino1 = pinos[contador]
   pino2 = pinos[contador+1]
   pino3 = pinos[contador+2]
   glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
   glPushMatrix()
   glRotatef(90,1,0,0)
   glTranslatef(0,0,-3)
   glColor3f(1,1,1)
   glutSolidCylinder(0.1,5.0,32,32)
   desenhaDiscosB()
   glPopMatrix()
   glPushMatrix()
   glRotatef(90,1,0,0)
   glTranslatef(-5,0,-3)
   glColor3f(1,1,1)
   glutSolidCylinder(0.1,5.0,32,32)
   desenhaDiscosA()
   glPopMatrix()
   glPushMatrix()
   glRotatef(90,1,0,0)
   glTranslatef(5,0,-3)
   glColor3f(1,1,1)
   glutSolidCylinder(0.1,5.0,32,32)
   desenhaDiscosC()
   glPopMatrix()
   glutSwapBuffers()
   contador += 3
   if contador > jogadas-1:
       contador = 0

def timer(i):
   glutPostRedisplay()
   glutTimerFunc(500,timer,1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Hanoi")
glutDisplayFunc(desenha)
criaLog()
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-20)
glutTimerFunc(500,timer,1)
glutMainLoop()