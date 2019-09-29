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
		print('connecting...')
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			self.s.connect((self.IP, self.PORT))
			return 0
		except TimeoutError:
			s.close()
			return 1
	def led_on(self):
		self.s.send(b'H')
	
	def led_off(self):
		self.s.send(b'L')
		
	def close(self):
		self.s.close()
		
	