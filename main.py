import pygame, asyncio
import random
import time

"""
Nota:
As variáveis que mencionam "gato 3; g3; ou outros relacionados" referem-se
ao sprite da ratoeira. Inicialmente a ratoeira era um gato como os outros, quando
foi alterado as variáveis mantiveram-se, só foi mudado o sprite
"""

#Inicializar o Pygame  
pygame.init()  

#Configurações da janela  
LARGURA=800
ALTURA=600  
janela=pygame.display.set_mode((LARGURA, ALTURA))  
pygame.display.set_caption("Cheese Chase")  

#Música de Fundo
pygame.mixer.music.load("goofyahhmusic.mp3")
pygame.mixer.music.play(-1)


async def main():
    pos_xr,pos_yr=350,500
    pos_x,pos_y=0,0

    #Fontes:
    fonte_tempo=pygame.font.Font(None, 50)
    fonte_pontos=pygame.font.Font(None, 50)

    #Rato:
    rato=pygame.image.load("rato.png")
    rato=pygame.transform.scale(rato,(70,70))
    rectrato=rato.get_rect()

    #Gatos:
    gatogordo=pygame.image.load("gatogordo.png")
    gatogordo=pygame.transform.scale(gatogordo,(200,200))
    rectgatogordo=gatogordo.get_rect()

    gato1=pygame.image.load("gato.png")
    gato1=pygame.transform.scale(gato1,(100,100))
    rectgato1=gato1.get_rect()

    gato2=pygame.image.load("gato.png")
    gato2=pygame.transform.scale(gato2,(100,100))
    rectgato2=gato2.get_rect()

    gato3=pygame.image.load("ratoeira.png")
    gato3=pygame.transform.scale(gato3,(80,80))
    rectgato3=gato3.get_rect()

    gato4=pygame.image.load("gato.png")
    gato4=pygame.transform.scale(gato4,(100,100))
    rectgato4=gato4.get_rect()

    #Queijo:
    queijo=pygame.image.load("queijo.png")
    queijo=pygame.transform.scale(queijo,(50,50))
    rectqueijo=queijo.get_rect()

    pontos=0

    #Fundo:
    fundo=pygame.image.load("fundo.png")

    jogoIniciado=False

    #Barreiras:
    barreiraup=pygame.Rect(0,0,800,1)
    pygame.draw.rect(fundo,(155,78,0),barreiraup)

    barreiradown=pygame.Rect(0,599,800,1)
    pygame.draw.rect(fundo,(155,78,0),barreiradown)

    barreiraleft=pygame.Rect(0,0,1,600)
    pygame.draw.rect(fundo,(155,78,0),barreiraleft)

    barreiraright=pygame.Rect(799,0,1,600)
    pygame.draw.rect(fundo,(155,78,0),barreiraright)

    def menu():
        fundo=pygame.image.load("menu.png")
        janela.blit(fundo,(pos_x, pos_y))

    def gameover():
        fundo=pygame.image.load("gameover.png")
        fundo=pygame.transform.scale(fundo,(600,400)) 
        pos_x,pos_y=100,100
        janela.blit(fundo,(pos_x, pos_y))

    def pausa():
        fundo=pygame.image.load("pause.png")
        fundo=pygame.transform.scale(fundo,(600,400)) 
        pos_x,pos_y=100,100
        janela.blit(fundo,(pos_x, pos_y))

    #Posicionamento Queijo:
    pos_xq=random.randint(0,710)
    pos_yq=-70
    velocidadequeijo=4
    queijovisivel=True

    #Posicionamento Gatos:
    pos_xg1=random.randint(0,710)
    pos_xg2=random.randint(0,710)
    pos_xg3=random.randint(0,710)
    pos_xg4=random.randint(0,710)
    pos_xgg=random.randint(0,610)

    pos_yg1=-90
    pos_yg2=-90
    pos_yg3=-90
    pos_yg4=-90
    pos_ygg=-185

    velocidadegato=4
    velocidadegatog=2
    gato1visivel=True
    gato2visivel=True
    gato3visivel=True
    gato4visivel=True
    gatogvisivel=True

    g2existe=False
    g3existe=False
    g4existe=False
    ggexiste=False

    gameoverestado=False

    # Loop principal  
    correr=True
    mostrar_pontos=False
    mostrar_tempo=False

    # Iniializacao de tempos
    t0=0
    t1=0
    tempo_de_jogo=0
    tempo_decorrido=0

    menu()
    
    while correr:
        for algo in pygame.event.get():  
            if algo.type==pygame.QUIT:  
                correr=False 

        teclas=pygame.key.get_pressed()

        #Pausa o jogo:
        if teclas[pygame.K_p]:
            pausa()
            jogoIniciado=False
            tempo_decorrido=tempo_de_jogo

        #Inicia o jogo:
        if teclas[pygame.K_SPACE] and gameoverestado == False:
            janela.blit(fundo,(pos_x, pos_y))
            jogoIniciado=True
            pausaestado=False
            t1=time.time()

        if jogoIniciado:
            tempo_de_jogo=round(t0-t1)+tempo_decorrido
            t0=time.time()

        #Sair para o menu:
        if teclas[pygame.K_q]:
            menu()
            pontos=0
            pos_xr,pos_yr=350,500
            queijovisivel=False
            jogoIniciado=False
            tempo_decorrido=0

        #Game over:
        if gameoverestado:
            gameover()
            janela.blit(texto,(620//2-texto.get_width()//2,845//2-texto.get_height()//2))
            if tempo_de_jogo%60<10:
                texto_tempo=fonte_tempo.render(str(f"{tempo_de_jogo//60}:0{tempo_de_jogo%60}"),True,(155,78,0))
                janela.blit(texto_tempo,(1050//2-texto_tempo.get_width()//2,845//2-texto_tempo.get_height()//2))
            else:
                janela.blit(texto_tempo,(1050//2-texto_tempo.get_width()//2,845//2-texto_tempo.get_height()//2))

            pontos=0
            tempo_decorrido = 0

        #Sair de gameover:
        if teclas[pygame.K_s] and gameoverestado:
            menu()
            jogoIniciado=False
            pos_xr,pos_yr=350,500
            gato1visivel=False
            gato2visivel=False
            gato3visivel=False
            gato4visivel=False
            gatogvisivel=False
            queijovisivel=False
            gameoverestado=False
            pos_yg1=-90
            pos_yg2=-90
            pos_yg3=-90
            pos_yg4=-90
            pos_ygg=-185

        # Movimentções do rato e colisões:
        rectrato.topleft=(pos_xr,pos_yr)
        rectqueijo.topleft=(pos_xq, pos_yq)
        rectgato1.topleft=(pos_xg1, pos_yg1)
        rectgato2.topleft=(pos_xg2, pos_yg2)
        rectgato3.topleft=(pos_xg3, pos_yg3)
        rectgato4.topleft=(pos_xg4, pos_yg4)
        rectgatogordo.topleft=(pos_xgg, pos_ygg)

        if teclas[pygame.K_UP] and pausaestado==False:
            if rectrato.colliderect(barreiraup):
                pos_yr-=0
            else:
                pos_yr-=5  


        if teclas[pygame.K_DOWN] and pausaestado==False:  
            if rectrato.colliderect(barreiradown):
                pos_yr-=0
            else:
                pos_yr+=5  


        if teclas[pygame.K_LEFT] and pausaestado==False:
            if rectrato.colliderect(barreiraleft):
                pos_xr-=0
            else:
                pos_xr-=5  


        if teclas[pygame.K_RIGHT] and pausaestado==False:
            if rectrato.colliderect(barreiraright):
                pos_xr-=0
            else:
                pos_xr+=5  


        if jogoIniciado:

            #Gera fundo
            janela.blit(fundo,(pos_x, pos_y))
            
            #Gera o rato:
            janela.blit(rato,(pos_xr,pos_yr))
            #pygame.draw.rect(janela, (222, 110, 0), rectrato, 2) #permite ver e acompanhar o rectangulo. Comentar para nao ver

            #Gera queijo:
            janela.blit(queijo,(pos_xq,pos_yq))

            #Trabalho queijo:
            if queijovisivel:
                pos_yq+=velocidadequeijo

            else:
                pos_xq=random.randint(0,710)
                pos_yq=-70
                queijovisivel=True 

            if rectqueijo.colliderect(rectrato):
                    pontos+=1
                    comer=pygame.mixer.Sound("comer.mp3")
                    comer.play()
                    queijovisivel=False

            if rectqueijo.colliderect(barreiradown):
                queijovisivel=False

            #Gera gato:
            janela.blit(gato1,(pos_xg1,pos_yg1))
            #janela.blit(gato2,(pos_xg2,pos_yg2)) # comentar para não ver no inicio
            #janela.blit(gato3,(pos_xg3,pos_yg3)) # comentar para não ver no inicio
            #janela.blit(gato4,(pos_xg4,pos_yg4)) # comentar para não ver no inicio
            #janela.blit(gatogordo,(pos_xgg,pos_ygg))
            #pygame.draw.rect(janela, (255, 255, 0), rectgato1, 2) # permite ver e acompanhar o rectangulo. Comentar para nao ver
            #pygame.draw.rect(janela, (255, 0, 0), rectgato2, 2) # permite ver e acompanhar o rectangulo. Comentar para nao ver
            #pygame.draw.rect(janela, (0, 255, 0), rectgato3, 2) # permite ver e acompanhar o rectangulo. Comentar para nao ver
            #pygame.draw.rect(janela, (0, 0, 255), rectgato4, 2) # permite ver e acompanhar o rectangulo. Comentar para nao ver
            #pygame.draw.rect(janela, (0, 255, 255), rectgatogordo, 2) # permite ver e acompanhar o rectangulo. Comentar para nao ver
            
            #pygame.draw.rect(janela, (255, 0, 255), rectqueijo, 2) # permite ver e acompanhar o rectangulo. Comentar para nao ver
            
            g2existe=False
            g3existe=False
            g4existe=False
            ggexiste=False

            if tempo_de_jogo>=10 and g2existe==False:
                janela.blit(gato2,(pos_xg2,pos_yg2))
                #pygame.draw.rect(janela, (255, 0, 0), rectgato2, 2) # permite ver e acompanhar o rectangulo. Comentar para nao ver
                g2existe=True

            if tempo_de_jogo>=25 and g3existe==False:
                janela.blit(gato3,(pos_xg3,pos_yg3))
                #pygame.draw.rect(janela, (0, 255, 0), rectgato3, 2) # permite ver e acompanhar o rectangulo. Comentar para nao ver
                g3existe=True

            if tempo_de_jogo>=40 and g4existe==False:
                janela.blit(gato4,(pos_xg4,pos_yg4))
                #pygame.draw.rect(janela, (0, 0, 255), rectgato4, 2) # permite ver e acompanhar o rectangulo. Comentar para nao ver
                g4existe=True

            if tempo_de_jogo>=60 and ggexiste==False:
                janela.blit(gatogordo,(pos_xgg,pos_ygg))
                #pygame.draw.rect(janela, (0, 255, 255), rectgatogordo, 2) # permite ver e acompanhar o rectangulo. Comentar para nao ver
                ggexiste=True

            #Trabalho gato 1:
            if gato1visivel:
                pos_yg1+=velocidadegato

            else:
                pos_yg1=-90
                pos_xg1=random.randint(0,710)
                gato1visivel=True

            if rectgato1.colliderect(rectrato):
                    morte=pygame.mixer.Sound("morte.mp3")
                    morte.play()
                    gameoverestado=True
                    jogoIniciado=False

            if rectgato1.colliderect(barreiradown):
                gato1visivel=False

            #Trabalho gato 2:
            if gato2visivel and g2existe==True:
                pos_yg2+=velocidadegato

            elif g2existe==True:
                pos_yg2=-90
                pos_xg2=random.randint(0,710)
                gato2visivel=True

            if rectgato2.colliderect(rectrato):
                    morte=pygame.mixer.Sound("morte.mp3")
                    morte.play()
                    gameoverestado=True
                    jogoIniciado=False

            if rectgato2.colliderect(barreiradown):
                gato2visivel=False

            #Trabalho gato 3:
            if gato3visivel and g3existe==True:
                pos_yg3+=velocidadegato

            elif g3existe==True:
                pos_yg3=-90
                pos_xg3=random.randint(0,710)
                gato3visivel=True

            if rectgato3.colliderect(rectrato):
                    morte=pygame.mixer.Sound("chicote.mp3")
                    morte.play()
                    gameoverestado=True
                    jogoIniciado=False

            if rectgato3.colliderect(barreiradown):
                gato3visivel=False

            #Trabalho gato 4:

            if gato4visivel and g4existe==True:
                pos_yg4+=velocidadegato

            elif g4existe==True:
                pos_yg4=-90
                pos_xg4=random.randint(0,710)
                gato4visivel=True

            if rectgato4.colliderect(rectrato):
                    morte=pygame.mixer.Sound("morte.mp3")
                    morte.play()
                    gameoverestado=True
                    jogoIniciado=False

            if rectgato4.colliderect(barreiradown):
                gato4visivel=False

            #Trabalho gato G:

            if gatogvisivel and ggexiste==True:
                pos_ygg+=velocidadegatog

            elif ggexiste==True:
                pos_ygg=-185
                pos_xgg=random.randint(0,610)
                gatogvisivel=True

            if rectgatogordo.colliderect(rectrato):
                    morte=pygame.mixer.Sound("morte.mp3")
                    morte.play()
                    gameoverestado=True
                    jogoIniciado=False

            if rectgatogordo.colliderect(barreiradown):
                gatogvisivel=False
        
            #Mostrador de Pontos:
            texto=fonte_pontos.render(str(pontos//2),True, (155,78,0))
            janela.blit(texto,(300//2-texto.get_width()//2,70//2-texto.get_height()//2))

            #Mostrador de Tempo:
            texto_tempo=fonte_tempo.render(str(f"{tempo_de_jogo//60}:{tempo_de_jogo%60}"),True,(155,78,0))
            if tempo_de_jogo%60<10:
                texto_tempo=fonte_tempo.render(str(f"{tempo_de_jogo//60}:0{tempo_de_jogo%60}"),True,(155,78,0))
                janela.blit(texto_tempo,(1480//2-texto_tempo.get_width()//2,70//2-texto_tempo.get_height()//2))
            else:
                janela.blit(texto_tempo,(1480//2-texto_tempo.get_width()//2,70//2-texto_tempo.get_height()//2))

        pygame.display.flip()

        asyncio.sleep(0)


asyncio.run(main())

#Sair do Pygame  
# pygame.quit()  