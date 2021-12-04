import pygame
import time
import random

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
dis_width = 800
dis_height  = 645
block_size = 10

class bullet:
    def __init__(self, x, y, direction, size):
        self.x = x
        self.y = y
        self.dir = direction
        self.block_size = size
        self.rect = self.rect = pygame.Rect(self.x, self.y, self.block_size, self.block_size)
    
    def update(self):
        if(self.dir == 'down'): 
            self.y += self.block_size * 1.5
            self.rect = pygame.Rect(self.x, self.y, self.block_size, self.block_size)
        elif(self.dir == 'up'):
            self.y -= self.block_size * 1.5
            self.rect = pygame.Rect(self.x, self.y, self.block_size, self.block_size)
        elif(self.dir == 'right'):
            self.x += (self.block_size * 1.5)
            self.rect = pygame.Rect(self.x, self.y, self.block_size, self.block_size)
        elif(self.dir == 'left'):
            self.x -= self.block_size * 1.5
            self.rect = pygame.Rect(self.x, self.y, self.block_size, self.block_size)
        return self.rect


class starship:
    def __init__(self, color, x, y, display):
        self.alive = True
        self.color = color
        self.x = x
        self.y = y
        self.display = display
        self.block_size=10
        self.dir = 'up'
        self.isVert = True
        self.bullets = []
        self.hasBullets = (len(self.bullets) > 0)
        self.side1 = pygame.Rect(self.x + self.block_size, self.y + self.block_size, self.block_size, 2 * self.block_size)
        self.side2 = pygame.Rect(self.x - self.block_size, self.y + self.block_size, self.block_size, 2 * self.block_size)
        self.front = pygame.Rect(self.x, self.y, self.block_size, 2 * self.block_size)

    
    def findDirection(self, x, y):
        if x > self.x:
            self.dir = 'right'
        elif x < self.x:
            self.dir = 'left'
        elif y < self.y:
            self.dir = 'up'
        elif y > self.y:
            self.dir = 'down'
    
    def detectBulletHit(self, bullets):
        if self.alive:
            for i in bullets:
                isHitFront = self.front.colliderect(i.rect)
                isHitSide1 = self.side1.colliderect(i.rect)
                isHitSide2 = self.side2.colliderect(i.rect)
                self.alive = (not isHitFront) and (not isHitSide1) and (not isHitSide2)
                if not self.alive:
                    bullets.remove(i)
                    break
        return self.alive

    def move(self, x, y):
        # bound check
        if ((abs(self.x - x) < 250) and (abs(self.y - y) < 250)):
            self.findDirection(x, y)
        self.x = x
        self.y = y

        # draw ship
        if(self.dir == 'down'): 
            self.side1 = pygame.Rect(self.x + self.block_size, self.y - self.block_size, self.block_size, 2 * self.block_size)
            self.side2 = pygame.Rect(self.x - self.block_size, self.y - self.block_size, self.block_size, 2 * self.block_size)
            self.front = pygame.Rect(self.x, self.y, self.block_size, 2 * self.block_size)
        elif(self.dir == 'up'):
            self.side1 = pygame.Rect(self.x + self.block_size, self.y + self.block_size, self.block_size, 2 * self.block_size)
            self.side2 = pygame.Rect(self.x - self.block_size, self.y + self.block_size, self.block_size, 2 * self.block_size)
            self.front = pygame.Rect(self.x, self.y, self.block_size, 2 * self.block_size)
        elif(self.dir == 'right'):
            self.side1 = pygame.Rect(self.x - self.block_size, self.y + self.block_size, 2 * self.block_size, self.block_size)
            self.side2 = pygame.Rect(self.x - self.block_size, self.y - self.block_size, 2 * self.block_size, self.block_size)
            self.front = pygame.Rect(self.x, self.y, 2 * self.block_size, self.block_size)
        elif(self.dir == 'left'):
            self.side1 = pygame.Rect(self.x + self.block_size, self.y + self.block_size, 2 * self.block_size, self.block_size)
            self.side2 = pygame.Rect(self.x + self.block_size, self.y - self.block_size, 2 * self.block_size, self.block_size)
            self.front = pygame.Rect(self.x, self.y, 2 * self.block_size, self.block_size)

        if self.alive:
            pygame.draw.rect(self.display, self.color, self.front)
            pygame.draw.rect(self.display, self.color, self.side1)
            pygame.draw.rect(self.display, self.color, self.side2)
    
        # draw bullets
        for i in range(0, len(self.bullets)):
            pygame.draw.rect(self.display, red, self.bullets[i].update())
        
        self.hasBullets = (len(self.bullets) > 0)

        # remove out of bound bullets
        for i in self.bullets:
            if (i.y > dis_height) or (i.y < 0) or (i.x > dis_width) or (i.x < 0):
                self.bullets.remove(i)

    def fire(self):
        if self.dir == 'right':
           self.bullets += [bullet(self.x + self.block_size, self.y, self.dir, self.block_size)]
        elif self.dir == 'down':
            self.bullets += [bullet(self.x, self.y + self.block_size, self.dir, self.block_size)]
        else:
            self.bullets += [bullet(self.x, self.y, self.dir, self.block_size)]


    def smartMove(self, heroX, heroY):
        x1_change = 0
        y1_change = 0
        enemy_speed = block_size/2

        # set persuit mode
        if (self.isVert) and (self.isClose(None, heroY)):
            self.isVert = False
        elif (not self.isVert) and (self.isClose(heroX, None)):
            self.isVert = True

   
        # smart persuit
        if self.y > heroY and self.isVert:
            # hero up
            y1_change = -enemy_speed
        elif self.y < heroY and self.isVert:
            # hero down
            y1_change = enemy_speed
        elif self.x > heroX and not self.isVert:
            # hero left
            x1_change = -enemy_speed
        elif self.x < heroX and not self.isVert:
            # hero right
            x1_change = enemy_speed
        else:
            # default
            y1_change = -enemy_speed

        
        # calculate next position
        nextx = self.x + x1_change
        nexty = self.y + y1_change

        # handle out of bounds
        if (nextx > dis_width): 
            x1 = 0
        elif (nextx < 0):
            x1 = dis_width
        elif nexty > dis_height: 
            y1 = 0
        elif nexty < 0:
            y1 = dis_height

        if random.randrange(1, 5) > 3:
            # determine if the bot should shoot
            if (self.y > heroY) and (self.dir == 'up') and (self.isClose(heroX, None)):
                # hero up and we are lined up on the x axis
                self.fire()
            elif (self.y < heroY) and (self.dir == 'down')  and (self.isClose(heroX, None)):
                # hero down and we are lined up on the x axis
                self.fire()
            elif (self.x < heroX) and (self.dir == 'right')  and (self.isClose(None, heroY)):
                # hero right and we are lined up on the y axis
                self.fire()
            elif (self.x > heroX) and (self.dir == 'left') and (self.isClose(None, heroY)):
                # hero left and we are lined up on the y axis
                self.fire()

        # call move function and pass in new location to move
        self.move(nextx, nexty)

    def isClose(self, x = None, y = None):
        if(x != None):
            return (self.x < x + 2* block_size) and (self.x > x - 2*block_size)
        elif(y != None):
            return (self.y < y + 2*block_size) and (self.y > y - 2*block_size)
        



