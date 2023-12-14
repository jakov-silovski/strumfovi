import pygame
import random

import sys
import math as np
import time
from sys import exit

def poligon1():      #funkcija za crtanje 1. poligona
    deb=10           #debljina poligona
    xmin=50    #
    xmax=750   #koordinate za crtanje poligona
    ymin=50    #
    ymax=650   #
    coord=list()
    pozadina=pygame.image.load('c:/Users/hrvoj/OneDrive/Desktop/pacman/slika1.png')
    pygame.draw.polygon(surface=screen,color='black',points=[(xmin,ymin),(xmax,ymin),(xmax,ymax),(xmin,ymax)],width=deb)
    
    pygame.draw.line(surface=screen,color='black',start_pos=(250,50), end_pos=(250,200),width=1)
    coord.append(((250,50),(250,200)))
    
    pygame.draw.line(surface=screen,color='black',start_pos=(550,50), end_pos=(550,200),width=1)
    coord.append(((550,50),(550,200)))
    
    pygame.draw.line(surface=screen,color='black',start_pos=(250,650), end_pos=(250,500),width=1)
    coord.append(((250,650),(250,500)))

    pygame.draw.line(surface=screen,color='black',start_pos=(550,650), end_pos=(550,500),width=1)
    coord.append(((550,650),(550,500)))

    pygame.draw.line(surface=screen,color='black',start_pos=(350,150), end_pos=(450,150),width=1)
    coord.append(((350,150),(450,150)))

    pygame.draw.line(surface=screen,color='black',start_pos=(350,550), end_pos=(450,550),width=1)
    coord.append(((350,550),(450,550)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(100,200), end_pos=(200,200),width=1)
    coord.append(((100,200),(200,200)))    

    pygame.draw.line(surface=screen,color='black',start_pos=(100,200), end_pos=(100,300),width=1)
    coord.append(((100,200),(100,300)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(100,400), end_pos=(100,500),width=1)
    coord.append(((100,400),(100,500)))

    pygame.draw.line(surface=screen,color='black',start_pos=(100,500), end_pos=(200,500),width=1)
    coord.append(((100,500),(200,500)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(200,250), end_pos=(250,250),width=1)
    coord.append(((200,250),(250,250)))

    pygame.draw.line(surface=screen,color='black',start_pos=(200,250), end_pos=(200,300),width=1)
    coord.append(((200,250),(200,300)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(320,160), end_pos=(320,200),width=1)
    coord.append(((320,160),(320,200))) 

    pygame.draw.line(surface=screen,color='black',start_pos=(200,450), end_pos=(200,400),width=1)
    coord.append(((200,450),(200,400)))

    pygame.draw.line(surface=screen,color='black',start_pos=(200,450), end_pos=(250,450),width=1)
    coord.append(((200,450),(250,450))) 
#
    pygame.draw.line(surface=screen,color='black',start_pos=(600,200), end_pos=(700,200),width=1)
    coord.append(((600,200),(700,200))) 

    pygame.draw.line(surface=screen,color='black',start_pos=(700,200), end_pos=(700,300),width=1)
    coord.append(((700,200),(700,300)))

    pygame.draw.line(surface=screen,color='black',start_pos=(700,400), end_pos=(700,500),width=1)
    coord.append(((700,400),(700,500)))

    pygame.draw.line(surface=screen,color='black',start_pos=(700,500), end_pos=(600,500),width=1)
    coord.append(((700,500),(600,500)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(550,250), end_pos=(600,250),width=1)
    coord.append(((550,250),(600,250)))

    pygame.draw.line(surface=screen,color='black',start_pos=(600,250), end_pos=(600,300),width=1)
    coord.append(((600,250),(600,300)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(600,400), end_pos=(600,450),width=1)
    coord.append(((600,400),(600,450)))

    pygame.draw.line(surface=screen,color='black',start_pos=(600,450), end_pos=(550,450),width=1)
    coord.append(((600,450),(550,450)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(300,300), end_pos=(500,300),width=1)
    coord.append(((300,300),(500,300)))

    pygame.draw.line(surface=screen,color='black',start_pos=(300,300), end_pos=(300,400),width=1)
    coord.append(((300,300),(300,400)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(500,300), end_pos=(500,400),width=1)
    coord.append(((500,300),(500,400)))

    pygame.draw.line(surface=screen,color='black',start_pos=(300,400), end_pos=(350,400),width=1)
    coord.append(((300,400),(350,400)))

    pygame.draw.line(surface=screen,color='black',start_pos=(450,400), end_pos=(500,400),width=1)
    coord.append(((450,400),(500,400)))

    ####defniniramo poziciju hrane

    eat=[(350,350),(150,600),(400,250),(170,125),(680,360),(620,150)]
    
    return xmin,xmax,ymin,ymax,coord,eat,pozadina

def poligon2():      #funkcija za crtanje 2. poligona
    deb=10
    xmin=50
    xmax=750
    ymin=50
    ymax=650
    coord=list()
    pozadina=pygame.image.load('c:/Users/hrvoj/OneDrive/Desktop/pacman/slika2.png')
    pygame.draw.polygon(surface=screen,color='black',points=[(xmin,ymin),(xmax,ymin),(xmax,ymax),(xmin,ymax)],width=deb)
    
    pygame.draw.line(surface=screen,color='black',start_pos=(250,50), end_pos=(250,250),width=1)
    coord.append(((250,50),(250,250)))
    
    pygame.draw.line(surface=screen,color='black',start_pos=(400,200), end_pos=(400,50),width=1)
    coord.append(((400,200),(400,50)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(650,550), end_pos=(650,650),width=1)
    coord.append(((650,550),(650,650)))

    pygame.draw.line(surface=screen,color='black',start_pos=(400,500), end_pos=(400,650),width=1)
    coord.append(((400,500),(400,650)))

    pygame.draw.line(surface=screen,color='black',start_pos=(150,650), end_pos=(150,575),width=1)
    coord.append(((150,650),(150,575)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(50,200), end_pos=(150,200),width=1)
    coord.append(((50,200),(150,200)))

    pygame.draw.line(surface=screen,color='black',start_pos=(50,500), end_pos=(150,500),width=1)
    coord.append(((50,500),(150,500)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(350,250), end_pos=(500,250),width=1)
    coord.append(((350,250),(500,250)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(150,250), end_pos=(150,450),width=1)
    coord.append(((150,250),(150,450)))

    pygame.draw.line(surface=screen,color='black',start_pos=(150,350), end_pos=(300,350),width=1)
    coord.append(((150,350),(300,350)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(200,500), end_pos=(200,575),width=1)
    coord.append(((200,500),(200,575)))

    pygame.draw.line(surface=screen,color='black',start_pos=(200,575), end_pos=(350,575),width=1)
    coord.append(((200,575),(350,575)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(250,450), end_pos=(375,450),width=1)
    coord.append(((250,450),(375,450)))

    pygame.draw.line(surface=screen,color='black',start_pos=(375,450), end_pos=(375,300),width=1)
    coord.append(((375,450),(375,300)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(450,500), end_pos=(450,400),width=1)
    coord.append(((450,500),(450,400)))

    pygame.draw.line(surface=screen,color='black',start_pos=(450,400), end_pos=(500,400),width=1)
    coord.append(((450,400),(500,400)))

    pygame.draw.line(surface=screen,color='black',start_pos=(500,400), end_pos=(500,300),width=1)
    coord.append(((500,400),(500,300)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(450,150), end_pos=(700,150),width=1)
    coord.append(((450,150),(700,150)))

    pygame.draw.line(surface=screen,color='black',start_pos=(700,150), end_pos=(700,350),width=1)
    coord.append(((700,150),(700,350)))

    pygame.draw.line(surface=screen,color='black',start_pos=(700,350), end_pos=(550,350),width=1)
    coord.append(((700,350),(550,350)))

    pygame.draw.line(surface=screen,color='black',start_pos=(550,350), end_pos=(550,250),width=1)
    coord.append(((550,350),(550,250)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(550,600), end_pos=(550,450),width=1)
    coord.append(((550,600),(550,450)))

    pygame.draw.line(surface=screen,color='black',start_pos=(550,450), end_pos=(700,450),width=1)
    coord.append(((550,450),(700,450)))
    
    eat=[(325,125),(625,300),(300,525),(475,575),(450,350),(200,300),(100,600),(600,150)]
    
    return xmin,xmax,ymin,ymax,coord,eat,pozadina

def poligon3():
    deb=10
    xmin=50
    xmax=750
    ymin=50
    ymax=650
    coord=list()
    pozadina=pygame.image.load('c:/Users/hrvoj/OneDrive/Desktop/pacman/slika3.png')
    pygame.draw.polygon(surface=screen,color='black',points=[(xmin,ymin),(xmax,ymin),(xmax,ymax),(xmin,ymax)],width=deb)
    
    pygame.draw.line(surface=screen,color='black',start_pos=(150,50), end_pos=(150,100),width=1)
    coord.append(((150,50),(150,100)))
    
    pygame.draw.line(surface=screen,color='black',start_pos=(250,50), end_pos=(250,200),width=1)
    coord.append(((250,50),(250,200)))
    
    pygame.draw.line(surface=screen,color='black',start_pos=(525,50), end_pos=(525,100),width=1)
    coord.append(((525,50),(525,100)))

    pygame.draw.line(surface=screen,color='black',start_pos=(300,150), end_pos=(500,150),width=1)
    coord.append(((300,150),(500,150)))

    pygame.draw.line(surface=screen,color='black',start_pos=(500,150), end_pos=(500,200),width=1)
    coord.append(((500,150),(500,200)))

    pygame.draw.line(surface=screen,color='black',start_pos=(500,200), end_pos=(550,200),width=1)
    coord.append(((500,200),(550,200)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(50,150), end_pos=(200,150),width=1)
    coord.append(((50,150),(200,150)))

    pygame.draw.line(surface=screen,color='black',start_pos=(100,200), end_pos=(150,200),width=1)
    coord.append(((100,200),(150,200)))

    pygame.draw.line(surface=screen,color='black',start_pos=(100,200), end_pos=(100,300),width=1)
    coord.append(((100,200),(100,300)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(100,350), end_pos=(200,350),width=1)
    coord.append(((100,350),(200,350)))

    pygame.draw.line(surface=screen,color='black',start_pos=(200,250), end_pos=(200,550),width=1)
    coord.append(((200,250),(200,550)))

    pygame.draw.line(surface=screen,color='black',start_pos=(200,550), end_pos=(100,550),width=1)
    coord.append(((200,550),(100,550)))

    pygame.draw.line(surface=screen,color='black',start_pos=(100,550), end_pos=(100,400),width=1)
    coord.append(((100,550),(100,400)))

    pygame.draw.line(surface=screen,color='black',start_pos=(100,450), end_pos=(150,450),width=1)
    coord.append(((100,450),(150,450)))

    pygame.draw.line(surface=screen,color='black',start_pos=(100,400), end_pos=(150,400),width=1)
    coord.append(((100,400),(150,400)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(150,650), end_pos=(150,600),width=1)
    coord.append(((150,650),(150,600)))

    pygame.draw.line(surface=screen,color='black',start_pos=(150,600), end_pos=(250,600),width=1)
    coord.append(((150,600),(250,600)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(600,400), end_pos=(700,400),width=1)
    coord.append(((600,400),(700,400)))

    pygame.draw.line(surface=screen,color='black',start_pos=(600,400), end_pos=(600,500),width=1)
    coord.append(((600,400),(600,500)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(650,650), end_pos=(650,500),width=1)
    coord.append(((650,650),(650,500)))

    pygame.draw.line(surface=screen,color='black',start_pos=(650,550), end_pos=(700,550),width=1)
    coord.append(((650,550),(700,550)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(650,250), end_pos=(700,250),width=1)
    coord.append(((650,250),(700,250)))

    pygame.draw.line(surface=screen,color='black',start_pos=(700,350), end_pos=(700,250),width=1)
    coord.append(((700,350),(700,250)))

    pygame.draw.line(surface=screen,color='black',start_pos=(700,350), end_pos=(650,350),width=1)
    coord.append(((700,350),(650,350)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(300,450), end_pos=(300,600),width=1)
    coord.append(((300,450),(300,600)))

    pygame.draw.line(surface=screen,color='black',start_pos=(300,600), end_pos=(550,600),width=1)
    coord.append(((300,600),(550,600)))

    pygame.draw.line(surface=screen,color='black',start_pos=(550,600), end_pos=(550,550),width=1)
    coord.append(((550,600),(550,550)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(350,500), end_pos=(500,500),width=1)
    coord.append(((350,500),(500,500)))

    pygame.draw.line(surface=screen,color='black',start_pos=(500,500), end_pos=(500,400),width=1)
    coord.append(((500,500),(500,400)))

    pygame.draw.line(surface=screen,color='black',start_pos=(500,400), end_pos=(425,400),width=1)
    coord.append(((500,400),(425,400)))

    pygame.draw.line(surface=screen,color='black',start_pos=(425,400), end_pos=(425,450),width=1)
    coord.append(((425,400),(425,450)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(450,320), end_pos=(600,320),width=1)
    coord.append(((450,320),(600,320)))

    pygame.draw.line(surface=screen,color='black',start_pos=(600,320), end_pos=(600,100),width=1)
    coord.append(((600,320),(600,100)))

    pygame.draw.line(surface=screen,color='black',start_pos=(600,100), end_pos=(700,100),width=1)
    coord.append(((600,100),(700,100)))

    pygame.draw.line(surface=screen,color='black',start_pos=(700,200), end_pos=(700,100),width=1)
    coord.append(((700,200),(700,100)))

    pygame.draw.line(surface=screen,color='black',start_pos=(700,200), end_pos=(750,200),width=1)
    coord.append(((700,200),(750,200)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(250,250), end_pos=(250,400),width=1)
    coord.append(((250,250),(250,400)))

    pygame.draw.line(surface=screen,color='black',start_pos=(250,400), end_pos=(350,400),width=1)
    coord.append(((250,400),(350,400)))

    pygame.draw.line(surface=screen,color='black',start_pos=(350,300), end_pos=(350,400),width=1)
    coord.append(((350,300),(350,400)))

    pygame.draw.line(surface=screen,color='black',start_pos=(250,250), end_pos=(450,250),width=1)
    coord.append(((250,250),(450,250)))
    
    ####defniniramo poziciju hrane

    eat=[(200,100),(700,450),(500,550),(650,150),(425,200),(150,500),(690,480),(350,350),(475,100),(685,250)]
    
    return xmin,xmax,ymin,ymax,coord,eat,pozadina



def lovac_grafika(t1,t2): #ovdje su definirani skinovi za lovca i crtanje lovca
    
    lik=pygame.draw.rect(screen, (255,0,0), (t1, t2, 20, 20)) #crtanje lovca
    if nivo==1:
        lovac1= pygame.image.load('c:/Users/hrvoj/OneDrive/Desktop/pacman/lovac113.png')#skin za lovca
        screen.blit(lovac1,(t1,t2))                                                     #     
    if nivo==2:
        lovac2=pygame.image.load('c:/Users/hrvoj/OneDrive/Desktop/pacman/lovac114.png')
        screen.blit(lovac2,(t1,t2))
    if nivo==3:
        lovac3=pygame.image.load('c:/Users/hrvoj/OneDrive/Desktop/pacman/lovac115.png')
        screen.blit(lovac3,(t1,t2))
    
    return lik

def lovac2_grafika(t3,t4): #ovdje definirano crtanje drugog lovca
    lik=pygame.draw.rect(screen, (255,100,255), (t3, t4, 18, 18))
    
    
    
    return lik


def lik_grafika(p1,p2): #funkcija definira crtanje lika i njegovog skina
    
    lik=pygame.draw.rect(screen, (255,0,0), (p1, p2, 18, 18))
    #ovdje se crta
    
    
    #crtanje skina
    igr=pygame.image.load('c:/Users/hrvoj/OneDrive/Desktop/pacman/igrac.png')
    screen.blit(igr,(p1,p2))
    
    return lik

def hrana_grafika(x1,x2): #u ovoje se funkciji definira grafika hrane 
    
    food=pygame.draw.rect(screen, (0,0,0), (x1, x2,10,10))
    
    return food

def draw_start_menu(): #u ovoj se funkciji definira menu (ispisuje se ono sto nije u samoj igrici)
   """
   Funkcija koja crta main menu prozor
   """
   screen.fill((0, 0, 0))
   font = pygame.font.SysFont('arial', 40)
   title = font.render('Munch Master', True, (255, 255, 255)) #na pocetku se ispisuje naslov
   start_button = font.render('S - Start', True, (255, 255, 255)) #gumb za pocetak igre
   screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/2))
   screen.blit(start_button, (screen_width/2 - start_button.get_width()/2, screen_height/2 + start_button.get_height()/2))
   pygame.display.update()

def draw_game_over_screen(scr): #u ovoj se funkciji definira game over koji se ispisuje kad igrac izgubi
   """
   Funkcija koja crta game over prozor
   """
   screen.fill((0, 0, 0))
   font = pygame.font.SysFont('arial', 40)
   font1 = pygame.font.SysFont('arial', 30)
   title = font.render('Game Over', True, (255, 255, 255))
   for i in range(len(scr)):
       score = font1.render(scr[i][:-2], True, (255, 255, 255))
       screen.blit(score, (10,i*35))
   restart_button = font.render('R - Restart', True, (255, 255, 255))
   quit_button = font.render('Q - Quit', True, (255, 255, 255))
   screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/3))
   screen.blit(restart_button, (screen_width/2 - restart_button.get_width()/2, screen_height/1.9 + restart_button.get_height()))
   screen.blit(quit_button, (screen_width/2 - quit_button.get_width()/2, screen_height/2 + quit_button.get_height()/2))
   pygame.display.update()


def draw_game_win_screen(scr): #u ovoj se funkciji definira game over koji se ispisuje kad igrac izgubi
   """
   Funkcija koja crta game over prozor
   """
   screen.fill((0, 0, 0))
   font = pygame.font.SysFont('arial', 40)
   font1 = pygame.font.SysFont('arial', 30)
   title = font.render('Well done! You win!', True, (255, 255, 255))
   for i in range(len(scr)):
       score = font1.render(scr[i][:-2], True, (255, 255, 255))
       screen.blit(score, (10,i*35))
   restart_button = font.render('R - Restart', True, (255, 255, 255))
   quit_button = font.render('Q - Quit', True, (255, 255, 255))
   screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/3))
   screen.blit(restart_button, (screen_width/2 - restart_button.get_width()/2, screen_height/1.9 + restart_button.get_height()))
   screen.blit(quit_button, (screen_width/2 - quit_button.get_width()/2, screen_height/2 + quit_button.get_height()/2))
   pygame.display.update()




def lovac(p1,p2,t1,t2,norm='da'):
    """
    Funkcija koja gleda pozicije igraca i lovca i gleda kako da lovac
    najbrze stigne do igraca

    Parameters
    ----------
    p1 : int
        x koordinata igraca
    p2 : int
        y kooord igraca
    t1 : int
        x koordinata lovca
    t2 : int
        y koordinata lovca
    norm : str, optional
        ako se ne nalazi kod zidova onda se normalno krece norm=da,
        ako je kod zida i ne moze ici nabjrzim putem jer mu smeta porepreka onda gleda druge mogucnosti. 
        The default is 'da'

    """
    step=1
    l1=p1-t1;l2=p2-t2
    v1=1;v2=0
    kut=(l1*v1+l2*v2)/(np.sqrt(l1*l1+l2*l2)*np.sqrt(v1*v1+v2*v2))
    if norm=='da':
        if kut>=-0.5 and kut<=0.5:
            if p2<t2:
                t2-=step
            elif p2>t2:
                t2+=step
            else:
                t2=t2
        elif kut>=-0.86 and kut<=0.86:
            if p1<t1 and p2<t2:
                t1-=step
                t2-=step
            elif p1<t1 and p2>t2:
                t1-=step
                t2+=step
            elif p1>t1 and p2<t2:
                t1+=step
                t2-=step
            elif p1>t1 and p2>t2:
                t1+=step
                t2+=step
            else:
                t1=t1
                t2=t2
        else:
            if p1<t1:
                t1-=step
            elif p1>t1:
                t1+=step
            else:
                t1=t1
    elif norm=='ne':
        if kut>=-0.5 and kut<=0.5:
            if p1<t1:
                t1-=step
            elif p1>t1:
                t1+=step
            else:
                t1+=random.randint(-4,4)
        else:
            if p2<t2:
                t2-=step
            elif p2>t2:
                t2+=step
            else:
                t2+=random.randint(-4,4)
    else:
        t1=t1
        t2=t2
    return t1,t2

def sort_score(lista):#funkcija koja sortira high score

    t=list()
    for lj in lista:
        t.append([lj[0],int(lj[1])])
    t=sorted(t,key=lambda x:x[1], reverse=True)
    lista=list()
    br=0
    for l in t:
        lista.append('{} {} \n'.format(l[0],l[1]))
        br+=1
        if br==10:
            break
    return lista


def pozicije1(): #u ovoj se funkciji definiraju sve bitne varijable ze pocetne polozaje
    p1=50        #lovc1, lovca2 i igraca
    p2=50
    step=1

    deb=10

    t1=650
    t2=50
    t3=50
    t4=650
    br=0
    return p1,p2,step,deb,t1,t2,t3,t4,br


pygame.init()
from pygame import mixer
mixer.init()
fps=30

X=700;Y=600
fpsclock=pygame.time.Clock()
screen=pygame.display.set_mode((X,Y))
pygame.display.set_caption("Keyboard_Input")
pol=pygame.draw.polygon(surface=screen,color='black',points=[(50,50),(850,50),(50,750),(750,850)],width=10)
White=(255,255,255)


going=True

green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.SysFont('timesnewroman',  30)
text = font.render('Game over...', True, green, blue)
textwin = font.render('You win', True, blue, green)
textRect = text.get_rect()
textRect.center = (X // 2, Y // 2)



score=0
tic=time.time()


nivo = 1
game_state = 'start_menu'
screen_width = 800
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

#za unos imena igrača
user_text = ''

try:# za ispisivanje scora u datoteku
    #ako vec postoji neki score
    with open('score.txt', 'r') as file:
        temp=file.readlines()
        txt=[]
        if len(temp)==1:
            temp=temp[0].split(' ')
            txt.append([temp[0],int(temp[1])])
        else:
            for t in temp:
                t=str(t)
                t=t.split()
                txt.append([t[0],int(t[1])])
except:
    file=open('score.txt', 'w')
    txt=list()
    file.close()
    


while going: #kostur igice
    if game_state == "start_menu":
        mixer.music.stop()
        draw_start_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            player_x = 200
            player_y = 400
            game_state = "name"
            name=''
            game_over = False
            if nivo == 1:
                xmin,xmax,ymin,ymax,coords,eat,pozadina=poligon1() #definiranje za poligon1 velicinu, koordinate hrane i pozadina
                p1,p2,step,deb,t1,t2,t3,t4,br=pozicije1()
                P1=p1;P2=p2
                T1=t1;T2=t2
                T3=t3;T4=t4
            elif nivo == 2: #isto kao i za if nivo==1
                xmin,xmax,ymin,ymax,coords,eat,pozadina=poligon2()
                p1,p2,step,deb,t1,t2,t3,t4,br=pozicije1()
                P1=p1;P2=p2
                T1=t1;T2=t2
                T3=t3;T4=t4
                mixer.music.load('c:/Users/hrvoj/OneDrive/Desktop/pacman/drugi.mp3')
                mixer.music.play(-1)
                tic=time.time()
            elif nivo ==3: #isto kao i za if nivo==1
                xmin,xmax,ymin,ymax,coords,eat,pozadina=poligon3()
                p1,p2,step,deb,t1,t2,t3,t4,br=pozicije1()
                P1=p1;P2=p2
                T1=t1;T2=t2
                T3=t3;T4=t4
                mixer.music.load('c:/Users/hrvoj/OneDrive/Desktop/pacman/treci.mp3')
                mixer.music.play(-1)
                tic=time.time()
            else: #za izlazak iz igrice
                time.sleep(2)
                pygame.quit()
                sys.exit()
    
    elif game_state == "name":
        screen.fill((225, 225, 225))
        
        font = pygame.font.SysFont('arial', 40)
        title = font.render('unesi ime:', True, (0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN: 
                # provjera za brisanje slova
                if event.key == pygame.K_BACKSPACE: 
                    #brise zadnje uneseno slovo
                    user_text = user_text[:-1] 
                #ako je pritisnuto enter znaci da je gotovo upisivanje
                elif event.key ==pygame.K_RETURN:
                    game_state='game'
                    mixer.music.load('c:/Users/hrvoj/OneDrive/Desktop/pacman/prvi.mp3') #za stavljanje muzike
                    mixer.music.play(-1)
                    tic=time.time()
                else: #unosi novi znak
                    user_text += event.unicode
        screen.blit(title,(10,10))
        title = font.render(user_text, True, (0, 0, 0))
        screen.blit(title,(10,100))
        
        
    elif game_state == "game_over": #sto se dogodi kad igrac izgubi
        mixer.music.stop() #zaustavi se muzika
        with open('score.txt','r') as file:
            scr=file.readlines()
        draw_game_over_screen(scr) #ispisivanje score-a
        
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]: #ako pritisnemo restart vodi nas na main menu da mozemo ponovno pokrenuti igricu
            game_state = "start_menu"
            user_text=''
        if keys[pygame.K_q]:
            pygame.quit()
            exit()
    elif game_state=='win':
        with open('score.txt','r') as file:
            scr=file.readlines()
            
        draw_game_win_screen(temp)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]: #ako pritisnemo restart vodi nas na main menu da mozemo ponovno pokrenuti igricu
            game_state = "start_menu"
            user_text=''
        if keys[pygame.K_q]:
            pygame.quit()
            exit()
      
    elif game_state == "game": #ako je igrica pokrenuta
        P1=p1;P2=p2
        screen.fill(White)
        screen.blit(pozadina,(0,0))
        
        if nivo==1:
            xmin,xmax,ymin,ymax,coords,_eat,pozadina=poligon1()
        elif nivo==2:
            xmin,xmax,ymin,ymax,coords,_eat,pozadina=poligon2()
        elif nivo==3:
            xmin,xmax,ymin,ymax,coords,_eat,pozadina=poligon3()
        else:
            pygame.quit()
            sys.exit()
            
        
        t1,t2=lovac(p1,p2,t1,t2)
        lovac1=lovac_grafika(t1,t2)
        if any(lovac1.clipline(*line) for line in coords):
            t1=T1;t2=T2
            t1,t2=lovac(p1,p2,t1,t2,norm='ne')
            lovac1=lovac_grafika(t1,t2)
            if any(lovac1.clipline(*line) for line in coords):
                while (any(lovac1.clipline(*line) for line in coords)):
                    t1,t2=lovac(p1,p2,t1,t2,norm='rand')
                    lovac1=lovac_grafika(t1,t2)
                    if any(lovac1.clipline(*line) for line in coords):
                        t1=T1;t2=T2        
        T1=t1;T2=t2
        
        t3,t4=lovac(p1,p2,t3,t4)
        lovac2=lovac_grafika(t3,t4)
        
        if any(lovac2.clipline(*line) for line in coords):
            t3=T3;t4=T4
            t3,t4=lovac(p1,p2,t3,t4,norm='ne')
            lovac2=lovac_grafika(t3,t4)
            if any(lovac2.clipline(*line) for line in coords):
                while (any(lovac2.clipline(*line) for line in coords)):
                    t3,t4=lovac(p1,p2,t3,t4,norm='rand')
                    lovac2=lovac_grafika(t3,t4)
                    if any(lovac2.clipline(*line) for line in coords):
                        t3=T3;t4=T4 
        T3=t3;T4=t4
        
        lik=lik_grafika(p1,p2)
        I=False
        for i in range(len(eat)):
            food=hrana_grafika(eat[i][0],eat[i][1])
            collide = pygame.Rect.colliderect(lik, food)
            if collide:
                sound = pygame.mixer.Channel(2)
                eat_sound = mixer.Sound('c:/Users/hrvoj/OneDrive/Desktop/pacman/eat.mp3')
                sound.play(eat_sound)
                I=True
                II=i
                br+=1
                if br%2==0:
                    step+=1
                toc=time.time()
                score+=5000/(toc-tic)
        if I:
            eat.pop(II)
        
        # provjera za poraz
        if pygame.Rect.colliderect(lik,lovac1) or pygame.Rect.colliderect(lik,lovac2):
            screen.blit(text, textRect)
            pygame.display.update()
            with open('score.txt', 'w') as file: #ispisivanje scora u datoteku
                txt.append([user_text,round(score,0)])
                temp=sort_score(txt)
                file.writelines(temp)
                user_text=''
            #time.sleep(2)
            game_state='game_over'
        
        
        
        
        ###  PROVJERA ZA POBJEDU
        if len(eat)==0:
            textRect = text.get_rect()
            textRect.center = (X // 2, Y // 2)
            screen.blit(textwin,textRect)
            pygame.display.update()
            mixer.music.stop()
            time.sleep(2)
            nivo += 1
            if nivo == 1:
                xmin,xmax,ymin,ymax,coords,eat,pozadina=poligon1()
                p1,p2,step,deb,t1,t2,t3,t4,br=pozicije1()
                P1=p1;P2=p2
                T1=t1;T2=t2
                T3=t3;T4=t4
                mixer.music.load('c:/Users/hrvoj/OneDrive/Desktop/pacman/prvi.mp3')
                mixer.music.play(-1)
            elif nivo == 2:
                xmin,xmax,ymin,ymax,coords,eat,pozadina=poligon2()
                p1,p2,step,deb,t1,t2,t3,t4,br=pozicije1()
                P1=p1;P2=p2
                T1=t1;T2=t2
                T3=t3;T4=t4
                mixer.music.load('c:/Users/hrvoj/OneDrive/Desktop/pacman/drugi.mp3')
                mixer.music.play(-1)
                tic=time.time()
            elif nivo ==3:
                xmin,xmax,ymin,ymax,coords,eat,pozadina=poligon3()
                p1,p2,step,deb,t1,t2,t3,t4,br=pozicije1()
                P1=p1;P2=p2
                T1=t1;T2=t2
                T3=t3;T4=t4
                mixer.music.load('c:/Users/hrvoj/OneDrive/Desktop/pacman/drugi.mp3')
                mixer.music.play(-1)
                tic=time.time()
            else:
                game_state='win'
                with open('score.txt', 'w') as file: #ispisivanje scora u datoteku
                    txt.append([user_text,round(score,0)])
                    temp=sort_score(txt)
                    file.writelines(temp)
                    user_text=''
        
            
        
        for eve in pygame.event.get():
            if eve.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        key_input = pygame.key.get_pressed()  
        
        if key_input[pygame.K_LEFT]: #definira kretanje igraca
            if (p1 - step) <= xmin+5:
                p1=p1
            else:
                p1 -= step
        if key_input[pygame.K_UP]: #definira kretanje igraca
            if (p2 - step) < ymin + 5:
                p2=p2
            else:
                p2 -= step
        if key_input[pygame.K_RIGHT]: #definira kretanje igraca
            if (p1 + 2*deb + step) > xmax:
                p1=p1
            else:
                p1 += step
        if key_input[pygame.K_DOWN]: #definira kretanje igraca
            if (p2 + 2*deb + step) > ymax:
                p2=p2
            else:
                p2 += step
        
        lik=lik_grafika(p1,p2)
        if any(lik.clipline(*line) for line in coords): #provjera sjece li igrac zidove
            try:
                lik=lik_grafika(P1,p2)
                if not any(lik.clipline(*line) for line in coords):
                    1==2
                else:
                    p1=p1;p2=P2
            except:
                p1=P1;p2=P2
            try:
                lik=lik_grafika(p1,P2)
                if not any(lik.clipline(*line) for line in coords):
                    1==2
                else:
                    p1=P1;p2=p2
            except:
                p1=P1;p2=P2
            
      
    elif game_over:
        game_state = "game_over"
        game_over = False
    
    for event in pygame.event.get(): #definiranje izlaska iz igre
       if event.type == pygame.QUIT:
           pygame.quit()
           exit()
    
    pygame.display.update()
    fpsclock.tick(fps)
