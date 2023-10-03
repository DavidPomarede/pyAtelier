import pygame
from math import sin, cos, pi, radians
from sys import exit as _exit

#stores three points of the triangle
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

def makeTriangle(scale, internalAngle, rotation):
    #define the points in a uint space
    ia = (radians(internalAngle) * 2) - 1
    p1 = (0, -1)
    p2 = (cos(ia), sin(ia))
    p3 = (cos(ia) * -1, sin(ia))

    #rotate the points
    ra = radians(rotation)
    rp1x = p1[0] * cos(ra) - p1[1] * sin(ra)
    rp1y = p1[0] * sin(ra) + p1[1] * cos(ra)                 
    rp2x = p2[0] * cos(ra) - p2[1] * sin(ra)
    rp2y = p2[0] * sin(ra) + p2[1] * cos(ra)                        
    rp3x = p3[0] * cos(ra) - p3[1] * sin(ra)                         
    rp3y = p3[0] * sin(ra) + p3[1] * cos(ra)
    rp1 = ( rp1x, rp1y )
    rp2 = ( rp2x, rp2y )
    rp3 = ( rp3x, rp3y )

    #scale the points 
    sp1 = [rp1[0] * scale, rp1[1] * scale]
    sp2 = [rp2[0] * scale, rp2[1] * scale]
    sp3 = [rp3[0] * scale, rp3[1] * scale]
                    
    return Triangle(sp1, sp2, sp3)

def drawTriangle(tri, color=(0, 0, 0)):
    pygame.draw.line(window, color, tri.p1, tri.p2)
    pygame.draw.line(window, color, tri.p2, tri.p3)
    pygame.draw.line(window, color, tri.p3, tri.p1)

def offsetTriangle(triangle, offsetx, offsety):
    triangle.p1[0] += offsetx;  triangle.p1[1] += offsety;
    triangle.p2[0] += offsetx;  triangle.p2[1] += offsety;
    triangle.p3[0] += offsetx;  triangle.p3[1] += offsety;

pygame.init()
window = pygame.display.set_mode((600, 600))

#create whatever type of triangle you want
mytriangle1 = makeTriangle(150, 30, 10)
offsetTriangle(mytriangle1, 100, 100)
mytriangle2 = makeTriangle(100, 45, 270)
offsetTriangle(mytriangle2, 300, 300)
mytriangle3 = makeTriangle(70, 45, 180)
offsetTriangle(mytriangle3, 400, 400)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            _exit();


    window.fill((255, 255, 255))

    #draw the triangles
    drawTriangle(mytriangle1)
    drawTriangle(mytriangle2)
    drawTriangle(mytriangle3)
    
    pygame.display.flip()
