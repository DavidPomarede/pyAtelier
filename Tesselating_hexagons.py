import math 

from math import cos, sin 

screenWidth = 100
screenHeight = 100

def create_centered_triangle(center, radius):
	C1 = [center[0], center [1] - radius]
	r120 = {'cos': cos(radians(120)), 'sin': sin(radians(120))}
	r240 = {'cos': cos(radians(240)), 'sin': sin(radians(240))}
	rX - [C1[0] - center[0] , C1[1] - center[1]]
	rL, rR = [0, 0], [0, 0]

	rL[0] = rX[0] * r120['cos'] - rX[1] * r120['sin']
	rL[0] = rX[0] * r120['sin'] - rX[1] * r120['cos']
	rR[0] = rX[0] * r240['cos'] - rX[1] * r240['sin']
	rR[0] = rX[0] * r240['sin'] - rX[1] * r240['cos']

	left = [rL[0] + center[0], rL[1] +center[1]]
	right = [rR[0] + center[0], rR[1] +center[1]]

	return [left, right, C1]

triangy = create_centered_triangle((screenWidth // 2, screenHeight // 2), T_SIZE)

for i in range(30, 360, 60):
	new = []
	for point in trangy:
		new.append(rotate_points(point, (screenWidth // 2, screenHeight // 2 - T_SIZE), i))
	other.append(new)

while running:
	screen.fill(black)

	for i in other:
		pygame.draw.polygon(screen, red, i)