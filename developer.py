def lovac(p1,p2,t1,t2,norm='da'):
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
        else:
            if p1<t1:
                t1-=step
            elif p1>t1:
                t1+=step
            else:
                t1=t1
    else:
        if kut>=-0.5 and kut<=0.5:
            if p1<t1:
                t1-=step
            elif p1>t1:
                t1+=step
            else:
                t1=t1
        else:
            if p2<t2:
                t2-=step
            elif p2>t2:
                t2+=step
            else:
                t2=t2
    return t1,t2




pygame.init()
fps=30

X=400;Y=300
fpsclock=pygame.time.Clock()
sur_obj=pygame.display.set_mode((X,Y))
pygame.display.set_caption("Keyboard_Input")
pol=pygame.draw.polygon(surface=sur_obj,color='black',points=[(50,50),(350,50),(50,350),(350,350)],width=10)
White=(255,255,255)
p1=50
p2=50
step=1
xmin=50
xmax=350
ymin=50
ymax=250
deb=10
t1=350
t2=250
going=True

green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.SysFont('timesnewroman',  30)
text = font.render('Game over...', True, green, blue)
textRect = text.get_rect()
textRect.center = (X // 2, Y // 2)

P1=p1;P2=p2
T1=t1;T2=t2
while going:
    P1=p1;P2=p2
    sur_obj.fill(White)
    
    xmin,xmax,ymin,ymax,coords=poligon()
    
    
    ######## LOVAC - s provjerom ###############
    t1,t2=lovac(p1,p2,t1,t2)
    lik=lovac_grafika(t1,t2)
    if any(lik.clipline(*line) for line in coords):
        t1=T1;t2=T2
        t1,t2=lovac(p1,p2,t1,t2,norm='ne')
        lik=lovac_grafika(t1,t2)
    T1=t1;T2=t2
    
    lik=lik_grafika(p1,p2)
    
    if p1==t1 and p2==t2:
        sur_obj.blit(text, textRect)
        pygame.display.update()
        time.sleep(5)
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
    
    
    pygame.display.update()
    fpsclock.tick(fps)