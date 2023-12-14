
def poligon3():
    deb=10
    xmin=50
    xmax=350
    ymin=50
    ymax=250
    coord=list()
    pygame.draw.polygon(surface=screen,color='black',points=[(xmin,ymin),(xmax,ymin),(xmax,ymax),(xmin,ymax)],width=deb)
    
    pygame.draw.line(surface=screen,color='black',start_pos=(75,85), end_pos=(75,200),width=1)
    coord.append(((75,85),(75,200)))
    
    pygame.draw.line(surface=screen,color='black',start_pos=(75,85), end_pos=(140,85),width=1)
    coord.append(((75,85),(140,85)))
    
    pygame.draw.line(surface=screen,color='black',start_pos=(85,100), end_pos=(130,100),width=1)
    coord.append(((85,100),(130,100)))

    #pygame.draw.line(surface=screen,color='black',start_pos=(130,101), end_pos=(130,75),width=1)
    #coord.append(((130,101),(130,75)))

    pygame.draw.line(surface=screen,color='black',start_pos=(175,210), end_pos=(175,110),width=1)
    coord.append(((175,210),(175,110)))

    pygame.draw.line(surface=screen,color='black',start_pos=(220,100), end_pos=(300,100),width=1)
    coord.append(((220,100),(300,100)))

    pygame.draw.line(surface=screen,color='black',start_pos=(300,125), end_pos=(300,210),width=1)
    coord.append(((300,125),(300,125)))

    pygame.draw.line(surface=screen,color='black',start_pos=(300,210), end_pos=(250,210),width=1)
    coord.append(((300,210),(250,210)))

    pygame.draw.line(surface=screen,color='black',start_pos=(130,130), end_pos=(130,200),width=1)
    coord.append(((130,130),(130,200)))

    pygame.draw.line(surface=screen,color='black',start_pos=(100,200), end_pos=(100,225),width=1)
    coord.append(((100,200),(100,225)))

    pygame.draw.line(surface=screen,color='black',start_pos=(100,225), end_pos=(170,225),width=1)
    coord.append(((100,225),(170,225)))

    pygame.draw.line(surface=screen,color='black',start_pos=(250,150), end_pos=(250,250),width=1)
    coord.append(((250,150),(250,250)))

    #pygame.draw.line(surface=screen,color='black',start_pos=(185,150), end_pos=(185,200),width=1)
    #coord.append(((185,150),(185,200)))

    pygame.draw.line(surface=screen,color='black',start_pos=(210,250), end_pos=(210,200),width=1)
    coord.append(((210,250),(210,200)))

    pygame.draw.line(surface=screen,color='black',start_pos=(190,50), end_pos=(190,100),width=1)
    coord.append(((190,50),(190,100)))

    pygame.draw.line(surface=screen,color='black',start_pos=(320,50), end_pos=(320,100),width=1)
    coord.append(((320,50),(320,100)))

    #pygame.draw.line(surface=screen,color='black',start_pos=(190,85), end_pos=(190,125),width=1)
    #coord.append(((190,85),(190,125)))

    #pygame.draw.line(surface=screen,color='black',start_pos=(210,150), end_pos=(240,150),width=1)
    #coord.append(((210,150),(240,150)))

    #pygame.draw.line(surface=screen,color='black',start_pos=(240,150), end_pos=(240,225),width=1)
    #coord.append(((240,150),(240,225)))

    #pygame.draw.line(surface=screen,color='black',start_pos=(310,250), end_pos=(310,220),width=1)
    #coord.append(((310,250),(310,220)))

    #pygame.draw.line(surface=screen,color='black',start_pos=(275,200), end_pos=(325,200),width=1)
    #coord.append(((275,200),(325,200)))

    #pygame.draw.line(surface=screen,color='black',start_pos=(275,200), end_pos=(275,225),width=1)
    #coord.append(((275,200),(275,225)))

    pygame.draw.line(surface=screen,color='black',start_pos=(320,80), end_pos=(320,170),width=1)
    coord.append(((320,80),(320,170)))

    #pygame.draw.line(surface=screen,color='black',start_pos=(320,170), end_pos=(275,170),width=1)
    #coord.append(((320,170),(275,170)))

    pygame.draw.line(surface=screen,color='black',start_pos=(230,80), end_pos=(300,80),width=1)
    coord.append(((230,80),(300,80)))

    #pygame.draw.line(surface=screen,color='black',start_pos=(230,115), end_pos=(290,115),width=1)
    #coord.append(((230,115),(290,115)))

    pygame.draw.line(surface=screen,color='black',start_pos=(265,115), end_pos=(265,150),width=1)
    coord.append(((265,115),(265,150)))

    pygame.draw.line(surface=screen,color='black',start_pos=(200,150), end_pos=(250,150),width=1)
    coord.append(((200,150),(250,150)))
    
    ####defniniramo poziciju hrane

    eat=[(60,235),(300,100),(60,150),(250,200)]
    
    return xmin,xmax,ymin,ymax,coord,eat

def lovac_grafika(t1,t2):
    
    lik=pygame.draw.rect(screen, (255,100,255), (t1, t2, 10, 10))
    
    return lik
def lovac2_grafika(t3,t4):
    lik=pygame.draw.rect(screen, (255,100,255), (t3, t4, 10, 10))
    return lik


def lik_grafika(p1,p2):
    
    lik=pygame.draw.rect(screen, (255,0,0), (p1, p2, 10, 10))
    
    return lik

def hrana_grafika(x1,x2):
    
    food=pygame.draw.rect(screen, (0,0,0), (x1, x2,5,5))
    
    return food

def draw_start_menu():
   screen.fill((0, 0, 0))
   font = pygame.font.SysFont('arial', 40)
   title = font.render('My Game', True, (255, 255, 255))
   start_button = font.render('S - Start', True, (255, 255, 255))
   screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/2))
   screen.blit(start_button, (screen_width/2 - start_button.get_width()/2, screen_height/2 + start_button.get_height()/2))
   pygame.display.update()

def draw_game_over_screen():
   screen.fill((0, 0, 0))
   font = pygame.font.SysFont('arial', 40)
   title = font.render('Game Over', True, (255, 255, 255))
   restart_button = font.render('R - Restart', True, (255, 255, 255))
   quit_button = font.render('Q - Quit', True, (255, 255, 255))
   screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/3))
   screen.blit(restart_button, (screen_width/2 - restart_button.get_width()/2, screen_height/1.9 + restart_button.get_height()))
   screen.blit(quit_button, (screen_width/2 - quit_button.get_width()/2, screen_height/2 + quit_button.get_height()/2))
   pygame.display.update()
