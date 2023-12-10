pygame.init()
from pygame import mixer
mixer.init()
fps=30

X=400;Y=300
fpsclock=pygame.time.Clock()
screen=pygame.display.set_mode((X,Y))
pygame.display.set_caption("Keyboard_Input")
pol=pygame.draw.polygon(surface=screen,color='black',points=[(50,50),(350,50),(50,350),(350,350)],width=10)
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
screen_width = 750
screen_height = 450
screen = pygame.display.set_mode((screen_width, screen_height))


while going:
    
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           exit()
    if game_state == "start_menu":
        mixer.music.stop()
        draw_start_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            player_x = 200
            player_y = 400
            game_state = "game"
            game_over = False
            if nivo == 1:
                xmin,xmax,ymin,ymax,coords,eat=poligon1()
                p1,p2,step,deb,t1,t2,t3,t4,br=pozicije1()
                P1=p1;P2=p2
                T1=t1;T2=t2
                T3=t3;T4=t4
                mixer.music.load('prvi.mp3')
                mixer.music.play(-1)
                tic=time.time()
            elif nivo == 2:
                xmin,xmax,ymin,ymax,coords,eat=poligon2()
                p1,p2,step,deb,t1,t2,t3,t4,br=pozicije1()
                P1=p1;P2=p2
                T1=t1;T2=t2
                T3=t3;T4=t4
                mixer.music.load('drugi.mp3')
                mixer.music.play(-1)
                tic=time.time()
            elif nivo ==3:
                xmin,xmax,ymin,ymax,coords,eat=poligon3()
                p1,p2,step,deb,t1,t2,t3,t4,br=pozicije1()
                P1=p1;P2=p2
                T1=t1;T2=t2
                T3=t3;T4=t4
                mixer.music.load('drugi.mp3')
                mixer.music.play(-1)
                tic=time.time()
            else:
                time.sleep(2)
                pygame.quit()
                sys.exit()
    elif game_state == "game_over":
        mixer.music.stop()
        draw_game_over_screen()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_state = "start_menu"
        if keys[pygame.K_q]:
            pygame.quit()
            exit()
      
    elif game_state == "game":
        P1=p1;P2=p2
        screen.fill(White)
        
        if nivo==1:
            xmin,xmax,ymin,ymax,coords,_eat=poligon1()
        elif nivo==2:
            xmin,xmax,ymin,ymax,coords,_eat=poligon2()
        elif nivo==3:
            xmin,xmax,ymin,ymax,coords,_eat=poligon3()
        else:
            pygame.quit()
            sys.exit()
            
        
        
        ######## LOVAC - s provjerom ###############
        t1,t2=lovac(p1,p2,t1,t2)
        lik=lovac_grafika(t1,t2)
        if any(lik.clipline(*line) for line in coords):
            t1=T1;t2=T2
            t1,t2=lovac(p1,p2,t1,t2,norm='ne')
            lik=lovac_grafika(t1,t2)
            if any(lik.clipline(*line) for line in coords):
                t1=T1;t2=T2
        T1=t1;T2=t2
        
        t3,t4=lovac(p1,p2,t3,t4)
        lik=lovac_grafika(t3,t4)
        if any(lik.clipline(*line) for line in coords):
            t3=T3;t4=T4
            t3,t4=lovac(p1,p2,t3,t4,norm='ne')
            lik=lovac_grafika(t3,t4)
            if any(lik.clipline(*line) for line in coords):
                t3=T3;t4=T4
        T3=t3;T4=t4
        
        lik=lik_grafika(p1,p2)
        I=False
        for i in range(len(eat)):
            food=hrana_grafika(eat[i][0],eat[i][1])
            collide = pygame.Rect.colliderect(lik, food)
            if collide:
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
        if (p1==t1 and p2==t2) or (p1==t3 and p2==t4):
            screen.blit(text, textRect)
            pygame.display.update()
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
                xmin,xmax,ymin,ymax,coords,eat=poligon1()
                p1,p2,step,deb,t1,t2,t3,t4,br=pozicije1()
                P1=p1;P2=p2
                T1=t1;T2=t2
                T3=t3;T4=t4
                mixer.music.load('prvi.mp3')
                mixer.music.play(-1)
            elif nivo == 2:
                xmin,xmax,ymin,ymax,coords,eat=poligon2()
                p1,p2,step,deb,t1,t2,t3,t4,br=pozicije1()
                P1=p1;P2=p2
                T1=t1;T2=t2
                T3=t3;T4=t4
                mixer.music.load('drugi.mp3')
                mixer.music.play(-1)
                tic=time.time()
            elif nivo ==3:
                xmin,xmax,ymin,ymax,coords,eat=poligon3()
                p1,p2,step,deb,t1,t2,t3,t4,br=pozicije1()
                P1=p1;P2=p2
                T1=t1;T2=t2
                T3=t3;T4=t4
                mixer.music.load('drugi.mp3')
                mixer.music.play(-1)
                tic=time.time()
            else:
                print(score)
                time.sleep(2)
                pygame.quit()
                sys.exit()
        
            
        
        for eve in pygame.event.get():
            if eve.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        key_input = pygame.key.get_pressed()  
        
        if key_input[pygame.K_LEFT]:
            if (p1 - step) <= xmin:
                p1=p1
            else:
                p1 -= step
        if key_input[pygame.K_UP]:
            if (p2 - step) < ymin:
                p2=p2
            else:
                p2 -= step
        if key_input[pygame.K_RIGHT]:
            if (p1 + step) > xmax:
                p1=p1
            else:
                p1 += step
        if key_input[pygame.K_DOWN]:
            if (p2 + step) > ymax:
                p2=p2
            else:
                p2 += step
        
        lik=lik_grafika(p1,p2)
        if any(lik.clipline(*line) for line in coords):
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
    
    
    
    
    pygame.display.update()
    fpsclock.tick(fps)
