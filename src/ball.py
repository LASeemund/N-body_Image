import random
#from time import time

class Ball:
    def __init__(self, x_max=0, y_max=0 , r=1, m=0, v=(0,0), rgb=(0,0,0), x=-1, y=-1, idb=0):
        self.id = idb
        self.acc = (0,0)
        #set x e y
        seed = int(3.14**2)

        if x < 0 or y < 0:
            if x_max <= 0:
                x_max = random.randint(seed, 1000 + seed) % 1000
            if y_max <= 0:
                y_max = random.randint(seed, 1000 + seed) % 1000
            self.x = random.randint(0, x_max)
            self.y = random.randint(0, y_max)
        else:
            self.x = x
            self.y = y

        #set raio
        if r <= 0:
            r = 1
        self.r = r

        #set mass
        if m <= 0:
            m = 3.14
        self.m = m * (self.r/2)

        #set velocidade
        if type(v) != type((1,2)):
            self.v = (0,0)
        else:
            if len(v) != 2:
                self.v = (0,0)
            else:
                self.v = v

        #set rgb
        if type(rgb) != type((0,1,2)):
            rgb = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        else:
            if len(rgb) != 3 or rgb == (0,0,0):
                rgb = (random.randint(5,255), random.randint(5,255), random.randint(5,255))
        self.rgb = rgb
    
    def __str___(self):
        return f"Ball id: {self.id}, pos: ({self.x},{self.y}), r:{self.r}, m:{self.m}, rgb:{self.rgb}"
    def __repr__(self):
        return f"Ball id: {self.id}, pos: ({self.x},{self.y}), r:{self.r}, m:{self.m}, rgb:{self.rgb}"
    
    #set X e Y
    def setXY(self,x,y):
        if x < 0 or y < 0:
            print(f"Error: Ball.setXY(). Ball.id:{self.id}")
            raise Exception("x or y is less than 0.")
    
    #get pos: (x,y)
    def getPos(self,div=0):
        if div != 0:
            return (self.x/div, self.y/div)
        return (self.x, self.y)
    
    def setColor(self, rgb=(0,0,0)):
        if type(rgb) != type((0,1,2)):
            print(f"Error: Ball.setColor(). Ball.id:{self.id}")
            raise Exception("rgb is not a tuple.")
        elif len(rgb) != 3:
            print(f"Error: Ball.setColor(). Ball.id:{self.id}")
            raise Exception("rgb is not of length 3.")
        elif rgb[0] < 0 or rgb[0] > 255:
            print(f"Error: Ball.setColor(). Ball.id:{self.id}")
            raise Exception("rgb[0] is less than 0 or greater than 255.")
        elif rgb[1] < 0 or rgb[1] > 255:
            print(f"Error: Ball.setColor(). Ball.id:{self.id}")
            raise Exception("rgb[1] is less than 0 or greater than 255.")
        elif rgb[2] < 0 or rgb[2] > 255:
            print(f"Error: Ball.setColor(). Ball.id:{self.id}")
            raise Exception("rgb[2] is less than 0 or greater than 255.")
        self.rgb = rgb

    #verifica se o self colidiu com outro ball object
    def colisionBall(self, ball):
        if type(self) != type(ball):
            print(f"Error: Ball.colisionBall(). Ball.id:{self.id}")
            raise Exception("ball is not a Ball class")
        distancia = ((self.x - ball.x)**2 + (self.y - ball.y)**2)**(1/2)
        if self.r + ball.r >= distancia:
            return True
        return False
    
    def getAcc(self, ball):
        softening = 0.1
        G = 6.673 * (10**(-11))
        G = 1
        if type(self) == type(ball):
            calM = ball.m #* self.m
            dx = ball.x - self.x
            dy = ball.y - self.y
            # dx = self.x - ball.x
            # dy = self.y - ball.y
            i = (dx**2 + dy**2 + softening**2)**(-1.5)
            dx = G * (dx * i) * calM
            dy = G * (dy * i) * calM
            return (dx,dy)
        if type([]) == type(ball):
            a = [0,0]
            #a = list(self.acc)
            for i in ball:
                calM = i.m #* self.m
                if type(self) != type(i):
                    print(f"Error: Ball.colisionBall(). Ball.id:{self.id}")
                    raise Exception("ball is not a Ball class")
                dx = i.x - self.x
                dy = i.y - self.y
                # dx = self.x - i.x
                # dy = self.y - i.y
                inv = (dx**2 + dy**2 + softening**2)**(-1.5)
                a[0] += G * dx * inv * calM
                a[1] += G * dy * inv * calM
            return (a[0],a[1])
        return (0,0)
    
    def update(self, ball, dt):
        a = list(self.getAcc(ball))
        self.acc = (a[0],a[1])
        v = list(self.v)
        v[0] += a[0] * dt
        v[1] += a[1] * dt
        self.v = (v[0],v[1])
        self.x += v[0] #* dt
        self.y += v[1] #* dt
        