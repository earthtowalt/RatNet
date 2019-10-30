














# single_controller.py
# earthtowalt
# 9/24/16
# Controller file for the ratnet...
# sets up pygame control scheme and server
# CONTROLS SINGLE RAT

import pygame
import os, sys
import math, random, time
import socket
from LEDController import LEDController

CAPTION = 'RAT CONTROLLER'
SCREEN_SIZE = (320,200)
BACKGROUND_COLOR = (0,0,0)
ICON_FILE = 'rat.png'

IP = '10.67.99.29'
PORT = 1337



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
		self.c = LEDController(IP, PORT)
		print('connecting...')
		while (self.c.connect()):
			print('connection timeout, trying again..')
		print('connected.')
			
	
	
	def event_loop(self):
		'''handles all events'''
		for event in pygame.event.get():
			self.keys = pygame.key.get_pressed()
			if event.type == pygame.QUIT or self.keys[pygame.K_ESCAPE]: # handle quit
				self.done = True
			elif event.type == pygame.JOYAXISMOTION: # handle joystick motion
				if event.axis == 1:
					self.left_motor = -round(self.joy.get_axis(1))
				elif event.axis == 3:
					self.right_motor = -round(self.joy.get_axis(3))
			elif event.type == pygame.JOYBUTTONDOWN:
				if event.button == 7:
					print('connecting...')
					if (self.c.connect()):
						print('connection failed')
					else:
						print('connected')
			
	
	def update(self):
		'''update server'''
		if self.left_motor == 1:
			self.c.led_on()
		else:
			self.c.led_off()
		
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
			self.update()
			self.draw()
			pygame.display.flip()
			pygame.time.wait(100)
			

def text_objects(text, font):
	text_surface = font.render(text, True, (255,255,255))
	return text_surface, text_surface.get_rect()

def initialize_gamepad():
	'''checks for gamepads and returns an intialized list of them if found'''
	joystick = None
	if pygame.joystick.get_count():
		joystick = (pygame.joystick.Joystick(0))
		joystick.init() 
	return joystick
	
def main():
	'''prepare display and start program'''
	os.environ['SLD_VIDEO_CENTERED'] = '1'
	#pygame window setup 
	pygame.init()
	pygame.display.set_caption(CAPTION)
	pygame.display.set_mode(SCREEN_SIZE)
	dir_path = os.path.dirname(os.path.realpath(__file__))
	icon = pygame.image.load(dir_path + '\\rat.png')
	pygame.display.set_icon(icon)
	
	Control().main_loop()
	
	pygame.quit()
	sys.exit()
	

if __name__ == '__main__':
	
	main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	