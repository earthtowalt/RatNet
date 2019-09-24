# controller.py
# earthtowalt
# 9/24/16
# Controller file for the ratnet...
# sets up pygame control scheme and server

import pygame
import os, sys
import math, random, time
import socket

CAPTION = "RAT CONTROLLER"
Screen_SIZE = (400,400)
BACKGROUND_COLOR = (0,0,0)

ip = '192.168.1.137'

class ServerController(object):
	'''Class defines methods for how the controller will interact with the server'''
	def __init__(self, controller):
		# setup controller input
		self.controller = controller
		if controller:
			self.id = controller.get_id()
		# FIXME setup server interface
	
	def update_movement()
		
	
	
	
	
	
	
	
	
	
	
	
	