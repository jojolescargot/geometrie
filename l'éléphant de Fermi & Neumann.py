from cmath import pi
import pygame 
import math




def cercle(surface,ratio,color):
    x, y = screen.get_size() 
    radius = y * ratio  
    pygame.draw.circle(surface, (color), (x/2, y/2), radius, 1)
    return radius,x/2, y/2

def rad_to_deg(angle):
    return  angle * pi / 180

def moving_circle(surface, angle, color, radius,x,y,rayon):
    cos = math.cos(angle)
    sin = math.sin(angle)
    x = x + cos * radius
    y = y + sin * radius
    pygame.draw.circle(surface, color, (x, y), rayon,1)
    pygame.draw.circle(surface, color, (x, y), 2,1)
    return x, y
def moving_point(surface, angle, color, radius,x,y,rayon):
    cos = math.cos(angle)
    sin = math.sin(angle)
    x = x + cos * radius
    y = y + sin * radius
    pygame.draw.circle(surface, (255,100,255), (x, y), 5,5)
    return x, y



red = (254,0,0)
green = (0,255,0)
lauched = True
taille = (600,600)
screen = pygame.display.set_mode(taille) 
x, y = screen.get_size()
lst_point = []
lst_radius_division = [2,4,5]
list_angle = [0,0,0]
speed_angle = [1,2,8]

while lauched:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lauched=False

    for o in range (len(list_angle)):
        list_angle[o] = (list_angle[o] + speed_angle[o]) % 36000
    
    
    screen.fill((0, 0, 0))
            
    radius,x_1,y_1 = cercle(screen,14/100,red)

    x_2, y_2 = moving_circle(screen,rad_to_deg(list_angle[0]/100),green,radius                       ,x_1,y_1,radius/lst_radius_division[0])
    x_3, y_3 = moving_circle(screen,rad_to_deg(list_angle[1]/100),green,radius/lst_radius_division[0] ,x_2,y_2,radius/lst_radius_division[1])
    x_4, y_4 = moving_circle(screen,rad_to_deg(list_angle[2]/100),green,radius/lst_radius_division[1] ,x_3,y_3,radius/lst_radius_division[2])
    #x_5, y_5 = moving_circle(screen,rad_to_deg(list_angle[3]/100),green,radius/lst_radius_division[2] ,x_4,y_4,radius/lst_radius_division[3])
    #x_6, y_6 = moving_circle(screen,rad_to_deg(list_angle[4]/100),green,radius/lst_radius_division[3] ,x_5,y_5,radius/lst_radius_division[4])
    #x_7, y_7 = moving_circle(screen,rad_to_deg(list_angle[5]/10),green,radius/lst_radius_division[4] ,x_6,y_6,radius/lst_radius_division[5])
   # x_8, y_8 = moving_circle(screen,rad_to_deg(list_angle[6]/10),green,radius/lst_radius_division[5] ,x_7,y_7,radius/lst_radius_division[6])
  #  x_9, y_9 =  moving_point(screen,rad_to_deg(list_angle[7]/10),green,radius/lst_radius_division[6] ,x_8,y_8,radius/lst_radius_division[7])
    
    


            





    lst_point.append(x_4)
    lst_point.append(y_4)
    
    if list_angle[0] == 35999:
        for i in range (int((len(lst_point)/2))):
            pygame.draw.circle(screen,(0,0,255),(lst_point[2*i],lst_point[2*i+1]),1)
            pygame.display.update()
        pygame.time.wait(5000)        
    pygame.display.update()