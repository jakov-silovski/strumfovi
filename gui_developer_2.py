def poligon3():
    deb=10
    xmin=50
    xmax=750
    ymin=50
    ymax=650
    coord=list()
    pozadina=pygame.image.load('C:/Users/eva/Desktop/pacman/slika3.png')
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

    pygame.draw.line(surface=screen,color='black',start_pos=(50,150), end_pos=(200,150),width=1)
    coord.append(((50,150),(200,150)))

    pygame.draw.line(surface=screen,color='black',start_pos=(100,200), end_pos=(150,200),width=1)
    coord.append(((100,200),(150,200)))

    pygame.draw.line(surface=screen,color='black',start_pos=(100,200), end_pos=(100,300),width=1)
    coord.append(((100,200),(100,300)))

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

    pygame.draw.line(surface=screen,color='black',start_pos=(150,650), end_pos=(150,600),width=1)
    coord.append(((150,650),(150,600)))

    pygame.draw.line(surface=screen,color='black',start_pos=(150,600), end_pos=(250,600),width=1)
    coord.append(((150,600),(250,600)))

    pygame.draw.line(surface=screen,color='black',start_pos=(600,400), end_pos=(700,400),width=1)
    coord.append(((600,400),(700,400)))

    pygame.draw.line(surface=screen,color='black',start_pos=(600,400), end_pos=(600,500),width=1)
    coord.append(((600,400),(600,500)))

    pygame.draw.line(surface=screen,color='black',start_pos=(650,650), end_pos=(650,500),width=1)
    coord.append(((650,650),(650,500)))

    pygame.draw.line(surface=screen,color='black',start_pos=(650,550), end_pos=(700,550),width=1)
    coord.append(((650,550),(700,550)))

    pygame.draw.line(surface=screen,color='black',start_pos=(650,250), end_pos=(700,250),width=1)
    coord.append(((650,250),(700,250)))

    pygame.draw.line(surface=screen,color='black',start_pos=(700,350), end_pos=(700,250),width=1)
    coord.append(((700,350),(700,250)))

    pygame.draw.line(surface=screen,color='black',start_pos=(700,350), end_pos=(650,350),width=1)
    coord.append(((700,350),(650,350)))

    pygame.draw.line(surface=screen,color='black',start_pos=(300,450), end_pos=(300,600),width=1)
    coord.append(((300,450),(300,600)))

    pygame.draw.line(surface=screen,color='black',start_pos=(300,600), end_pos=(550,600),width=1)
    coord.append(((300,600),(550,600)))

    pygame.draw.line(surface=screen,color='black',start_pos=(550,600), end_pos=(550,550),width=1)
    coord.append(((550,600),(550,550)))

    pygame.draw.line(surface=screen,color='black',start_pos=(350,500), end_pos=(500,500),width=1)
    coord.append(((350,500),(500,500)))

    pygame.draw.line(surface=screen,color='black',start_pos=(500,500), end_pos=(500,400),width=1)
    coord.append(((500,500),(500,400)))

    pygame.draw.line(surface=screen,color='black',start_pos=(500,400), end_pos=(425,400),width=1)
    coord.append(((500,400),(425,400)))

    pygame.draw.line(surface=screen,color='black',start_pos=(425,400), end_pos=(425,450),width=1)
    coord.append(((425,400),(425,450)))

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

    pygame.draw.line(surface=screen,color='black',start_pos=(250,250), end_pos=(250,400),width=1)
    coord.append(((250,250),(250,400)))

    pygame.draw.line(surface=screen,color='black',start_pos=(250,400), end_pos=(350,400),width=1)
    coord.append(((250,400),(350,400)))

    pygame.draw.line(surface=screen,color='black',start_pos=(350,300), end_pos=(350,400),width=1)
    coord.append(((350,300),(350,400)))

    pygame.draw.line(surface=screen,color='black',start_pos=(250,250), end_pos=(450,250),width=1)
    coord.append(((250,250),(450,250)))

    eat=[(200,100),(700,450),(500,550),(650,150),(425,200),(150,500),(690,480),(350,350),(475,100),(685,250)]
    
    return xmin,xmax,ymin,ymax,coord,eat,pozadina



def lovac2_grafika(t3,t4):
    lik=pygame.draw.rect(screen, (255,100,255), (t3, t4, 18, 18))
    return lik


def lik_grafika(p1,p2): 
    
    lik=pygame.draw.rect(screen, (255,0,0), (p1, p2, 18, 18))
    

    igr=pygame.image.load('c:/Users/eva/Desktop/pacman/igrac.png')
    screen.blit(igr,(p1,p2))
    
    return lik

def hrana_grafika(x1,x2): 
    
    food=pygame.draw.rect(screen, (0,0,0), (x1, x2,5,5))
    
    return food

def draw_start_menu(): 
   """
   Funkcija koja crta main menu prozor
   """
   screen.fill((0, 0, 0))
   font = pygame.font.SysFont('arial', 40)
   title = font.render('Munch Master', True, (255, 255, 255)) 
   start_button = font.render('S - Start', True, (255, 255, 255)) 
   screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2 - title.get_height()/2))
   screen.blit(start_button, (screen_width/2 - start_button.get_width()/2, screen_height/2 + start_button.get_height()/2))
   pygame.display.update()

def draw_game_over_screen(scr): 
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