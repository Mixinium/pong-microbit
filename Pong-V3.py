import sys, pygame, random, serial, time
from easygui import *
import keyboard

bonnus = 0


# MENU
msg = "     Bienvenue dans le jeu pong avec le joueur 2 qui joue avec une microbit \n\n\n Commandes : \n\n Joueur 1 \n\n Z = Haut \n S = Bas\n\n Joueur 2 \n\n Flèche du haut = Haut \n Flèche du bas = Bas"
choix = ["Ok"]
buttonbox(msg, choices=choix)

# MENU
msg4 = "                        Veuillez choisir un mode de jeu !"
choix4 = ["Solo", "2 Joueurs", "Solo Microbit", "2 Joueurs Microbit"]
mode = buttonbox(msg4, choices=choix4)

# MENU
msg2 = "                        Veuillez choisir une difficulté"
choix2 = ["Facile", "Normal", "Dur", "Impossible"]
difficulty = buttonbox(msg2, choices=choix2)

if difficulty == "Facile":
    speed = 3
    vitesse = 6
    vitessenorme = 6
    tp = 0
elif difficulty == "Normal":
    speed = 6
    vitesse = 6
    vitessenorme = 6
    tp =0
elif difficulty == "Dur":
    speed = 9
    vitesse = 9
    vitessenorme = 9

    tp = 0
elif difficulty == "Impossible":
    speed = 13
    vitesse = 10
    vitessenorme = 10
    tp = 0

# MENU
msg3 = "                                  Bonus Activé ?"
choix3 = ["Oui", "Non"]
bonusa = buttonbox(msg3, choices=choix3)
if bonusa == "Oui":
    bonnus = 1

msg7 = "Score pour gagner ? (5 min, 100 max)"
scoremax = integerbox(msg7, lowerbound=5, upperbound=100)

reponse = ccbox("Voulez vous continuer ?", "Mon application")


if reponse == 1 and tp == 0:
    # Regarde le mode choisi 
    if mode == "2 Joueurs Microbit" or mode == "Solo Microbit":
        port = "COM5"
        baud = 115200
        s = serial.Serial(port)
        s.baudrate = baud
        s.timeout = 0
    
#============================================================================================================================================
    
    #variables bonus malus
    ttt = 0
    data = 0
    tp = 0
    raquette = 0
    vitesse1 = vitesse
    inverse =0
    raquette = 0
    bonus = 0
    malus = 0
    
#============================================================================================================================================

    
    # Lance l'écran
    pygame.init()
    width = 1000
    height = 600
    écran = pygame.display.set_mode((width, height))
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Pong")
    bg = pygame.image.load('bg.png')
    bgwin1 = pygame.image.load('bgwin1.png')
    bgwin2 = pygame.image.load('bgwin2.png')
    #scores
    def draw(canvas):
        myfont1 = pygame.font.SysFont("Comic Sans MS", 20)
        label1 = myfont1.render(str(score_1), 1, (255, 255, 226))
        canvas.blit(label1, (70, 20))

        myfont2 = pygame.font.SysFont("Comic Sans MS", 20)
        label2 = myfont2.render(str(score_2), 1, (255, 255, 226))
        canvas.blit(label2, (900, 20))

#============================================================================================================================================

    #Joueur 1
    joueur_1_img = pygame.image.load('player.png')
    joueur_1_X = 23
    joueur_1_Y_default = height/2 - 100
    joueur_1_Y_dif = 0
    joueur_1_malus = pygame.image.load('playermalus.png')
    joueur_1_bonus = pygame.image.load('playerbonus.png')


    #Joueur 2
    joueur_2_img = pygame.image.load('player.png')
    joueur_2_X = 950
    joueur_2_Y_default = height/2 - 100
    joueur_2_Y_dif = 0
    joueur_2_malus = pygame.image.load('playermalus.png')
    joueur_2_bonus = pygame.image.load('playerbonus.png')

