
def poligon1():   
    deb=10
    xmin=50
    xmax=750
    ymin=50
    ymax=650
    coord=list()
    pozadina=pygame.image.load('C:/Users/marta/Desktop/PYTHON/slika1.png')
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

    eat=[(350,350),(150,600),(400,250),(170,125),(680,360),(620,150)]
    
    return xmin,xmax,ymin,ymax,coord,eat,pozadina

def poligon2():     
    deb=10
    xmin=50
    xmax=750
    ymin=50
    ymax=650
    coord=list()
    pozadina=pygame.image.load('C:/Users/marta/Desktop/PYTHON/slika2.png')
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


def lovac_grafika(t1,t2): 
    
    lik=pygame.draw.rect(screen, (255,0,0), (t1, t2, 20, 20)) 
    if nivo==1:
        lovac1= pygame.image.load('c:/Users/hrvoj/OneDrive/Desktop/pacman/lovac113.png')
        screen.blit(lovac1,(t1,t2))                                                         
    if nivo==2:
        lovac2=pygame.image.load('c:/Users/hrvoj/OneDrive/Desktop/pacman/lovac114.png')
        screen.blit(lovac2,(t1,t2))
    if nivo==3:
        lovac3=pygame.image.load('c:/Users/hrvoj/OneDrive/Desktop/pacman/lovac115.png')
        screen.blit(lovac3,(t1,t2))
    
    return lik
