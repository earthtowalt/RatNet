# led controller optimized for use in 

import os
import socket

class LEDController:
	'''open tcp connection with nodemcu board. Provides capability to flash led on and off'''
	def __init__(self, ip, port, bs=1024):
		'''setup necessary variables'''
		self.IP = ip
		self.PORT = port
		self.BUFFER_SIZE = bs
		self.s = None
	
	def set_ip(self, ip):
		'''mutator for ip address'''
		self.IP = ip
		
	def set_port(self, port):
		'''mutator for port'''
		self.PORT = port
		
	def connect(self):
		'''attempt to open connection to ip:port'''
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			self.s.connect((self.IP, self.PORT))
			return 0
		except TimeoutError:
			self.s.close()
			self.s = None
			return 1
	def led_on(self):
		try:
			self.s.send(b'H')
			return 0
		except ConnectionResetError:
			self.s.close()
			return 1
			
	
	def led_off(self):
		try:
			self.s.send(b'L')
			return 0
		except ConnectionResetError:
			self.s.close()
			return 1
		
	def close(self):
		self.s.close()
		
	