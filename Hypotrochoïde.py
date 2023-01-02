from cmath import pi
import pygame 
import math



def cercle(surface,radius,color,x,y):
       
    pygame.draw.circle(surface, (color), (x/2, y/2), radius, 1)
    return radius,x/2, y/2


def rad_to_deg(angle):
    return  angle * pi / 180

def moving_circle(surface, angle, color, radius,x,y,rayon):
    cos = math.cos(angle)
    sin = math.sin(angle)
    x = x + cos * (radius -  rayon)
    y = y + sin * (radius -  rayon)
    pygame.draw.circle(surface, color, (x, y), rayon,1)
    pygame.draw.circle(surface, color, (x, y), 60,1)
    cos = math.cos(angle_2)
    sin = math.sin(angle_2)
    x_1 = x + cos * 60
    y_1 = y + sin * 60
    pygame.draw.line(surface,color,(x, y),(x_1,y_1) )

    return x_1,y_1








lst_point = []
lauched = True
taille = (600,600)
screen = pygame.display.set_mode(taille) 
x, y = screen.get_size()
angle = 360
angle_2 =  0 

while lauched:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lauched=False
    screen.fill((0, 0, 0))
    radius,x_1,y_1 = cercle(screen,200,(255,0,0),x,y)
    x_1,y_1 = moving_circle(screen, rad_to_deg(angle/10), (200,0,200), radius,x_1,y_1,30)



    lst_point.append(x_1)
    lst_point.append(y_1)
    
    if angle ==3599:
        for i in range (int((len(lst_point)/2))):
            pygame.draw.circle(screen,(0,0,255),(lst_point[2*i],lst_point[2*i+1]),1)
            pygame.display.update()
        pygame.time.wait(5000)
    angle = (angle - 1) % 3600  
    angle_2 = (angle_2 + 1) % 3600 
    pygame.display.update()