#============================================================================================================================================

    #Mouvements
    def haut1(y_val):
        global joueur_1_Y_dif
        if joueur_1_Y_dif-y_val >= -joueur_1_Y_default+10:
            joueur_1_Y_dif -= y_val

    def bas1(y_val):
        global joueur_1_Y_dif
        if joueur_1_Y_dif+y_val <= joueur_1_Y_default-10:
            joueur_1_Y_dif += y_val

    def haut2(y_val):
        global joueur_2_Y_dif
        if joueur_2_Y_dif-y_val >= -joueur_2_Y_default+10:
            joueur_2_Y_dif -= y_val

    def bas2(y_val):
        global joueur_2_Y_dif
        if joueur_2_Y_dif+y_val <= joueur_2_Y_default-10:
            joueur_2_Y_dif += y_val

#============================================================================================================================================

    #Balle
    balle = pygame.image.load("ball.png")
    balle_X = width/2 - 15
    balle_Y = height/2 - 15
    balle_dir_X = -speed
    balle_dir_Y = speed
    game_on = True
    scores = 0
    score_1 = 0
    score_2 = 0
    J1 = "Joueur 1"
    J2 = "Joueur 2"
    def calc_ball():
        global balle_dir_X
        global balle_dir_Y
        global balle_X
        global balle_Y
        global scores
        global score_1
        global score_2
        global J1
        global J2
        global speed
        global inverse
        global bonus
        global malus
        global vitesse
        global vitesse1
        global raquette
        global joueur_1_X
        global joueur_2_X

#============================================================================================================================================

        #Collision bordure
        if balle_Y == 10:
            balle_dir_Y *= -1
            
        elif balle_Y == height-40:
            balle_dir_Y *= -1
            
#============================================================================================================================================
           
        # Bonus raquette rapprochée
        # 0 = non
        # 1 = gauche
        # 2 = droite
        
        if raquette == 0:
            if balle_X <= 45 and balle_Y >= joueur_1_Y_default+joueur_1_Y_dif-30 and balle_Y <= joueur_1_Y_default+joueur_1_Y_dif+200 and balle_dir_X < 0:
                balle_dir_X *= -1
            if balle_X >= 925 and balle_Y >= joueur_2_Y_default+joueur_2_Y_dif-30 and balle_Y <= joueur_2_Y_default+joueur_2_Y_dif+200 and balle_dir_X > 0:
                balle_dir_X *= -1
        if raquette == 1:
            if balle_X <= 45+90 and balle_Y >= joueur_1_Y_default+joueur_1_Y_dif-30 and balle_Y <= joueur_1_Y_default+joueur_1_Y_dif+200 and balle_dir_X < 0:
                balle_dir_X *= -1
            if balle_X >= 925 and balle_Y >= joueur_2_Y_default+joueur_2_Y_dif-30 and balle_Y <= joueur_2_Y_default+joueur_2_Y_dif+200 and balle_dir_X > 0:
                balle_dir_X *= -1
        if raquette == 2:
            if balle_X <= 45 and balle_Y >= joueur_1_Y_default+joueur_1_Y_dif-30 and balle_Y <= joueur_1_Y_default+joueur_1_Y_dif+200 and balle_dir_X < 0:
                balle_dir_X *= -1
            if balle_X >= 925-90 and balle_Y >= joueur_2_Y_default+joueur_2_Y_dif-30 and balle_Y <= joueur_2_Y_default+joueur_2_Y_dif+200 and balle_dir_X > 0:
                balle_dir_X *= -1
            
#============================================================================================================================================
        
        #Mouvements balle
        balle_X+=balle_dir_X
        balle_Y+=balle_dir_Y
 
#============================================================================================================================================
       
        # Regarde si les bonus sont activés + regarde si la balle marque un point
        if bonnus == 0:
            if (balle_X < 40):
                score_2 += 1
                scores = J1, score_1, J2, score_2
                pygame.display.set_caption(str(scores))
                balle_dir_X *= -1
                balle_X = width/2 - 15
                balle_Y = height/2 - 15
                
            elif (balle_X > 950):
                score_1 += 1
                scores = J1, score_1, J2, score_2
                pygame.display.set_caption(str(scores))
                balle_dir_X *= -1
                balle_X = width/2 - 15
                balle_Y = height/2 - 15

