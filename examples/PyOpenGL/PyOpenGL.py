from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB) 
glutInitWindowSize(300, 300)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow(b"Happy New Year!")
glutMainLoop()