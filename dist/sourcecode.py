import pygame
import random
pygame.init()

pygame.mixer.init()


def game():
    exit_game=False

    white=(255,255,255)
    black=(0,0,0)
    red=(255,0,0)
    snk_length=1
    score=0
    gamewindow=pygame.display.set_mode((900,700))
    pygame.display.set_caption("my first game")
    pygame.display.update()

    quits=False
    clock=pygame.time.Clock()
    x=5
    y=55
    i=0
    foodx=random.randrange(200,700)
    foody=random.randrange(200,500)

    velx=0
    vely=0
    print(pygame.font.get_fonts())
    snk_list=[]

    with open("highscore.txt","r") as s:
        high = s.read()

    font = pygame.font.Font(None, 40)
    def score1(score, color, x, y):
        game_font = font.render(score, True, color)
        gamewindow.blit(game_font, [x, y])
    while not quits:
        gamewindow.fill(white)
        score1("snake game  ",black,300,200)
        score1(" made with snake language ", black, 200, 300)
        score1(" press enter to continue ", black, 250, 400)
        pygame.display.update()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quits=True
                pygame.quit()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load("back.mp3")
                    pygame.mixer.music.play(-1)
                    quits=True
    quits=False
    while not quits:









        gamewindow.fill(white)
        def snake_plot(snk_list):
            for x,y in snk_list:
                pygame.draw.rect(gamewindow,black,[x, y, 15, 15])







        for event in pygame.event.get():


            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if( (event.key==pygame.K_RIGHT) and velx==0):
                    velx=10+i
                    vely=0

                if( (event.key==pygame.K_LEFT)and velx==0):
                    velx = -10-i
                    vely = 0
                if ((event.key==pygame.K_UP)and vely==0):
                    velx = 0
                    vely = -10-i
                if ((event.key==pygame.K_DOWN) and vely==0):
                    velx = 0
                    vely = 10+i


        x=x+velx
        y=y+vely
        if (abs(x - foodx) <= 10) and (abs(y - foody) <= 10):
            score = score + 10
            if((score)>int(high)):
                high=str(score)

            i=i+0.5
            snk_length =snk_length+5
            foodx = random.randrange(200,700)
            foody = random.randint(200,500)

        snk_head = []

        snk_head.append(x)
        snk_head.append(y)
        snk_list.append(snk_head)
        snake_plot(snk_list)
        if len(snk_list)>snk_length:
            del snk_list[0]

        score1("score:- "+str(score),red,5,5)
        score1("highscore:- " + str(high), red, 150, 5)

        pygame.draw.rect(gamewindow, red, [foodx, foody, 15, 15])
        pygame.display.update()
        if x<0 or x>900 or y<0 or y>700:
            exit_game=True
        if snk_head in snk_list[:-1]:
            exit_game=True
        if (exit_game):
            pygame.mixer.music.load("gameover.wav")
            pygame.mixer.music.play()
            with open("highscore.txt","w")as t:
                t.write((str(high)))

            while not quits:

                gamewindow.fill(white)

                score1("game over.press enter to restart", black, 100, 100)
                pygame.display.update()
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()


                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_RETURN:
                            game()

        clock.tick(30)



game()
pygame.quit()