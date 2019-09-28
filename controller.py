














# controller.py
# earthtowalt
# 9/24/16
# Controller file for the ratnet...
# sets up pygame control scheme and server

import pygame
import os, sys
import math, random, time
import socket

CAPTION = 'RAT CONTROLLER'
SCREEN_SIZE = (320,200)
BACKGROUND_COLOR = (0,0,0)
ICON_FILE = 'rat.png'

ip = '192.168.1.137'

class Control(object):
	'''Class defines methods for how the controller will interact with the rat'''
	def __init__(self):
		'''initialize controls and communication stuff'''
		# init screen
		self.screen = pygame.display.get_surface()
		self.screen_rect = self.screen.get_rect()
		# get keys
		self.keys = pygame.key.get_pressed()
		# setup joystick, if not joysticks found, then joy=None
		self.joy = initialize_gamepad()
		# left motor and right motor values 
		self.left_motor = 0
		self.right_motor = 0
		# keep running loop.
		self.done = False
		
		# set up communication. 
		
	
	def event_loop(self):
		'''handles all events'''
		for event in pygame.event.get():
			self.keys = pygame.key.get_pressed()
			if event.type == pygame.QUIT or self.keys[pygame.K_ESCAPE]:
				self.done = True 
			# handle events
			# grab motion of sticks and update value with motion. 
	
	def update(self):
		'''update server'''
		pass
		
	def message_display(self, text):
		'''draw message to the display'''
		largeText = pygame.font.Font('freesansbold.ttf',115)
		TextSurf, TextRect = text_objects(text, largeText)
		TextRect.center = ((SCREEN_SIZE/2),(SCREEN_SIZE/2))
		gameDisplay.blit(TextSurf, TextRect)
	
	def draw(self):
		'''draw important elements''' # screen elements are left and right motor values printed in #fixme some fancy way
		self.screen.fill(BACKGROUND_COLOR)
		self.motor_display()

	def motor_display(self):
		'''Draw the values of the motors on the window'''
		large_text = pygame.font.Font('freesansbold.ttf',20)
		
		left_surface, left_rect, = text_objects(str(self.left_motor), large_text)
		right_surface, right_rect = text_objects(str(self.right_motor), large_text)
		
		left_rect.center = ((SCREEN_SIZE[0]/4),(SCREEN_SIZE[1]/2))
		right_rect.center = ((SCREEN_SIZE[0] * 3 /4),(SCREEN_SIZE[1]/2))
		
		self.screen.blit(left_surface, left_rect)
		self.screen.blit(right_surface, right_rect)
		
	def main_loop(self):
		'''main loop'''
		while not self.done:
			self.event_loop()
			self.draw()
			pygame.display.flip()
			

def text_objects(text, font):
	text_surface = font.render(text, True, (255,255,255))
	return text_surface, text_surface.get_rect()

def initialize_gamepad():
	'''checks for gamepads and returns an intialized list of them if found'''
	joystick = None
	joystick = (pygame.joystick.Joystick(0))
	if joystick:
		joystick.init() 
	return joystick
	
def main():
	'''prepare display and start program'''
	os.environ['SLD_VIDEO_CENTERED'] = '1'
	#pygame window setup 
	pygame.init()
	pygame.display.set_caption(CAPTION)
	pygame.display.set_mode(SCREEN_SIZE)
	icon = pygame.image.load('rat.png')
	pygame.display.set_icon(icon)
	
	Control().main_loop()
	
	pygame.quit()
	sys.exit()
	

if __name__ == '__main__':
	main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	