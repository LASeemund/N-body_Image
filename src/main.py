from ball import Ball
from image import Img
import random
import pygame

#python -m pip install -U pygame==2.3.0 --user

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
renderV = 6

class Size:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    n_ball = 3
    #size = Size(7680, 4320)
    size = Size(1080, 720)
    dt = 0.5
    t = 0
    image = Img("save8k.png", size.x, size.y)

    genImage = False

    if genImage:
        # initialize the pygame module
        pygame.init()
        pygame.display.set_caption("minimal program")
        screen = pygame.display.set_mode((size.x/renderV,size.y/renderV))

    staticBall = []

    #cria os objetos parados
    for i in range(0, n_ball):
        staticBall.append(Ball(size.x, size.y, 10, m = 1000))
    
    if n_ball == 3:
        staticBall[0].setColor(red)
        staticBall[1].setColor(green)
        staticBall[2].setColor(blue)
    
    for i in staticBall:
        print(i)

    #main loop
    for y in range(size.y):
        for x in range(size.x):
            ball = Ball(0,0,50,100,x=x,y=y)

            initW = t
            while(True):
                #if t - initW >= 1:
                #    break
                
                c = (0,0,0)
                #calcula a colisao
                ct = False
                for sb in staticBall:
                    if ball.colisionBall(sb):
                        c = sb.rgb
                        ct = True
                        break
                if ct:
                    break
                ball.update(staticBall, dt)

                if genImage:
                    #draw
                    screen.fill((250,250,250))
                    if list(ball.getPos(renderV))[0] > 0:
                        pygame.draw.circle(screen, (255,255,0), ball.getPos(renderV), ball.r/2)
                    for sb in staticBall:
                        pygame.draw.circle(screen, sb.rgb, sb.getPos(renderV), sb.r/2)
                    pygame.display.flip()
                    #pygame.display.update()
                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            return 1
                #print(f"ball pos: ({ball.x},{ball.y}). ve: ({ball.v[0]},{ball.v[1]})")
                t += dt
            image.addPixel(c)
            #print(c)
        if ((y / size.y)*100) % 10 == 0:
            print("{}%".format((y / size.y)*100))

    image.save()

if __name__ == "__main__":
    main()