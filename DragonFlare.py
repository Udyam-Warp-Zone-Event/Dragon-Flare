__author__ = 'MemBRAIN'
#importing
import pygame
from pygame import *



#importing libraries
import os
import pygame
import sys
import time
import math
import random
from datetime import datetime
from pygame.locals import *


#initializing pygame
pygame.init()
filename = "Dragon/"
back = pygame.image.load(filename + "02c560ade4fb9441245af5d083a1f357.png")

"""
Creating our game screen by passing its screen size as the parameter,
and setting its caption as 'DragonFlare'
"""

pygame.display.set_caption('DRAGON FLARE')
filename = "Dragon/"
icon = pygame.image.load(filename + "iconSmall2.png")
pygame.display.set_icon(icon)

def displaytext(text,fontsize,x,y,color):
        font = pygame.font.SysFont('sawasdee', fontsize, True)
        text = font.render(text, 1, color)
        textpos = text.get_rect( centerx = x, centery = y)
        SCREEN.blit(text, textpos)

black = (0,0,0)
white = (255,255,255)
red = (120,100,150)
grey = (80,80,80)
darkgrey = (80,20,150)
darkred = (210, 10, 20)
scr_size = (width,height) = (1100,700)
SCREEN = pygame.display.set_mode(scr_size)

