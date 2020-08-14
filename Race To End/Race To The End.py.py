import pygame
import time
import random
import math

pygame.init()

win_width = 900
win_height = 600

GameIcon = pygame.image.load('game icon.png')

Bg = pygame.image.load('game bg.png')

CarImage = pygame.image.load('racing-car.png')

StopImage = pygame.image.load('stop.png')


crashS = pygame.mixer.Sound("crash.wav")

coins = pygame.image.load('dollar.png')



win = pygame.display.set_mode((win_width, win_height))

pygame.display.set_caption('Race To End')

pygame.display.set_icon(GameIcon)


x = 380
y = 530
width = 64
height = 64
vel = 2.8
lives = 3
score = 0
crashstate = False
run = False
coinC = 0
highscore = 0



stopvel = 6
stopX2 = random.randint(10, 300)
stopX = random.randint(350, 800)
stopY = 35

coiny = 35
coinx = random.randint(10, 800)

def crash(count):
	global scorex
	global scorey
	global scoreSize
	global run
	global menu
	global startMenu
	global stopvel
	global lives
	global stopvel
	global score
	global highscore
	global HSM
	global fileH
	global coinC
	global fileH
	global hsr


	stopvel = 0

	stopX2 = random.randint(10, 300)
	topX = random.randint(350, 800)

	lives -= 1




	mouseP = pygame.mouse.get_pos()
	mouseC = pygame.mouse.get_pressed()

	stopvel == 0 

	if 750 + 80 > mouseP[0] > 750 and 480 + 50 > mouseP[1] > 480:
		if mouseC[0] == 1:
			run = False

			highscore += score

	if 350 + 80 > mouseP[0] > 350 and 480 + 50 > mouseP[1] > 480:
		if mouseC[0] == 1:

			highscore += score


			lives = 3
			stopvel = 4
			score = 0
			nice = True



	scorex = 330
	scorey = 400
	scoreSize = 45

	crashstate = True

	font = pygame.font.SysFont("comicsansms", 100)
	sFont = pygame.font.SysFont("comicsansms", 25)

	textb3 = sFont.render("Play", True, (0,0,0))
	textB2 = sFont.render("Quit", True, (0,0,0))


	crasht = font.render("You Crashed", True, (0, 0, 0))
	pygame.draw.rect(win, (255, 255, 255), (0, 0, win_width, win_height))

	pygame.draw.rect(win, (0 , 255, 0), (350, 480, 80, 50))


	font = pygame.font.SysFont("comicsansms", 45)
	text = font.render("score: "+str(count), True, (0, 0, 255))
	win.blit(text,(400, 350))
	win.blit(crasht,(230, 120))
	win.blit(textb3, (355, 480))

	pygame.draw.rect(win, (255, 0, 0), (750, 480, 80, 50))
	win.blit(textB2, (750, 480))
		
	pygame.display.update()


 
def isCollision():
	global lives
	global x
	global stopY
	global stopX
	global stopX2





	if y < stopY  + 128:
	 	print("y crossover")
	 	if x > stopX and x < stopX + 128 or x + 64 > stopX and x + 64 < stopX + 128:
	 		print("x crossover")
	 		lives -= 1
	 		stopY = 35
	 		stopX2 = random.randint(10, 800)
	 		stopX = random.randint(10, 800)

	 	if x > stopX2 and x < stopX2 + 128 or x + 64 > stopX2 and x + 64 < stopX2 + 128:
	 		print("x crossover")
	 		lives -= 1
	 		stopY = 35
	 		stopX2 = random.randint(10, 800)
	 		stopX = random.randint(10, 800)


def isCollisionCoin():
	global y
	global x
	global coinx
	global coiny
	global coinC
	global C
	global CM
	global fileC
	global coinC




	if y < coiny  + 128:
	 	print("y crossover")
	 	if x > coinx and x < coinx + 128 or x + 64 > coinx and x + 64 < coinx + 128:
	 		print("x crossover")
	 		coinC += 1
	 		coiny = 35
	 		coinx = random.randint(10, 800)


