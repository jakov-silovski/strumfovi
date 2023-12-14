
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
        if random.randint(0,1)==0:
            t1+=random.randint(-4,4) 
        else:
            t2+=random.randint(-4,4)
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
                eat_sound = mixer.Sound('eat.mp3')
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
                print(score)
                time.sleep(2)
                pygame.quit()
                sys.exit()
        
            
        
        for eve in pygame.event.get():
            if eve.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        key_input = pygame.key.get_pressed()  
        
        if key_input[pygame.K_LEFT]: #definira kretanje igraca
            if (p1 - step) <= xmin:
                p1=p1
            else:
                p1 -= step
        if key_input[pygame.K_UP]: #definira kretanje igraca
            if (p2 - step) < ymin:
                p2=p2
            else:
                p2 -= step
        if key_input[pygame.K_RIGHT]: #definira kretanje igraca
            if (p1 + step) > xmax:
                p1=p1
            else:
                p1 += step
        if key_input[pygame.K_DOWN]: #definira kretanje igraca
            if (p2 + step) > ymax:
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
