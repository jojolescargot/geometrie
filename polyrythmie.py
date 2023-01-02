from cmath import pi
import pygame 
import math
def rythme(bpm,intervalle):
    temps = 60000/bpm
    temps_intervalle = int(temps/intervalle)

    return temps_intervalle

def cercle(surface, ratio):
    x, y = screen.get_size() 
    radius = y * ratio  
    pygame.draw.circle(surface, (102, 255, 255), (x/2, y/2), radius, 5)
    return radius


def moving_circle(surface, angle, color, radius):
    x, y = screen.get_size()
    cos = math.cos(angle)
    sin = math.sin(angle)
    x = x/2 + cos * radius
    y = y/2 + sin * radius
    pygame.draw.circle(surface, color, (x, y), 8)
    
def rad_to_deg(angle):
    return  angle * pi / 180

def get_speed(time_one_loop):
    return 360 / time_one_loop


def stars(surface,color,rythme,radius):
    cos = math.cos(0)
    sin = math.sin(0)
    x, y = screen.get_size()
    point_1 = (x/2 + cos * radius , y/2 + sin * radius)
    point_2 = ()
    i =  rythme 
    angle = 360 / rythme
    angle_O = 360 / rythme
    
    while i != 0:
        i = i - 1       
        cos = math.cos(rad_to_deg(angle))
        sin = math.sin(rad_to_deg(angle))
        point_2 = ( x/2 + cos * radius , y/2 + sin * radius)
        pygame.draw.line(surface, color,point_1,point_2, 3)
        point_1 = point_2
        angle = angle + angle_O 
         
def moving_circle_on_stars(surface,rythme,radius,t):
    cos = math.cos(0)
    sin = math.sin(0)
    x, y = screen.get_size()
    point_1 = (x/2 + cos * radius , y/2 + sin * radius)
    point_2 = () 
    angle = 360 / rythme
    angle_O = 360 / rythme        
    cos = math.cos(rad_to_deg(angle))
    sin = math.sin(rad_to_deg(angle))
        

    point_2 = ( x/2 + cos * radius , y/2 + sin * radius)
   
    if t > 0.9:
        point_1 = point_2
        angle =  angle + angle_O
        cos = math.cos(rad_to_deg(angle))
        sin = math.sin(rad_to_deg(angle))
        point_2 = ( x/2 + cos * radius , y/2 + sin * radius)
    
    center = (point_1[0]+t*(point_2[0]-point_1[0]),point_1[1]+t*(point_2[1]-point_1[1]))
    pygame.draw.circle(surface,(255,255,255),center,50)
    print(t)

 

pygame.mixer.init()
pygame.init

lauched = True
taille = (600,600)
screen = pygame.display.set_mode(taille,pygame.RESIZABLE)
bpm = 10
angle = 0
p = 0

clock = pygame.time.Clock()

while lauched:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lauched=False

    # Logic
    clock.tick()
    delta_time = clock.get_time() * 1e-3
    speed = get_speed(10)
    angle = (angle + speed * delta_time) % 360
    
    # Drawing
    screen.fill((254, 163, 71))



    radius = 0 
    radius = cercle(screen, 9/20)
    moving_circle(screen, rad_to_deg(angle), (255, 0, 0), radius)














    stars(screen,(60,80,200),3,radius)
    stars(screen,(100,50,70),13,radius)
    p = (p +0.001)
    moving_circle_on_stars(screen,3,radius,p)
     
    if p > 0.9:
        p = 0
    pygame.display.update()
