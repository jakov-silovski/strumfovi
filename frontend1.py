def poligon():
    coord=list()
    pygame.draw.polygon(surface=sur_obj,color='black',points=[(xmin,ymin),(xmax,ymin),(xmax,ymax),(xmin,ymax)],width=deb)
    
    pygame.draw.line(surface=sur_obj,color='black',start_pos=(200,200), end_pos=(200,150),width=1)
    coord.append(((200,200),(200,150)))
    
    pygame.draw.line(surface=sur_obj,color='black',start_pos=(250,250), end_pos=(250,150),width=1)
    coord.append(((250,250),(250,150)))
    
    pygame.draw.line(surface=sur_obj,color='black',start_pos=(100,100), end_pos=(200,100),width=1)
    coord.append(((100,100),(200,100)))
    
    return xmin,xmax,ymin,ymax,coord