def livescount(count):
	font = pygame.font.SysFont("comicsansms", 20)
	text = font.render("Lives: "+str(count), True, (255, 0, 0))
	win.blit(text,(5, 3))

def scorecount(count):
	font = pygame.font.SysFont("comicsansms", 20)
	text = font.render("Score: "+str(count), True, (0, 0, 255))
	win.blit(text,(4, 21))

def coincount(count):
	global coinC
	font = pygame.font.SysFont("comicsansms", 20)
	text = font.render("Coins: "+ str(coinC), True, (255,255,0))
	win.blit(text,(4, 40))

def hscorecount():
	global highscore
	global HSM
	global hsr
	font = pygame.font.SysFont("comicsansms", 20)
	text = font.render("HighScore: "+ str(highscore) + "          ", True, (0,255,0))
	win.blit(text,(4, 63))



def startMenu():
	global run

	menu = True
	while menu:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

		mouseP = pygame.mouse.get_pos()
		mouseC = pygame.mouse.get_pressed()

		if 150 + 80 > mouseP[0] > 150 and 480 + 50 > mouseP[1] > 480:
			if mouseC[0] == 1:
				menu = False
				run = True


		if 750 + 80 > mouseP[0] > 750 and 480 + 50 > mouseP[1] > 480:
			if mouseC[0] == 1:
				menu = False

     

			
		win.fill((250, 250,250))

		sFont = pygame.font.SysFont("comicsansms", 25)
		font = pygame.font.SysFont("comicsansms", 100)
		text = font.render("Race To  The ", True, (0,185,255))
		text1 = font.render("     End", True, (0,185,255))
		textB1 = sFont.render("Start", True, (0,0,0))
		textB2 = sFont.render("Quit", True, (0,0,0))
		textB3 = sFont.render("Shop", True, (0,0,0))
		textby = sFont.render("by Gurman", True, (150, 255, 0))


		pygame.draw.rect(win, (0, 255, 0), (150, 480, 80, 50))
		pygame.draw.rect(win, (255, 0, 0), (750, 480, 80, 50))


		win.blit(text,(200, 50))
		win.blit(text1, (250, 150)) 
		win.blit(textB1, (153, 480))
		win.blit(textB2, (753, 480))
		win.blit(textby, (450, 560))
		pygame.display.update()
		
run = False

startMenu()
while run:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		x -= vel

	if keys[pygame.K_RIGHT]:
		x += vel

	if x >= win_width - 50 :
		x -= vel

	if x <= -1:
		x += vel

	if stopX == stopX2:
		stopX2 += 138

	if stopX == stopX2:
		stopX2 -= 138

	stopY += stopvel


	if stopY >= win_height - 64:
		stopY = 35
		stopX2 = random.randint(10, 300)
		stopX = random.randint(350, 800)


	isCollision()
	isCollisionCoin()



	win.blit(Bg, (0, 0))
	win.blit(CarImage, (x, y))
	win.blit(coins, (coinx, coiny))

	win.blit(StopImage, (stopX, stopY))
	win.blit(StopImage, (stopX2, stopY))


	livescount(lives)

	scorecount(score)

	coincount(coinC)

	hscorecount()



	if y <= stopY and not x == stopX:
		score += 1

	if lives == 0:
		crash(score)
		pygame.mixer.Sound.play(crashS)

	if lives <= 0:
		crash(score)

	coiny += 4

	if coiny >= win_height :
		coiny = 35
		coinx = random.randint(10, 800)


	if score == 4:
		stopvel = 7

	if score == 10 :
		stopvel = 8

	if score == 16 :
		stopvel = 9

	if score == 25:
		stopvel = 10


	if score == 50:
		stopvel = 13





	pygame.display.update()


pygame.quit()