import pygame
import random
import time
pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
#greens(0,155,0)
blue=(0,0,255)
gray=(118,119,110)
car_img=pygame.image.load("car-clipart-sprite-sheet-14.jpg")
car_img=pygame.transform.scale(car_img,(100,100))
background_img=pygame.image.load("background1.jpg")
grass_img=pygame.image.load("download12.jpg")



def message(size,mess,x_pos,y_pos):
    font=pygame.font.SysFont(None,size)

    render=font.render(mess,True,black)
    screen.blit(render,(x_pos,y_pos))

message(100, "START", 100, 100)
clock.tick(1)
def enemy_car(x_r,y_r):
    screen.blit(car_img,(x_r,y_r))

def car(x,y):
    screen.blit(car_img, (x, y))
    screen.blit(grass_img, (0, 0))
    screen.blit(grass_img, (700,0))
    if 0<x<100 or 700<x<800:
        message(100,"GAME OVER",200,200)
        pygame.display.update()
        clock.tick(0.5)
        game_intro()

def button(x_button,y_button,mess_b):
    pygame.draw.rect(screen,green,[x_button,y_button,100,30])
    message(50,mess_b,x_button,y_button)
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    print(mouse)
    print(click)
    if x_button<mouse[0]<x_button+100 and y_button<mouse[1]<y_button+30:
        pygame.draw.rect(screen,blue, [x_button, y_button, 100, 30])
        message(50, mess_b, x_button, y_button)
        if click==(1,0,0) and mess_b=="START":
            game_loop()
        elif click==(1,0,0) and mess_b=="QUIT":
            pygame.quit()
            quit()

def car_crash(x,x_r,y,y_r):
    if x_r<x<x_r+90 and y_r<y<y_r+90 or x_r<x+90<x_r+90 and y_r<y+90<y_r+90:
        message(50,"CRASHED VIKAS",200,200,)
        pygame.display.update()
        time.sleep(1)
        game_intro()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
def score(count):
    font=pygame.font.SysFont(None,30)
    screen_text=font.render('score:'+str(count),True,white)
    screen.blit(screen_text,(0,0))


def game_intro():
    intro=False
    while intro == False:
        screen.blit(background_img, (0, 0))
        button(100,300,"START")
        button(600,300,"QUIT")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro == True
        pygame.display.update()


def game_loop():
        x=300
        count=0
        x_r=random.randrange(100,600)
        y_r=0
        y=490
        x_change=0
        y_change=0
################making display_screen######################################



        game_over=False
        while game_over==False:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_over==True
######################## END OF MAKING DISPLY IN PYGAME#####################

     ##### FOR MOVING OBJECT  #######
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        x_change=+10
                    elif event.key==pygame.K_RIGHT:
                        x_change=-10
                    elif event.key==pygame.K_UP:
                        y_change=+10
                    elif event.key==pygame.K_DOWN:
                        y_change=-10
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                        x_change=0
                    if event.key==pygame.K_DOWN or event.key==pygame.K_UP:
                        y_change=0

        ######     END   ####################33
            screen.fill(gray)
            car(x,y)
            score(count)
            enemy_car(x_r,y_r)
            y_r+=10
            if y_r==600:
                x_r = random.randrange(100, 600)
                y_r=0
                count+=1
            car_crash(x,x_r,y,y_r)

            #message(100, "START", 100, 100)
            #clock.tick(1)
            x=x-x_change
            y=y-y_change
            clock.tick(58)
            pygame.display.update()



game_intro()
pygame.display.update()
pygame.quit()
quit()