#============================================================================================================================================
        
        # Si oui alors activer les bonus + regarde si la balle marque un point
        if bonnus == 1:
            global ttt
            if (balle_X < 40):
                score_2 += 1
                scores = J1, score_1, J2, score_2
                pygame.display.set_caption(str(scores))
                draw(écran)
                balle_dir_X *= -1
                balle_X = width/2 - 15
                balle_Y = height/2 - 15
                # Tire au sort un malus/bonus
                ttt = random.randint(1,7)
                bonus = 0
                malus = 0
                if ttt==1:
                    inverse = 2
                    malus = 1
                else:
                    inverse = 0
                if ttt==2:
                    vitesse = vitessenorme-3
                    vitesse1 = vitessenorme
                    malus = 1
                
                if ttt == 3:
                    vitesse1 = vitessenorme+5
                    vitesse = vitessenorme
                    bonus = 2
                
                if ttt == 4:
                    raquette = 1
                    joueur_1_X = 23+90
                    joueur_2_X = 950
                    bonus = 2
                else:
                    raquette = 0
                    joueur_1_X = 23
                    joueur_2_X = 950
            
            elif (balle_X > 950):
                score_1 += 1
                scores = J1, score_1, J2, score_2
                pygame.display.set_caption(str(scores))
                draw(écran)
                balle_dir_X *= -1
                balle_X = width/2 - 15
                balle_Y = height/2 - 15
                tt = random.randint(1,7)
                malus = 0
                bonus = 0
                if tt==1:
                    inverse = 1
                    malus = 2
                else:
                    inverse = 0
                if tt==2:
                    vitesse1 = vitessenorme -3
                    vitesse = vitessenorme
                    malus = 2
                else:
                    vitesse1 = vitessenorme
                if tt == 3:
                    vitesse = vitessenorme+5
                    vitesse1 = vitessenorme
                    bonus = 1

                if tt == 4:
                    raquette = 2
                    joueur_2_X = 950-90
                    joueur_1_X = 23
                    bonus = 1
                else:
                    raquette = 0
                    joueur_2_X = 950
                    joueur_1_X = 23
                    
#============================================================================================================================================

        #Bordures
        balle_Y = min(balle_Y, height-40)
        balle_Y = max(balle_Y, 10)


    
    # IA Impossible
    
    def IA():
        global joueur_2_Y_dif
        if joueur_2_Y_dif <= balle_Y-240:
            if joueur_2_Y_dif+6 <= joueur_2_Y_default-10:
                joueur_2_Y_dif += 6
        if joueur_2_Y_dif >= balle_Y-220 :
            if joueur_2_Y_dif-6 <= joueur_2_Y_default+10:
                joueur_2_Y_dif -= 6
    
#============================================================================================================================================

    #Créé et place les images 
    def ball():
        écran.blit(balle, (balle_X, balle_Y))
    def joueur1(y_val):
        écran.blit(joueur_1_img, (joueur_1_X, y_val))
    def joueur1malus(y_val):
         écran.blit(joueur_1_malus, (joueur_1_X, y_val))
    def joueur1bonus(y_val):
         écran.blit(joueur_1_bonus, (joueur_1_X, y_val))
    def joueur2(y_val):
        écran.blit(joueur_2_img, (joueur_2_X, y_val))
    def joueur2malus(y_val):
        écran.blit(joueur_2_malus, (joueur_2_X, y_val))
    def joueur2bonus(y_val):
        écran.blit(joueur_2_bonus, (joueur_2_X, y_val))
    def scorebg():
        écran.blit(bg, (0, 0))
        draw(écran)
    def win1():
        écran.blit(bgwin1,(0,0))
    def win2():
        écran.blit(bgwin2,(0,0))
    scorebg()
    joueur1(joueur_1_Y_default+joueur_1_Y_dif)
    joueur2(joueur_2_Y_default+joueur_2_Y_dif)
    ball()
    calc_ball()

