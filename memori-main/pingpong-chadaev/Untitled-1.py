from pygame import *
from random import *
mixer.init()
fps = 80
clock = time.Clock()
speed_x = 3
speed_y = 3

game = True
finish = False
window = display.set_mode((700, 500))
display.set_caption("sss")

font.init()
font = font.SysFont('Arial',30)

bab = window.fill((0, 0, 0))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_speed2, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.speed2 = player_speed2
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        
        if keys_pressed[K_w] and self.rect.x < 650:
            self.rect.y-= self.speed
        if keys_pressed[K_s] and self.rect.x > 0:
            self.rect.y+= self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        
        if keys_pressed[K_UP] and self.rect.x > 650:
            self.rect.y+= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 0:
            self.rect.y-= self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.x-=self.speed2
        self.rect.y-=self.speed
        if self.rect.y <= 1:
            self.speed*=-1
        if self.rect.y > 430:
            self.speed*=-1
        if self.rect.x > 690:
            self.speed2*=-1
        if self.rect.x < 1:
            self.speed2*=-1


ball = Enemy("ball.png", 70, 70, 10, 10, 50, 50)
background = Player('background.png', 25, 70, 40, 40,350, 350)
p1 = Player('1.png', 50, 150, 10, 10, 35, 170)
p2 = Player2('2.png', 650, 150,10, 10, 35, 170 )

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False  
        if finish != True:
            ball.rect.x += speed_x
            ball.rect.y += speed_y
        if ball.rect.y > 500-50 or ball.rect.y < 0:
            speed_y *= -1
        elif e.type == KEYDOWN:
            if e.key ==K_SPACE:
               sprite1.fire()
    clock.tick(fps)
    
    window.fill((0, 0, 0))
    ball.reset()
    ball.update()
    p1.reset()
    p1.update()
    p2.reset()
    p2.update()
    display.update()
    
   