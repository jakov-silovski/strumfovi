
def poligon1():
    deb=10
    xmin=50
    xmax=350
    ymin=50
    ymax=250
    coord=list()
    pygame.draw.polygon(surface=screen,color='black',points=[(xmin,ymin),(xmax,ymin),(xmax,ymax),(xmin,ymax)],width=deb)
    
    pygame.draw.line(surface=screen,color='black',start_pos=(150,50), end_pos=(150,100),width=1)
    coord.append(((150,50),(150,100)))
    
    pygame.draw.line(surface=screen,color='black',start_pos=(150,250), end_pos=(150,200),width=1)
    coord.append(((150,250),(150,200)))
    
    pygame.draw.line(surface=screen,color='black',start_pos=(250,50), end_pos=(250,100),width=1)
    coord.append(((250,50),(250,100)))

    pygame.draw.line(surface=screen,color='black',start_pos=(250,250), end_pos=(250,200),width=1)
    coord.append(((250,250),(250,200)))

    pygame.draw.line(surface=screen,color='black',start_pos=(175,100), end_pos=(225,100),width=1)
    coord.append(((175,100),(225,100)))

    pygame.draw.line(surface=screen,color='black',start_pos=(175,200), end_pos=(225,200),width=1)
    coord.append(((175,200),(225,200)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(80,100), end_pos=(80,140),width=1)
    coord.append(((80,100),(80,140)))    # ovdje je pisalo (80,150)

    pygame.draw.line(surface=screen,color='black',start_pos=(80,100), end_pos=(110,100),width=1)
    coord.append(((80,100),(110,100)))

    pygame.draw.line(surface=screen,color='black',start_pos=(80,160), end_pos=(80,200),width=1)
    coord.append(((80,160),(80,200)))

    pygame.draw.line(surface=screen,color='black',start_pos=(80,200), end_pos=(110,200),width=1)
    coord.append(((80,200),(110,200)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(320,100), end_pos=(320,140),width=1)
    coord.append(((320,100),(320,140)))

    pygame.draw.line(surface=screen,color='black',start_pos=(290,100), end_pos=(320,100),width=1)
    coord.append(((290,100),(320,100)))

    pygame.draw.line(surface=screen,color='black',start_pos=(320,160), end_pos=(320,200),width=1)
    coord.append(((320,160),(320,200)))  #prvi (320,100),(320,160)

    pygame.draw.line(surface=screen,color='black',start_pos=(290,200), end_pos=(320,200),width=1)
    coord.append(((290,200),(320,200)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(140,140), end_pos=(100,140),width=1)
    coord.append(((140,140),(100,140))) #prvi (150,140)

    pygame.draw.line(surface=screen,color='black',start_pos=(140,160), end_pos=(100,160),width=1)
    coord.append(((140,160),(100,160))) #prvi (150,160)
#
    pygame.draw.line(surface=screen,color='black',start_pos=(260,140), end_pos=(300,140),width=1)
    coord.append(((260,140),(300,140)))

    pygame.draw.line(surface=screen,color='black',start_pos=(260,160), end_pos=(300,160),width=1)
    coord.append(((260,160),(300,160)))
#
    pygame.draw.line(surface=screen,color='black',start_pos=(175,130), end_pos=(225,130),width=1)
    coord.append(((175,130),(225,130)))

    pygame.draw.line(surface=screen,color='black',start_pos=(175,170), end_pos=(190,170),width=1)
    coord.append(((175,170),(190,170)))

    pygame.draw.line(surface=screen,color='black',start_pos=(210,170), end_pos=(225,170),width=1)
    coord.append(((210,170),(225,170)))

    pygame.draw.line(surface=screen,color='black',start_pos=(175,130), end_pos=(175,170),width=1)
    coord.append(((175,130),(175,170)))

    pygame.draw.line(surface=screen,color='black',start_pos=(225,130), end_pos=(225,170),width=1)
    coord.append(((225,130),(225,170)))

    
    #defniniramo poziciju hrane

    eat=[(200,150),(320,70),(60,150),(270,210),(125,300),(200, 80),(210,230),(110,115),(330,50),(120,210),(280,150)]
    
    return xmin,xmax,ymin,ymax,coord,eat


def poligon2():
    deb=10
    xmin=50
    xmax=350
    ymin=50
    ymax=250
    coord=list()
    pygame.draw.polygon(surface=screen,color='black',points=[(xmin,ymin),(xmax,ymin),(xmax,ymax),(xmin,ymax)],width=deb)
    
    pygame.draw.line(surface=screen,color='black',start_pos=(50,100), end_pos=(75,100),width=1)
    coord.append(((50,100),(75,100)))
    
    pygame.draw.line(surface=screen,color='black',start_pos=(50,200), end_pos=(75,200),width=1)
    coord.append(((50,200),(75,200)))
    
    pygame.draw.line(surface=screen,color='black',start_pos=(75,225), end_pos=(75,250),width=1)
    coord.append(((75,225),(75,250)))

    pygame.draw.line(surface=screen,color='black',start_pos=(75,125), end_pos=(75,175),width=1)
    coord.append(((75,125),(75,175)))

    pygame.draw.line(surface=screen,color='black',start_pos=(75,150), end_pos=(125,150),width=1)
    coord.append(((75,150),(125,150)))

    pygame.draw.line(surface=screen,color='black',start_pos=(90,50), end_pos=(90,125),width=1)
    coord.append(((90,50),(90,125)))

    pygame.draw.line(surface=screen,color='black',start_pos=(110,125), end_pos=(160,125),width=1)
    coord.append(((110,125),(160,125)))

    pygame.draw.line(surface=screen,color='black',start_pos=(160,125), end_pos=(160,175),width=1)
    coord.append(((160,125),(160,175)))

    pygame.draw.line(surface=screen,color='black',start_pos=(110,175), end_pos=(160,175),width=1)
    coord.append(((110,175),(160,175)))

    pygame.draw.line(surface=screen,color='black',start_pos=(100,200), end_pos=(100,225),width=1)
    coord.append(((100,200),(100,225)))

    pygame.draw.line(surface=screen,color='black',start_pos=(100,225), end_pos=(170,225),width=1)
    coord.append(((100,225),(170,225)))

    pygame.draw.line(surface=screen,color='black',start_pos=(125,200), end_pos=(185,200),width=1)
    coord.append(((125,200),(185,200)))

    pygame.draw.line(surface=screen,color='black',start_pos=(185,150), end_pos=(185,200),width=1)
    coord.append(((185,150),(185,200)))

    pygame.draw.line(surface=screen,color='black',start_pos=(210,250), end_pos=(210,200),width=1)
    coord.append(((210,250),(210,200)))

    pygame.draw.line(surface=screen,color='black',start_pos=(210,50), end_pos=(210,100),width=1)
    coord.append(((210,50),(210,100)))

    pygame.draw.line(surface=screen,color='black',start_pos=(110,85), end_pos=(190,85),width=1)
    coord.append(((110,85),(190,85)))

    pygame.draw.line(surface=screen,color='black',start_pos=(190,85), end_pos=(190,125),width=1)
    coord.append(((190,85),(190,125)))

    pygame.draw.line(surface=screen,color='black',start_pos=(210,150), end_pos=(240,150),width=1)
    coord.append(((210,150),(240,150)))

    pygame.draw.line(surface=screen,color='black',start_pos=(240,150), end_pos=(240,225),width=1)
    coord.append(((240,150),(240,225)))

    pygame.draw.line(surface=screen,color='black',start_pos=(310,250), end_pos=(310,220),width=1)
    coord.append(((310,250),(310,220)))

    pygame.draw.line(surface=screen,color='black',start_pos=(275,200), end_pos=(325,200),width=1)
    coord.append(((275,200),(325,200)))

    pygame.draw.line(surface=screen,color='black',start_pos=(275,200), end_pos=(275,225),width=1)
    coord.append(((275,200),(275,225)))

    pygame.draw.line(surface=screen,color='black',start_pos=(320,80), end_pos=(320,170),width=1)
    coord.append(((320,80),(320,170)))

    pygame.draw.line(surface=screen,color='black',start_pos=(320,170), end_pos=(275,170),width=1)
    coord.append(((320,170),(275,170)))

    pygame.draw.line(surface=screen,color='black',start_pos=(230,80), end_pos=(300,80),width=1)
    coord.append(((230,80),(300,80)))

    pygame.draw.line(surface=screen,color='black',start_pos=(230,115), end_pos=(290,115),width=1)
    coord.append(((230,115),(290,115)))

    pygame.draw.line(surface=screen,color='black',start_pos=(290,115), end_pos=(290,150),width=1)
    coord.append(((290,115),(290,150)))

    pygame.draw.line(surface=screen,color='black',start_pos=(270,150), end_pos=(290,150),width=1)
    coord.append(((270,150),(290,150)))
    
    #defniniramo poziciju hrane

    eat=[(60,235),(300,100),(60,150),(250,200),(125,300),(100,75),(200,150),(200, 100), (180,210),(335,230),(130,160)]
    
    return xmin,xmax,ymin,ymax,coord,eat