#============================================================================================================================================
    
    # Boucle "infini", début du jeu
    while game_on:
        if mode == "Solo Microbit" or mode == "2 Joueurs Microbit":
            data = s.read()
        
        draw(écran)
        
        #Regarde si une touche est appuyée
        key_input = pygame.key.get_pressed()

        for event in pygame.event.get():
            #Pour quitter
            if event.type==pygame.QUIT:
                game_on=False
            if key_input[pygame.K_l]:
             game_on=False

#============================================================================================================================================
        
        #Commandes microbit avec serial 
        if mode == "2 Joueurs Microbit":
            if data==b'1':
                haut1(150)
            if data==b'2':
                bas1(150)
            if data==b'3':
                haut2(150)
            if data==b'4':
                bas2(150)
        if mode == "Solo Microbit":
            if data==b'1':
                haut1(150)
            if data==b'2':
                bas1(150)
                
            IA()

#============================================================================================================================================

        if mode == "Solo":
            if inverse == 0:
                #Déplacements
                if key_input[pygame.K_z]:
                    haut1(vitesse)
                if key_input[pygame.K_s]:
                    bas1(vitesse)
            if inverse == 1:
                if key_input[pygame.K_z]:
                    bas1(vitesse)
                if key_input[pygame.K_s]:
                    haut1(vitesse)
            
            IA()
        if mode == "2 Joueurs":
            #regarde si le malus touche inverse est activé si oui inverse les touches + commands normales
            if inverse == 0 or inverse == 2:
                if key_input[pygame.K_z]:
                    haut1(vitesse)
                if key_input[pygame.K_s]:
                    bas1(vitesse)
            if inverse == 1:
                if key_input[pygame.K_z]:
                    bas1(vitesse)
                if key_input[pygame.K_s]:
                    haut1(vitesse)
            if inverse == 0 or inverse == 1:
                if key_input[pygame.K_UP]:
                    haut2(vitesse1)
                if key_input[pygame.K_DOWN]:
                    bas2(vitesse1)
            if inverse == 2:
                if key_input[pygame.K_UP]:
                    bas2(vitesse1)
                if key_input[pygame.K_DOWN]:
                    haut2(vitesse1)
        # affiche le score
        scorebg()

#============================================================================================================================================

        #Change la couleur de la raquette en fonction de si il y a un bonus ou un malus
        if bonus == 0 and malus == 0:
            joueur1(joueur_1_Y_default+joueur_1_Y_dif)
            joueur2(joueur_2_Y_default+joueur_2_Y_dif)
        if bonus == 2:
            joueur1bonus(joueur_1_Y_default+joueur_1_Y_dif)
            joueur2(joueur_2_Y_default+joueur_2_Y_dif)
        if bonus == 1:
            joueur1(joueur_1_Y_default+joueur_1_Y_dif)
            joueur2bonus(joueur_2_Y_default+joueur_2_Y_dif)
        if malus == 2:
            joueur1malus(joueur_1_Y_default+joueur_1_Y_dif)
            joueur2(joueur_2_Y_default+joueur_2_Y_dif)
        if malus == 1:
            joueur1(joueur_1_Y_default+joueur_1_Y_dif)
            joueur2malus(joueur_2_Y_default+joueur_2_Y_dif)
        
        ball()
        calc_ball()

#============================================================================================================================================
        
        # Score Max + Affiche écran de fin
        if score_1 >= scoremax :
            win1()
            pygame.display.update()
            time.sleep(5)
            game_on = False
        if score_2 >= scoremax :
            win2()
            pygame.display.update()
            time.sleep(5)
            game_on = False
        # Rafraichis l'écran
        pygame.display.update()
        