import sys, pygame, random
from easygui import *
import keyboard
#bonus/malus
raquette = 0
inverse =0
vitesse = 6
vitesse1 = 6

bonus = 0
malus = 0


speed = 6
for i in range(1):
    pygame.init()
    width = 1000
    height = 600
    écran = pygame.display.set_mode((width, height))
    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Pong")
    bg = pygame.image.load('bg.png')

    #scores
    def draw(canvas):
        myfont1 = pygame.font.SysFont("Comic Sans MS", 20)
        label1 = myfont1.render(str(score_1), 1, (255, 255, 226))
        canvas.blit(label1, (70, 20))

        myfont2 = pygame.font.SysFont("Comic Sans MS", 20)
        label2 = myfont2.render(str(score_2), 1, (255, 255, 226))
        canvas.blit(label2, (900, 20))


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


        if balle_Y == 10:
            balle_dir_Y *= -1
            
        elif balle_Y == height-10-30:
            balle_dir_Y *= -1
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
            
        
        
        balle_X+=balle_dir_X
        balle_Y+=balle_dir_Y
        if (balle_X < 40):
            score_2 += 1
            scores = J1, score_1, J2, score_2
            pygame.display.set_caption(str(scores))
            draw(écran)
            balle_dir_X *= -1
            balle_X = width/2 - 15
            balle_Y = height/2 - 15
            ttt = random.randint(4,4)
            bonus = 0
            malus = 0
            if ttt==1:
                inverse = 2
                malus = 1
            else:
                inverse = 0
            if ttt==2:
                vitesse = 2
                vitesse1 = 6
                malus = 1
            else:
                vitesse = 6
            if ttt == 3:
                vitesse1 = 10
                vitesse = 6
                bonus = 2
            else:
                vitesse1 = 6
                vitesse = 6
            if ttt == 4:
                raquette = 1
                joueur_1_X = 23+90
                joueur_2_X = 950
            else:
                raquette = 0
                joueur_1_X = 23
                joueur_2_X = 950
            print(ttt)
            
        elif (balle_X > 950):
            score_1 += 1
            scores = J1, score_1, J2, score_2
            pygame.display.set_caption(str(scores))
            draw(écran)
            balle_dir_X *= -1
            balle_X = width/2 - 15
            balle_Y = height/2 - 15
            tt = random.randint(4,4)
            malus = 0
            bonus = 0
            joueur_1_X = 23
            if tt==1:
                inverse = 1
                malus = 2
            else:
                inverse = 0
            if tt==2:
                vitesse1 = 3
                vitesse = 6
                malus = 2
            else:
                vitesse1 = 6
            if tt == 3:
                vitesse = 9
                vitesse1 = 6
                bonus = 1

            else:
                vitesse1 = 6
                vitesse = 6
            if tt == 4:
                raquette = 2
                joueur_2_X = 950-90
                joueur_1_X = 23
            else:
                raquette = 0
                joueur_2_X = 950
                joueur_1_X = 23
            print(tt)
            
            
            
        balle_Y = min(balle_Y, height-10-30)
        balle_Y = max(balle_Y, 10)


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
    scorebg()
    joueur1(joueur_1_Y_default+joueur_1_Y_dif)
    joueur2(joueur_2_Y_default+joueur_2_Y_dif)
    ball()
    calc_ball()
    while game_on:
        draw(écran)
        key_input = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_on=False
            if key_input[pygame.K_l]:
             game_on=False

        if inverse == 0:
            if keyboard.is_pressed('z'):
                haut1(vitesse1)
            if keyboard.is_pressed('s'):
                bas1(vitesse1)
            if keyboard.is_pressed('up'):
                haut2(vitesse)
            if keyboard.is_pressed('down'):
                bas2(vitesse)

        if inverse == 1:
            if keyboard.is_pressed('z'):
                bas1(vitesse1)
            if keyboard.is_pressed('s'):
                haut1(vitesse1)
            if keyboard.is_pressed('up'):
                haut2(vitesse)
            if keyboard.is_pressed('down'):
                bas2(vitesse)
        if inverse == 2:
            if keyboard.is_pressed('up'):
                bas2(vitesse)
            if keyboard.is_pressed('down'):
                haut2(vitesse)
            if keyboard.is_pressed('z'):
                haut1(vitesse1)
            if keyboard.is_pressed('s'):
                bas1(vitesse1)
        

        
        scorebg()
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
        pygame.display.update()