def Game():
    global SCREEN
    highscore = int((open(filename+"highscore.txt","r+")).read())


    t1=datetime.now()
    t2=datetime.now()
    t3=datetime.now()

    tpic1 = datetime.now()
    tpic2 = datetime.now()


    temp=1



    #setting the FPS or number of Frames per Second
    FPS = 60

    #Setting the screen size
    scr_size = (width,height) = (1100,700)


    #creating a clock object from pygame.time.Clock class
    clock = pygame.time.Clock()


    #Declaring various color values
    black = (0,0,0)
    white = (255,255,255)
    red = (50,100,150)
    grey = (80,80,80)
    darkgrey = (80,20,150)
    darkred = (210, 10, 20)

    """
    A function used to display text on the screen
    It takes in 4 parameters, i.e
    text : the text which is to be printed. Has to be a string
    fontsize : the fontsize of the text to be printed. Must be an integer
    x,y : The x and y coordinates where we want our text to be printed
    color : The color of the text. Its has to be in (R,G,B) format where R, G and B takes values from 0 to 255
    """
    def displaytext(text,fontsize,x,y,color):
        font = pygame.font.SysFont('sawasdee', fontsize, True)
        text = font.render(text, 1, color)
        textpos = text.get_rect( centerx = x, centery = y)
        SCREEN.blit(text, textpos)

    displaytext('DRAGONFLARE',10,0,100,black)

    """

    Class defining Dragon's attributes

    """
    score=0

    dragonImage = []
    for i in range(20):
        dragonImage.append(pygame.image.load(filename + "dragon1 screens/png/"+str(i)+".png"))
    i = 0

    shoot = []
    for i in range(3):
        shoot.append(pygame.image.load(filename + "fireball/"+str(i)+".png"))

    Obstacle = pygame.image.load(filename + "Bubble.png")
    bubble1 = pygame.image.load(filename + "bubble2.png")
    upwall = pygame.image.load(filename + "up.png")
    downwall = pygame.image.load(filename + "down.png")
    background = pygame.image.load(filename + "IceWall.jpg")
    Flame = pygame.image.load(filename + "flame.png")
    Villain = pygame.image.load(filename + "/dragon2 screens/0.png")



    Heart = pygame.image.load(filename + "Heart.png")
    speed = 5
    explosion = pygame.mixer.Sound(filename + "explosion.wav")
    pygame.mixer.music.load(filename + "bg_music.ogg")
    pygame.mixer.music.play(-1)

    def collision():

        dragonx1 = Flare.x+100
        dragony1 = Flare.y+120
        dragony2 = Flare.y+170
        dragonx2 = Flare.x+250

        flag = 0

        for Bub in BubbleList:
            bubblex1 = Bub.x
            bubblex2 = Bub.x+Bub.sizex
            bubbley1 = Bub.y
            bubbley2 = Bub.y+Bub.sizey

            if (dragonx1 > bubblex2 or dragonx2 < bubblex1):

                continue


            elif dragony1 > bubbley2 or dragony2 < bubbley1:

                continue

            else:
                flag = 1
                break

        if flag == 0:
            return 0

        else:
            return 1

    def attackhit(vil):

        dragonx1 = vil.x
        dragony1 = vil.y
        dragony2 = vil.y+60
        dragonx2 = vil.x+70

        x1 = FireBall.x-10
        x2 = FireBall.x+40
        y1 = FireBall.y-10
        y2 = FireBall.y+40
        flag = 0


        if (dragonx1 > x2 or dragonx2 < x1):

            flag=0


        elif dragony1 > y2 or dragony2 < y1:

            flag=0

        else:
                flag = 1



        return flag


    def Powerup(obj):
        dragonx1 = Flare.x+100
        dragony1 = Flare.y+120
        dragony2 = Flare.y+170
        dragonx2 = Flare.x+250

        Ex1 = obj.x
        Ex2 = obj.x +obj.width
        Ey1 = obj.y
        Ey2 = obj.y+obj.height

        if dragonx1 > Ex2 or dragonx2 < Ex1 :
            return 0


        if dragony1 > Ey2 or dragony2 < Ey1 :
            return 0

        return 1

    def Blast():
        x1 = FireBall.x-10
        x2 = FireBall.x+40
        y1 = FireBall.y-10
        y2 = FireBall.y+40


        dest=-1
        for i in range(len(BubbleList)):
            bubblex1 = BubbleList[i].x
            bubblex2 = BubbleList[i].x+BubbleList[i].sizex
            bubbley1 = BubbleList[i].y
            bubbley2 = BubbleList[i].y+BubbleList[i].sizey

            if (x1 > bubblex2 or x2 < bubblex1):

                continue


            elif y1 > bubbley2 or y2 < bubbley1:

                continue

            elif BubbleList[i].ultimate == 0:
                dest=i
            else:
                FireBall.x=scr_size[0]+10


        if dest != -1 :
            pygame.mixer.music.stop()
            explosion.play(1)
            pygame.mixer.music.play()
            BubbleList.remove(BubbleList[dest])












    class Dragon():

        def __init__(self,sizex,sizey,x,y,speedUp,speedDown,health):

            self.x = x
            self.y = y
            self.speedUp = speedUp
            self.sizex = sizex
            self.sizey = sizey
            self.speedDown = speedDown
            self.health=health



        def Up(self,flame):
            self.y = self.y-self.speedUp
            if flame!=2:
                self.Health()

        def Down(self):
            self.y = self.y+self.speedDown

        def Draw(self, j):
            #if(j%2)==0:
            if self.health < 25:
                color = darkred
            else:
                color = darkgrey
            pygame.draw.rect(SCREEN,color,[20, 7 ,int(self.health*10),10])

            SCREEN.blit(dragonImage[j%20],[self.x, self.y])



        def Loser(self):
            if self.health <= 0 or self.y+70<Wall.upwall or self.y+Flare.sizey-70 > scr_size[1]-Wall.downwall:
                return 0

        def Health(self):
            self.health = self.health-0.2

    Flare = Dragon(273,300,100,200,5,3,100)
    gameOver = 0
    h = 0
    k=0


    class squartle():

        def __init__(self,x,y,speedy):
            self.x=x
            self.y=y
            self.speedy=speedy
            self.y1=self.y
            self.health = 100
            self.tr = 1/2



        def rand (self):
            self.y1=random.randrange(scr_size[1]-330)+150

        def move(self):

            if self.y1>self.y:
                self.y+=self.speedy

            else:
                self.y-=self.speedy
            if score>4000:
                SCREEN.blit(Villain,[self.x-60,self.y])
            else:
                SCREEN.blit(Villain,[self.x-40,self.y])
            color = red

            pygame.draw.rect(SCREEN,color,[10, scr_size[1]-27 ,int(self.health*10),10])


        def shoot(self,scor):


            for j in range(len(BubbleList)):
                BubbleList[j].move(0)
            if scor>4000:
                self.tr = 3/4

            if len(BubbleList)==0 or BubbleList[len(BubbleList)-1].x < scr_size[0]*self.tr :

                    if scor == 1000:

                        b1 = Bubble(-1,0,speed,0,10,10,1)
                    elif scor >1000 and scor<4000:
                        b1 = Bubble(-1,0,speed,speed,10,10,0)

                    else :
                        ak=random.randrange(2)
                        if ak == 0:

                            b1 = Bubble(-1,0,speed,0,10,10,1)


                        else:
                            b1 = Bubble(-1,0,speed,speed,10,10,0)

                    b1.x=self.x
                    b1.y=self.y
                    b1.y0=b1.y
                    BubbleList.append(b1)

        def health(self):
            self.health = self.health-5



    s1 = squartle(scr_size[0]-50,500,3)







    class Walls():

        def __init__(self,upwall,downwall):
            self.upwall = upwall
            self.downwall = downwall



        def Draw(self):
            #pygame.draw.rect(SCREEN,white,[0,0,scr_size[0],self.upwall])
            SCREEN.blit(upwall,[0,0])
            SCREEN.blit(downwall,[0,scr_size[1]-120])

    Wall=Walls(50,50)


    class Bubble():
        def __init__(self, x ,y, speedx ,speedy, sizex , sizey, ultimate):
            self.speedx=speedx
            self.speedy=speedy
            self.x = x
            self.y = y
            self.y0=self.y
            self.sizex = sizex
            self.sizey = sizey
            self.ultimate=ultimate

        def re(self,x,y,speedx,speedy,sizex,sizey):
            self.speedx=speedx
            self.speedy=speedy
            self.x = x
            self.y = y
            self.sizex = sizex
            self.sizey = sizey



        def drawBubble (self):
            if self.ultimate == 1:
                SCREEN.blit(bubble1,[self.x, self.y])
            else:
                SCREEN.blit(Obstacle,[self.x, self.y])


        def randLoc (self):
            self.x = scr_size[0]
            self.y = random.randrange(0, scr_size[1]-330) +150
            self.y0=self.y


        def move(self,check):
            self.x -= self.speedx
            if self.y<150 or self.y>scr_size[1]-180 or self.y<self.y0-70 or self.y>self.y0+70:
                self.speedy = -self.speedy



            self.y += self.speedy

            if(check==0):
                self.drawBubble()
            else:
                pygame.draw.rect(SCREEN,white,[self.x,self.y,3,3])




    B1=Bubble(-1,0,speed,0,10,10,0)
    stars = Bubble(-1,0,2,0,10,10,0)
    starsList = []
    for i in  range(20):
        b1 = Bubble(-1,0,2,0,10,10,0)
        b1.randLoc()
        b1.x=random.randrange(scr_size[0])
        starsList.append(b1)

    starsList.append(stars)
    B1.randLoc()
    BubbleList=[]
    BubbleList.append(B1)
    c=0
    class Elixir():

        def __init__(self,width,height,spd,x,y):
            self.width=width
            self.height=height
            self.spd=spd
            self.x=x
            self.y=y



        def draw(self):
            SCREEN.blit(Heart,[self.x, self.y])

        def randE(self):
            self.y=random.randrange(scr_size[1]/2)+scr_size[1]/4
            self.x=scr_size[0]

        def move(self,t1,t2,time,spd,y=0):
            self.spd=spd
            if self.x >= 0:
                self.x -= self.spd
                if y==0:
                    self.draw()
                else:
                    SCREEN.blit(Flame,[self.x,self.y])

            elif self.x < 0:
                if (((t2.second - t1.second) + 60) % 60) > time:

                    self.randE()
                    return t2

            return t1

    El = Elixir(10,10,speed,-1,-1)
    Power = Elixir(10,10,speed,-1,-1)



    class Fireball():

        def __init__(self,x,y,speed):
            self.x = x
            self.y = y
            self.speed=speed

        def init(self,x,y):
            self.x = x
            self.y = y

        def draw(self,im):
            self.x+=self.speed
            SCREEN.blit(shoot[im%3],[self.x, self.y])

    FireBall = Fireball(1000,0,7)
    fire=0
    turn=18
    flame=0

    abc = 1
    while gameOver == 0:


        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    h = 1

                if event.key ==pygame.K_RIGHT:
                    fire=1

                if event.key == pygame.K_ESCAPE:
                    displaytext("GAME PAUSED",50,scr_size[0]/2,200,darkgrey)
                    pygame.display.update()

                    while(1):


                        k = 0

                        for event in pygame.event.get() :
                            if(event.type == pygame.KEYDOWN):
                                if event.key == pygame.K_ESCAPE:
                                    k=1

                        if k==1:
                            break


            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        h = 0

            if event.type == pygame.QUIT:
                gameOver=1


        if fire == 1 and FireBall.x >=scr_size[0] and flame != 0:

            FireBall.init(Flare.x+260,Flare.y+125)
            pygame.mixer.music.stop()
            explosion.play(1)
            pygame.mixer.music.play()

        fire=0


        if score!=1000 and score != 3000 and score != 5000:
            score=score+1

            if(highscore <score):
                highscore = score
                (open(filename+"highscore.txt","w+")).write(str(highscore))


        if h == 1:
            Flare.Up(flame)
        elif h == 0:
            Flare.Down()
            k=2



        #SCREEN.blit(background,[0,0] )
        SCREEN.fill(black)
        for j in range(len(starsList)):
            starsList[j].move(1)

        if starsList[len(starsList)-1].x < scr_size[0]*7/8:
                b1 = Bubble(-1,0,2,0,10,10,0)
                b1.randLoc()
                starsList.append(b1)

        displaytext("" + str(score),150 ,scr_size[0]/2,scr_size[1]/2,grey)


        displaytext("Highscore : " + str(highscore),50 ,scr_size[0]/2,scr_size[1]/2-70,grey)

        if Flare.Loser() == 0 or collision() == 1:
            pygame.mixer.music.stop()
            explosion.play(1)
            pygame.mixer.music.play()


            print("You Lose")
            gameOver=1

        if Powerup(El) == 1:
            Flare.health=100
            El.x = -1

        if Powerup(Power) == 1:
            if flame == 0:
                flame=1
            Power.x=-1


        if(FireBall.x<scr_size[0]):
            FireBall.draw(k)

        if FireBall.x>scr_size[0]:
            FireBall.x=2000

        Blast()


        k = k+1




        Wall.Draw()

        #pygame.draw.rect(SCREEN,white,[Flare.x+100,Flare.y+50,Flare.sizex/2-30,Flare.sizey-100])
        #pygame.draw.rect(SCREEN,white,[Flare.x+100,Flare.y+120,150,50])
        Flare.Draw(k)

        if score !=1000 and score != 3000 and score != 5000:
            for j in range(len(BubbleList)):
                BubbleList[j].move(0)

            if BubbleList[len(BubbleList)-1].x < scr_size[0]*3/4:
                    if score>1000 and score < 3000:
                        b1 = Bubble(-1,0,speed,0,10,10,1)
                    elif score <1000:
                        b1 = Bubble(-1,0,speed,0,10,10,0)

                    else :
                        b1 = Bubble(-1,0,speed,speed,10,10,0)

                    b1.randLoc()
                    BubbleList.append(b1)


        else:
            flame = 2
            if abc == 1:
                BubbleList.clear()
                #del BubbleList[:]
                #BubbleList = []
                s1.health = 100
                abc=0
            if abs(s1.y1-s1.y)<3:
                s1.rand()
            s1.move()
            s1.shoot(score)

            if attackhit(s1) == 1:
                pygame.mixer.music.stop()
                explosion.play(1)
                pygame.mixer.music.play()
                if score <4000:
                    s1.health=s1.health-3

                else :
                    s1.health=s1.health -0.5

            if s1.health < 0:
                score = score+500
                flame = 1
                abc = 1


        time = 10
        t2=datetime.now()
        if flame==1 and (t2.second-t1.second+60)%60>10:
            flame = 0

        t1=El.move(t1,t2, time, speed)

        temp=t3
        t3=Power.move(t3,t2,turn, speed, 1)
        if(temp!=t3 and turn<=60):
            turn=turn*1.5









        if speed < 10:
            speed+=0.002

        pygame.display.update()


        clock.tick(FPS)

    SCREEN.fill(black)
    SCREEN.blit(back,[30,30])
    displaytext("GAME OVER",50,scr_size[0]/2,200,red)
    displaytext("YOUR SCORE = "+str(score),50,scr_size[0]/2,300,red)
    displaytext("PRESS ESC TO CONTINUE",50,scr_size[0]/2,400,red)
    pygame.display.update()

    while(1):
        k=0

        for event in pygame.event.get() :
            if(event.type == pygame.KEYDOWN):
                if event.key == pygame.K_ESCAPE:
                    k=1

        if k==1:
            break









