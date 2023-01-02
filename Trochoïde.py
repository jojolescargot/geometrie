from cmath import pi
import pygame 
import math


def droite(surface,x,y,color):
    pygame.draw.line(surface,color,(0,y/2),(x,y/2),3)
    return 0,(y/2)



def cercle(surface,x,y,l,color,radius,radius_2):
    pygame.draw.circle(surface,color,(l,int(y-radius)),radius,3)





    ###pygame.draw.circle(surface,color,(l,int(y-radius)),radius_2,3)





    cos = math.cos(l/radius)
    sin = math.sin(l/radius)
    x_p = l + cos * radius_2
    y_p  = y-radius  + sin * radius_2


    pygame.draw.line(surface,color,(l,int(y-radius)),(x_p,y_p))
    pygame.draw.circle(surface,color,(x_p,y_p),8)
    return x_p,y_p

lst_point = []
lauched = True
taille = (1500,600)
screen = pygame.display.set_mode(taille) 
x, y = screen.get_size()
l = 0


while lauched:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lauched=False
    screen.fill((0, 0, 0))
    x_c,y_c = droite(screen,x,y,(122,122,4))
    x_p,y_p = cercle(screen,x_c,y_c,l/10,(4,122,122),80,100)
    l = l + 10

    lst_point.append(x_p)
    lst_point.append(y_p)

    if l == x*10:
        for i in range (int((len(lst_point)/2))):
            pygame.draw.circle(screen,(0,0,255),(lst_point[2*i],lst_point[2*i+1]),1)
            pygame.display.update()
        pygame.time.wait(5000)        
        l = 0


    pygame.display.update()