def main():
    pygame.init()

 

    dis = pygame.display.set_mode((dis_width, dis_height))
    bg = pygame.image.load("sky.jpg")
    dis.blit(bg, (0, 0))

    pygame.display.set_caption('Starship')
 
    game_over = False
 
    x1 = dis_width/2
    y1 = dis_height/2
 
    hero = starship(white, dis_width/2, dis_height/2, dis)
    enemy = []

    level = 0
 
    x1_change = 0
    y1_change = 0
 
    clock = pygame.time.Clock()
    ship_speed=10
 
    font_style = pygame.font.SysFont(None, 50)
 
    def message(msg,color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width/2, dis_height/2])

    def displayLevel(msg):
        mesg = font_style.render("Level: "+ str(msg), True, white)
        dis.blit(mesg, [block_size, block_size])

    def displayScore(msg):
        mesg = font_style.render("Score: "+ str(msg), True, white)
        dis.blit(mesg, [dis_width - (15 * block_size), block_size])

    level = 0
    score = 0

    # get user input
    while not game_over:
        # new level enemies
        if len(enemy) <=0:
            level += 1
            for i in range(0, level):
                enemy += [starship(blue, random.randrange(0, dis_width, block_size), random.randrange(0, dis_width, block_size), dis)]
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0
                elif event.key == pygame.K_SPACE:
                    hero.fire()    
                elif event.key ==pygame.K_q:
                    game_over = True
 
        # calculate hero next position
        nextx = x1 + x1_change
        nexty = y1 + y1_change
        
        # handle hero wrap around
        if (nextx > dis_width): 
            x1 = 0
        elif (nextx < 0):
            x1 = dis_width
        elif nexty > dis_height: 
            y1 = 0
        elif nexty < 0:
            y1 = dis_height
        else:
            x1 += x1_change
            y1 += y1_change

        # apply hero move
        dis.blit(bg, (0, 0))
        hero.move(x1, y1)
        displayLevel(level)
        displayScore(score)

        # update enemy positions
        for ship in enemy:
            # detect if hero hit and end game
            if not hero.detectBulletHit(ship.bullets):
                game_over = True
            # detect if enemy is alive
            if ship.detectBulletHit(hero.bullets) and ship.alive:
                ship.smartMove(x1, y1)
            # draw bullets after dead
            else:
                ship.move(dis_width/2, dis_height - (2 * block_size))
            # remove enemy object if no bullets left and dead
            if not ship.alive and not ship.hasBullets:
                enemy.remove(ship)
                score += 1
 
        pygame.display.update()
 
        clock.tick(ship_speed)
 
    message("You lost",red)
    pygame.display.update()
    time.sleep(2)

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()