menu = 0
def Menu():
    global menu
    SCREEN.fill(black)

    SCREEN.blit(back,[30,30])
    pygame.draw.rect(SCREEN,white,[scr_size[0]/2-80,280+menu*100,160,50])
    displaytext("DRAGON FLARE",80,scr_size[0]/2,100,red)
    displaytext("START",50,scr_size[0]/2,300,red)
    displaytext("HELP",50,scr_size[0]/2,400,red)
    displaytext("EXIT",50,scr_size[0]/2,500,red)
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                menu += 1

            if event.key == pygame.K_UP:
                menu -= 1
                if menu < 0:
                    menu = 2

            if event.key == K_RETURN:
                if menu == 0:

                    Game()



                if menu == 1:
                    SCREEN.fill(black)
                    SCREEN.blit(back,[30,30])
                    displaytext("HELP",40,scr_size[0]/2,40,red)
                    displaytext("USE SPACE BAR TO FLY YOUR DRAGON",30,scr_size[0]/2,100,red)
                    displaytext("FLYING YOUR DRAGON REDUCES DRAGON'S STAMINA",30,scr_size[0]/2,150,red)
                    displaytext("TOUCHING THE BUBBLE KILLS YOUR DRAGON",30,scr_size[0]/2,200,red)
                    displaytext("IF THE STAMINA REDUCES TO ZERO YOUR DRAGON DIES",30,scr_size[0]/2,250,red)
                    displaytext("POWERUPS WILL INCREASE THE DRAGON'S STAMINA OR GIVE IT FIRE SHOOTING ABILITY",30,scr_size[0]/2,300,red)
                    displaytext("TO SHOOT PRESS RIGHT ARROW KEY",30,scr_size[0]/2,350,red)

                    displaytext("PRESS ESC TO GO BACK",40,scr_size[0]/2,400,red)
                    while(1):
                        k=0

                        for event in pygame.event.get() :
                            if(event.type == pygame.KEYDOWN):
                                if event.key == pygame.K_ESCAPE:
                                    k=1

                        if k==1:
                            break


                        pygame.display.update()



                if menu == 2:
                    pygame.quit()
                    exit()







    menu = menu%3









while(1):
    Menu()





quit()
