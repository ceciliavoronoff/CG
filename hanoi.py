from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

ESCAPE = b'\x1b'
pino1 = [8,7,6,5,4,3,2,1]
pino2 = []
pino3 = []
origem = 0
destino = 0
movimento = 0
window = 0
um = b'1'
dois = b'2'
tres = b'3'

def desenhaDiscosA():
   z = 4.5
   for i in pino1:
      glPushMatrix()
      glTranslatef(0,0,z)
      glColor3f(0.5,0,1/i)
      glutSolidCylinder(i/4,0.5,32,32)
      z -= 0.5
      glPopMatrix()

def desenhaDiscosB():   
   z = 4.5
   for i in pino2:
      glPushMatrix()
      glTranslatef(0,0,z)
      glColor3f(0.5,0,1/i)
      glutSolidCylinder(i/4,0.5,32,32)
      z -= 0.5
      glPopMatrix()
   
def desenhaDiscosC():   
   z = 4.5
   for i in pino3:
      glPushMatrix()
      glTranslatef(0,0,z)
      glColor3f(0.5,0,1/i)
      glutSolidCylinder(i/4,0.5,32,32)
      z -= 0.5
      glPopMatrix()

def desenha():
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

def keyPressed(*args):
   global movimento
   if args[0] == um:
      movimento = 1
   if args[0] == dois:
      movimento = 2
   if args[0] == tres:
      movimento = 3
   if args[0] == ESCAPE:
      glutDestroyWindow(window)
      sys.exit()

c = 0
def movimentos():
   global origem
   global destino
   global c
   global movimento
   glutKeyboardFunc(keyPressed)
   print(movimento)
   c += 1
   if c == 1:
      origem = movimento
      
   else:
      destino = movimento
      c = 0
      jogada()

def jogada():
   if origem == "1":
      if pino1:
         ultimo1 = pino1[-1]
         if destino == "2":
            if pino2:
               ultimo2 = pino2[-1]
               if ultimo1 < ultimo2:
                  pino2.append(ultimo1)
                  pino1.pop()  
            elif not pino2:
               pino2.append(ultimo1)
               pino1.pop()
         if destino == "3":
            if pino3:
               ultimo3 = pino3[-1]
               if ultimo1 < ultimo3:
                  pino3.append(ultimo1)
                  pino1.pop()  
            elif not pino3:
               pino3.append(ultimo1)
               pino1.pop()
   if origem == "2":
      if pino2:
         ultimo2 = pino2[-1]
         if destino == "1":
            if pino1:
               ultimo1 = pino1[-1]
               if ultimo2 < ultimo1:
                  pino1.append(ultimo2)
                  pino2.pop()  
            elif not pino1:
               pino1.append(ultimo2)
               pino2.pop()
         if destino == "3":
            if pino3:
               ultimo3 = pino3[-1]
               if ultimo2 < ultimo3:
                  pino3.append(ultimo2)
                  pino2.pop()  
            elif not pino3:
               pino3.append(ultimo2)
               pino2.pop()
   if origem == "3":
      if pino3:
         ultimo3 = pino3[-1]
         if destino == "2":
            if pino2:
               ultimo2 = pino2[-1]
               if ultimo3 < ultimo2:
                  pino2.append(ultimo3)
                  pino3.pop()  
            elif not pino2:
               pino2.append(ultimo3)
               pino3.pop()
         if destino == "1":
            if pino1:
               ultimo1 = pino1[-1]
               if ultimo3 < ultimo1:
                  pino1.append(ultimo3)
                  pino3.pop()  
            elif not pino1:
               pino1.append(ultimo3)
               pino3.pop()
   

def timer(i):
   glutPostRedisplay()
   glutTimerFunc(50,timer,1)

def main():
   glutInit(sys.argv)
   glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
   glutInitWindowSize(800,600)
   window = glutCreateWindow("Hanoi")
   glutDisplayFunc(desenha)
   movimentos()
   glEnable(GL_MULTISAMPLE)
   glEnable(GL_DEPTH_TEST)
   glClearColor(0.,0.,0.,1.)
   gluPerspective(45,800.0/600.0,0.1,50.0)
   glTranslatef(0.0,0.0,-20)
   glutTimerFunc(50,timer,1)
   glutMainLoop()

main()