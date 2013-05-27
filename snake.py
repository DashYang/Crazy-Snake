#!/usr/bin/python
# -*- coding: utf-8 -*-
# 记住上面这行是必须的，而且保存文件的编码要一致！
import sys, pygame 
from pygame.locals import * 
from random import randrange 

up =lambda x:(x[0]-1,x[1]) 
down = lambda x :(x[0]+1,x[1]) 
left = lambda x : (x[0],x[1]-1) 
right = lambda x : (x[0],x[1]+1) 
tl = lambda x :x<3 and x+1 or 0 
tr = lambda x :x==0 and 3 or x-1 
dire = [up,left,down,right] 
move = lambda x,y:[y(x[0])]+x[:-1] 
grow = lambda x,y:[y(x[0])]+x 
s = [(5,5),(5,6),(5,7)] 
blocks = []
d = up
food = randrange(0,30),randrange(0,40)
score = 0
food_type = 1
def create_block():
	while(1):
		block = randrange(0,30,1),randrange(0,40,1)
		#print(block)
		if (block != food and block not in s and block not in blocks):
			return [(block[0],block[1])]

FPSCLOCK=pygame.time.Clock() 

pygame.init() 
windows = pygame.display.set_mode((800,600))
#display caption
pygame.display.set_caption('crazy snake!!!') 
pygame.mouse.set_visible(0) 

screen = pygame.display.get_surface() 
screen.fill((0,0,0)) 
times=0.0 

font = pygame.font.Font("Ubuntu-B.ttf", 20)
text_surface = font.render(u"", 1, (255, 0,0))

while True: 
	time_passed = FPSCLOCK.tick(30) 
	if times>=150: 
		times =0.0 
		s = move(s,d) 
	else: 
		times += time_passed 
		for event in pygame.event.get(): 
			if event.type == QUIT: 
				sys.exit() 
			if event.type == KEYDOWN and event.key == K_UP: 
				s = move(s,d) 
			if event.type == KEYDOWN and event.key == K_LEFT: 
				d=dire[tl(dire.index(d))] 
			if event.type == KEYDOWN and event.key == K_RIGHT: 
				d=dire[tr(dire.index(d))] 
			if event.type == KEYDOWN and event.key == K_ESCAPE: 
				sys.exit()
	if s[0]==food or s[1] == food: 
		s = grow(s,d)
		score += 5
		if(food_type == 1):
			blocks += create_block()
		food_type = randrange(0,3,1)
		food =randrange(0,30),randrange(0,40) 
	if s[0] in s[1:] or s[0][0]<0 or s[0][0] >= 30 or s[0][1]<0 or s[0][1]>=40 or s[0] in blocks: 
			break 
	#clear the screen
	screen.fill((0,0,0))
	#draw new things
	for r,c in s: 
		pygame.draw.rect(screen,(255,0,0),(c*20,r*20,20,20)) 
	pygame.draw.rect(screen,(0,0,255),(food[1]*20,food[0]*20,20,20))
	for bx,by in blocks:
		pygame.draw.rect(screen,(0,255,255),(by*20,bx*20,20,20))

	text_surface = font.render("score:" + str(score), 1, (0, 255, 120))
	windows.blit(text_surface, (0,5))
	pygame.display.update()
